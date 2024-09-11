import glob, os, sys
import ROOT as r
import yaml
import time
import uuid
import EventProducer.common.utils as ut
class checker_yaml():

#__________________________________________________________
    def __init__(self, indir, para, fext, process, yamldir):
        self.indir  = indir
        self.para   = para
        self.fext   = fext
        self.process = process
        self.yamldir = yamldir
        self.filecounting_dir = f'/tmp/fcc_filecounting_{uuid.uuid4().hex[:14]}'
        self.count = 0

        if not os.path.isdir(self.filecounting_dir):
            os.system('mkdir %s' % self.filecounting_dir)
            print(f'Created temporary file counting direcotory: {self.filecounting_dir}')

#__________________________________________________________
    def checkFile_stdhep(self, f):

        hack = True
        #hack = False

        size=os.path.getsize(f)
        if size==0:
            self.count+=1
            print ('file size is 0, job is bad')
            return -1,False

        # Clear all STDHEP file from the temporary directory
        os.system(f'rm -f {self.filecounting_dir}/*stdhep*')

        if hack: 
           cmd = 'cp /dev/null %s/%s' % (self.filecounting_dir, f.split('/')[-1])
        else :
           cmd = 'cp %s %s'%(f, self.filecounting_dir)

        outputCMD = ut.getCommandOutput(cmd)
        fcount = '%s/%s' % (self.filecounting_dir, f.split('/')[-1])
        if os.path.isfile(fcount):
            cmd='gunzip %s'%(fcount)
            stderr=''
            if not hack:
                outputCMD = ut.getCommandOutput(cmd)
                stderr=outputCMD["stderr"]
            if len(stderr)>0:
                print ('can not unzip the file, try again (count %i)'%self.count)
                self.count+=1
                os.system('rm %s'%(fcount))
                return -1,False

            nevts = 100000 # temporary hack !!
            if not hack:
                if os.path.isfile('tmp.slcio'):
                    os.system('rm tmp.slcio')
                cmd='stdhepjob %s tmp.slcio 1000000000 | grep \"written to LCIO\" ' %(fcount.replace('.gz',''))
                outputCMD = ut.getCommandOutput(cmd)
                if len( outputCMD["stdout"].split() ) < 2:
                    print('... problem in checkFile_stdhep with stdhepjob')
                snevts = outputCMD["stdout"].split()[1]
                nevts=int(snevts)
                os.system('rm tmp.slcio')
                if nevts==0:
                    print ('no events in the file, job is bad')
                    os.system('rm %s'%(fcount.replace('.gz','')))
                    return 0,False
                else:
                    print ('%i events in file %s, job is good'%(nevts,f))
                    os.system('rm %s'%(fcount.replace('.gz','')))
            return nevts,True
        else:
            print ('file not properly copied... try again (count %i)'%self.count)
            if not ut.testeos(self.para.eostest,self.para.eostest_size):
                print ('eos seems to have problems, should check, will exit')
                sys.exit(3)
            self.count+=1
            return -1, False



#__________________________________________________________
    def checkFile_lhe(self, filepath):
        # Check file size
        size = os.path.getsize(filepath)
        if size == 0:
            self.count += 1
            print(f'File "{filepath}" is empty, job is bad!')
            return -1, False

        # Clear temporary directory from LHE files
        os.system(f'rm -f {self.filecounting_dir}/*lhe*')

        # Copy zipped LHE file to temporary directory
        cmd = 'cp %s %s' % (filepath, self.filecounting_dir)
        outputCMD = ut.getCommandOutput(cmd)

        filepath_local = '%s/%s' % (self.filecounting_dir, filepath.split('/')[-1])
        if os.path.isfile(filepath_local):
            cmd = f'gunzip {filepath_local}'
            outputCMD = ut.getCommandOutput(cmd)
            stderr = outputCMD["stderr"]
            if len(stderr) > 0:
                print('Can not unzip the file, try again (count %i)' %self.count)
                self.count += 1
                os.system('rm %s' % (filepath_local))
                return -1, False

            cmd = 'grep \"<event>\" %s | wc -l' % (filepath_local.replace('.gz', ''))
            outputCMD = ut.getCommandOutput(cmd)
            stdoutplit = outputCMD["stdout"].split(' ')
            nevts = int(stdoutplit[0])
            if nevts == 0:
                print ('no events in the file, job is bad')
                os.system('rm %s'%(filepath_local.replace('.gz','')))
                return 0, False
            else: 
                print(f'{nevts} events in file "{filepath}", job is good')
                os.system('rm %s'%(filepath_local.replace('.gz','')))
                return nevts, True
        else:
            print ('file not properly copied... try again (count %i)'%self.count)
            if not ut.testeos(self.para.eostest,self.para.eostest_size):
                print ('eos seems to have problems, should check, will exit')
                sys.exit(3)
            self.count+=1
            return -1, False


#__________________________________________________________
    def checkFile_root(self, f, tname):
        tf=None
        try:
            tf=r.TFile.Open(f)
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            print ('file ===%s=== must be deleted'%f)
            return -1,-1,False
        except ValueError:
            print ("Could read the file")
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            print ('file ===%s=== must be deleted'%f)
        #os.system('rm %s'%f)
            return -1,-1,False

        tf=r.TFile.Open(f)
        tt=None
        try :
            tt=tf.Get(tname)
            if tt==None:
                print ('file ===%s=== must be deleted'%f)
            #os.system('rm %s'%f)
                return -1,-1,False

        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            print ('file ===%s=== must be deleted'%f)
            return -1,-1,False
        except ValueError:
            print ("Could read the file")
        except OSError:#for root 6.24
            print ('file ===%s=== must be deleted'%f)
        #os.system('rm %s'%f)
            return -1,-1,False
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            print ('file ===%s=== must be deleted'%f)
        #os.system('rm %s'%f)
            return -1,-1,False

        if not ut.isValidROOTfile(f):
            return -1,-1,False
    
        f=r.TFile.Open(f)
        tt=tf.Get(tname)
        nentries=tt.GetEntries()
        weight_sum=float(nentries)

        ##TODO: here we miss the metadata to get the sum of weights properly done
	## compute sum of weights
        #r.gROOT.SetBatch(True)
        #tt.Draw('mcEventWeights.value[0]>>histo')
        #histo=r.gDirectory.Get('histo')
        #
        #try:
        #    weight_sum=float(nentries)*histo.GetMean()
        #except AttributeError as e:
        #    print ("error ",e)
        #    if nentries!=100000 and nentries!=10000:
        #        print ('nentries  ',nentries)
        #        #nentries=0
        if nentries==0:
            print ('file has 0 entries ===%s=== must be deleted'%f)
            return 0,0,False

        print ('%i events in the file and sum of weights = %f --> job is good'%(nentries,weight_sum))
        return int(nentries),weight_sum,True

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
            print ('eos seems to have problems, should check, will exit')
            sys.exit(3)

        for l in ldir:
            if self.process!='' and self.process!=l: 
                continue
            #continue if process has been checked
            if l=='BADPYTHIA' or l=='lhe' or l=="__restored_files__" or l=="backup": continue
            print ('%s/%s/check'%(self.yamldir,l))
            if not ut.file_exist('%s/%s/check'%(self.yamldir,l)) and not force: continue
            print ('--------------------- ',l)
            process=l
            All_files = glob.glob("%s/%s/events_*%s"%(self.indir,l,self.fext))
            print ('number of files  ',len(All_files))
            if len(All_files)==0:continue
            
            print ('process from the input directory ',process)

            outdir = self.makeyamldir(self.yamldir+process)
            hasbeenchecked=False
            nevents_tot=0
            sumweights_tot=0
            njobsdone_tot=0
            njobsbad_tot=0
            userjobs=[]
            for f in All_files:

                self.count = 0
                if not os.path.isfile(f): 
                    print ('file does not exists... %s'%f)
                    continue
            
                jobid=f.split('_')[-1]
                jobid=jobid.replace(self.fext,'')
                userid=ut.find_owner(f)

                outfile='%sevents_%s.yaml'%(outdir,jobid)
                if  ut.getsize(outfile)==0:
                    cmd="rm %s"%(outfile)
                    print ('file size 0, remove and continue   ',cmd)
                    os.system(cmd)
                    continue
                if ut.file_exist(outfile) and ut.getsize(outfile)> 100 and not force:
                    doc = None
                    with open(outfile) as ftmp:
                        try:
                            doc = yaml.load(ftmp, Loader=yaml.FullLoader)
                        except yaml.YAMLError as exc:
                            print(exc)
                        except IOError as exc:
                            print ("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                            print ("outfile ",outfile)
                        try: 
                            if doc!=None:value = doc['processing']['status']
                            if value=='DONE': continue
        
                        except KeyError as e:
                            print ('status %s does not exist' % str(e))

                hasbeenchecked=True
                print ('-----------',f)

                if '.root' in self.fext:
                    nevts, sumw, check=self.checkFile_root(f, self.para.treename)
                    status='DONE'
                    if not check: status='BAD' 

                    if status=='DONE':
                        nevents_tot+=nevts
                        sumweights_tot+=sumw
                        njobsdone_tot+=1
                        if userid not in userjobs:userjobs.append(userid)
                    else:
                        njobsbad_tot+=1

                    dic = {'processing':{
                            'process':process, 
                            'jobid':jobid,
                            'nevents':nevts,
                            'sumofweights':sumw,
                            'status':status,
                            'out':f,
                            'size':os.path.getsize(f),
                            'user':userid
                            }
                           }
                    try:
                        with open(outfile, 'w') as outyaml:
                            yaml.dump(dic, outyaml, default_flow_style=False) 
                        continue
                    except IOError as exc:
                            print ("I/O error({0}): {1}".format(exc.errno, exc.strerror))
                            print ("outfile ",outfile)
                            time.sleep(10)
                            with open(outfile, 'w') as outyaml:
                                yaml.dump(dic, outyaml, default_flow_style=False) 
                            continue

                elif '.lhe.gz' in self.fext:
                    nevts, check = self.checkFile_lhe(f)
                    while nevts == -1 and not check:
                        nevts,check = self.checkFile_lhe(f)
                        if self.count==10:
                            print ('can not copy or unzip the file, declare it wrong')
                            break

                    status = 'DONE'
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

                elif '.stdhep.gz' in self.fext:
                    nevts,check=self.checkFile_stdhep(f)
                    while nevts==-1 and not check:
                        nevts,check=self.checkFile_lhe(f)
                        if self.count==10:
                            print ('can not copy or unzip the file, declare it wrong')
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
                    print ('not correct file extension %s'%self.fext)
            
            if hasbeenchecked:
                userstmp=''
                for u in userjobs:
                    if userstmp=='':
                        userstmp=u
                    else:
                        userstmp+=',',u

                cmdp='<pre>date=%s \t time=%s njobs=%i \t nevents=%i  \t sumofweights=%f\t njobbad=%i \t process=%s \t users=%s</pre>\n'%(ut.getdate_str(),ut.gettime_str() ,njobsdone_tot,nevents_tot, sumweights_tot, njobsbad_tot,process,userstmp)
                stat_exist=ut.file_exist(statfile)
                with open(statfile, "a") as myfile:
                    if not stat_exist: 
                        myfile.write('<link href="/afs/cern.ch/user/f/fccsw/www/style/txtstyle.css" rel="stylesheet" type="text/css" />\n')
                        myfile.write('<style type="text/css"> /*<![CDATA[*/ .espace{ margin-left:3em } .espace2{ margin-top:9em } /*]]>*/ </style>\n')

                    myfile.write(cmdp)

                print ('date=%s  time=%s  njobs=%i  nevents=%i  sumofweights=%f  njobbad=%i  process=%s users=%s'%(ut.getdate_str(),ut.gettime_str() ,njobsdone_tot,nevents_tot,sumweights_tot, njobsbad_tot,process,userstmp))



