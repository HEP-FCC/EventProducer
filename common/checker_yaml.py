#python check_outputs.py /eos/experiment/fcc/hh/simulation/samples/v01
import glob, os, sys
import ROOT as r
import yaml
import EventProducer.common.utils as ut

class checker_yaml():

#__________________________________________________________
    def __init__(self, indir, para, fext, process, yamldir, yamlcheck):
        self.indir  = indir
        self.para   = para
        self.fext   = fext
        self.process = process
        self.yamldir = yamldir
        self.yamlcheck = yamlcheck
        self.count = 0



#__________________________________________________________
    def checkFile_lhe(self, f):
        size=os.path.getsize(f)
        if size==0:
            self.count+=1
            print 'file size is 0, job is bad'
            return -1,False

        filecounting='filecounting'
        if os.path.isdir(filecounting)==False:
            os.system('mkdir %s'%filecounting)
        cmd='cp %s %s'%(f,filecounting)
        outputCMD = ut.getCommandOutput(cmd)
        fcount='%s/%s'%(filecounting,f.split('/')[-1])
        if os.path.isfile(fcount):
            cmd='gunzip %s'%(fcount)
            outputCMD = ut.getCommandOutput(cmd)
            stderr=outputCMD["stderr"]
            if len(stderr)>0:
                print 'can not unzip the file, try again (count %i)'%self.count
                self.count+=1
                os.system('rm %s'%(fcount))
                return -1,False

            cmd='grep \"<event>\" %s | wc -l'%(fcount.replace('.gz',''))
            outputCMD = ut.getCommandOutput(cmd)
            stdoutplit=outputCMD["stdout"].split(' ')
            nevts=int(stdoutplit[0])
            if nevts==0:
                print 'no events in the file, job is bad'
                os.system('rm %s'%(fcount.replace('.gz','')))
                return 0,False
            else: 
                print '%i events in file %s, job is good'%(nevts,f)
                os.system('rm %s'%(fcount.replace('.gz','')))
                return nevts,True
        else:
            print 'file not properly copied... try again (count %i)'%self.count
            if not ut.testeos(self.para.eostest,self.para.eostest_size):
                print 'eos seems to have problems, should check, will exit'
                sys.exit(3)
            self.count+=1
            return -1, False


#__________________________________________________________
    def checkFile_root(self, f, tname):
        tf=None
        try:
            tf=r.TFile.Open(f)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could read the file"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            print 'file ===%s=== must be deleted'%f
        #os.system('rm %s'%f)
            return -1,False

        tf=r.TFile.Open(f)
        tt=None
        try :
            tt=tf.Get(tname)
            if tt==None:
                print 'file ===%s=== must be deleted'%f
            #os.system('rm %s'%f)
                return False

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could read the file"
        except:
            print "Unexpected error:", sys.exc_info()[0]
            print 'file ===%s=== must be deleted'%f
        #os.system('rm %s'%f)
            return -1,False
    

        if not ut.isValidROOTfile(f):
            return -1,False
    
        f=r.TFile.Open(f)
        tt=tf.Get(tname)
        nentries=tt.GetEntries()
        if nentries==0:
            print 'file has 0 entries ===%s=== must be deleted'%f
            return 0,False
        
        print  '%i events in the file, job is good'%nentries
        return int(nentries),True

#__________________________________________________________
    def makeyamldir(self, outdir):

        if not ut.dir_exist(outdir):
            os.system("mkdir -p %s"%outdir)
    
        if  outdir[-1]!='/':
            outdir+='/'

        return outdir

#__________________________________________________________
    def check(self, force, statfile):

        #ldir=[x[0] for x in os.walk(self.indir)]
        ldir=next(os.walk(self.indir))[1]
        
        if not ut.testeos(self.para.eostest,self.para.eostest_size):
            print 'eos seems to have problems, should check, will exit'
            sys.exit(3)
    
        for l in ldir:
            if self.process!='' and self.process!=l: 
                continue
            #continue if process has been checked
            if ut.yamlcheck(self.yamlcheck, l) and not force :continue

            print '--------------------- ',l
            process=l
            All_files = glob.glob("%s/%s/events_*%s"%(self.indir,l,self.fext))
            print 'number of files  ',len(All_files)
            if len(All_files)==0:continue
            if l=='lhe' or l=="__restored_files__" or l=="backup": continue
            print 'process from the input directory ',process

            outdir = self.makeyamldir(self.yamldir+process)
            hasbeenchecked=False
            nevents_tot=0
            njobsdone_tot=0
            njobsbad_tot=0
            for f in All_files:

                self.count = 0
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
            
                jobid=f.split('_')[-1]
                jobid=jobid.replace(self.fext,'')
                userid=ut.find_owner(f)

                outfile='%sevents_%s.yaml'%(outdir,jobid)
                if ut.file_exist(outfile) and ut.getsize(outfile)> 100 and not force: continue
                hasbeenchecked=True
                print '-----------',f

                if '.root' in self.fext:
                    nevts, check=self.checkFile_root(f, self.para.treename)
                    status='DONE'
                    if not check: status='BAD' 

                    if status=='DONE':
                        nevents_tot+=nevts
                        njobsdone_tot+=1
                    else:
                        njobsbad_tot+=1

                    dic = {'processing':{
                            'process':process, 
                            'jobid':jobid,
                            'nevents':nevts,
                            'status':status,
                            'out':f,
                            'size':os.path.getsize(f),
                            'user':userid
                            }
                           }
                    with open(outfile, 'w') as outyaml:
                        yaml.dump(dic, outyaml, default_flow_style=False) 
                    continue
                
                elif '.lhe.gz' in self.fext:
                    nevts,check=self.checkFile_lhe(f)
                    while nevts==-1 and not check:
                        nevts,check=self.checkFile_lhe(f)
                        if self.count==10:
                            print 'can not copy or unzip the file, declare it wrong'
                            break

                    status='DONE'
                    if not check: status='BAD' 

                    if status=='DONE':
                        nevents_tot+=nevts
                        njobsdone_tot+=1
                    else:
                        njobsbad_tot+=1

                    dic = {'processing':{
                            'process':process, 
                            'jobid':jobid,
                            'nevents':nevts,
                            'status':status,
                            'out':f,
                            'size':os.path.getsize(f),
                            'user':userid
                            }
                           }
                    with open(outfile, 'w') as outyaml:
                        yaml.dump(dic, outyaml, default_flow_style=False) 
                    continue
                else:
                    print 'not correct file extension %s'%self.fext
            
            if hasbeenchecked:
                ut.yamlstatus(self.yamlcheck, process, False)
                cmdp='<pre>date=%s \t time=%s njobs=%i \t nevents=%i \t njobbad=%i \t process=%s </pre>\n'%(ut.getdate_str(),ut.gettime_str() ,njobsdone_tot,nevents_tot,njobsbad_tot,process)
                stat_exist=ut.file_exist(statfile)
                with open(statfile, "a") as myfile:
                    if not stat_exist: 
                        myfile.write('<link href="/afs/cern.ch/user/h/helsens/www/style/txtstyle.css" rel="stylesheet" type="text/css" />\n')
                        myfile.write('<style type="text/css"> /*<![CDATA[*/ .espace{ margin-left:3em } .espace2{ margin-top:9em } /*]]>*/ </style>\n')

                    myfile.write(cmdp)

                print 'date=%s  time=%s  njobs=%i  nevents=%i  njobbad=%i  process=%s'%(ut.getdate_str(),ut.gettime_str() ,njobsdone_tot,nevents_tot,njobsbad_tot,process)



