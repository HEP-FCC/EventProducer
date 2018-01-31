#python check_outputs.py /eos/experiment/fcc/hh/simulation/samples/v01
import glob, os, sys,subprocess,cPickle
import commands
import time
import random
from datetime import datetime
import ROOT as r
import json
import yaml
import EventProducer.common.utils as ut

class checker_yaml():

#__________________________________________________________
    def __init__(self, indir, para, fext, process, version):
        self.indir  = indir
        self.para   = para
        self.fext   = fext
        self.process = process
        self.yamldir = self.para.yamldir
        if 'lhe' in self.fext:
           self.yamldir = self.yamldir+'lhe/'
           self.yamlcheck = para.yamlcheck_lhe

        elif 'root' in  self.fext:
            self.yamldir = self.yamldir+version+'/'
            self.yamlcheck = para.yamlcheck_reco.replace('VERSION',version)
        else:
            print 'file extension not known... exit'
            sys.exit(3)


#__________________________________________________________
    def checkFile_lhe(self, f):
        count=0
        size=os.path.getsize(f)
        if size==0:
            print 'file size is 0, job is bad'
            return -1,False

        filecounting='filecounting'
        if os.path.isdir(filecounting)==False:
            os.system('mkdir %s'%filecounting)
        cmd='cp %s %s'%(f,filecounting)
        print cmd
        outputCMD = ut.getCommandOutput(cmd)
        fcount='%s/%s'%(filecounting,f.split('/')[-1])
        if os.path.isfile(fcount):
            os.system('gunzip %s'%(fcount))
            cmd='grep \"<event>\" %s | wc -l'%(fcount.replace('.gz',''))
            outputCMD = ut.getCommandOutput(cmd)
            stdoutplit=outputCMD["stdout"].split(' ')
            nevts=int(stdoutplit[0])
            if nevts==0:
                print 'no events in the file, job is bad'
                os.system('rm %s'%(fcount.replace('.gz','')))
                return 0,False
            else: 
                print '%i events in the file, job is good'%nevts
                os.system('rm %s'%(fcount.replace('.gz','')))
                return nevts,True
        else:
            print 'file not properly copied... try again (count %i)'%count
            if not ut.testeos(self.para.eostest,self.para.eostest_size):
                print 'eos seems to have problems, should check, will exit'
                sys.exit(3)
            count+=1
            checkFile_lhe(f)
            if count==10:
                print 'can not copy the file, declare it wrong'
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
    def check(self):

        #ldir=[x[0] for x in os.walk(self.indir)]
        ldir=next(os.walk(self.indir))[1]
        
        if not ut.testeos(self.para.eostest,self.para.eostest_size):
            print 'eos seems to have problems, should check, will exit'
            sys.exit(3)
    
        for l in ldir:
            print '--------------------- ',l
            process=l
            All_files = glob.glob("%s/%s/events_*%s"%(self.indir,l,self.fext))
            print 'number of files  ',len(All_files)
            if len(All_files)==0:continue
            if l=='lhe' or l=='BADLYMOVED' or l=="__restored_files__": continue
            print 'process from the input directory ',process
            if self.process!='' and self.process!=l: 
                continue

            outdir = self.makeyamldir(self.yamldir+process)

            ntot=0
            hasbeenchecked=False
            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
            
                jobid=f.split('_')[-1]
                jobid=jobid.replace(self.fext,'')
                userid=ut.find_owner(f)

                outfile='%sevents_%s.yaml'%(outdir,jobid)
                if ut.file_exist(outfile) and ut.getsize(outfile)> 80: continue
                hasbeenchecked=True
                print '-----------',f

                if '.root' in self.fext:
                    nevts, check=self.checkFile_root(f, self.para.treename)
                    status='DONE'
                    if not check: status='BAD' 
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
                    status='DONE'
                    if not check: status='BAD' 
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
    
            if hasbeenchecked:ut.yamlstatus(self.yamlcheck, process, False)



