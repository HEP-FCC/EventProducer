#python check_outputs.py /eos/experiment/fcc/hh/simulation/samples/v01
import glob, os, sys,subprocess,cPickle
import commands
import time
import random
from datetime import datetime
import ROOT as r
import json
import EventProducer.common.utils as ut
import EventProducer.common.dicwriter as dicr
import EventProducer.common.isreading as isr


class checker():

#__________________________________________________________
    def __init__(self,indict, indir, inread, para, fext, process):
        self.indict = indict
        self.indir  = indir
        self.inread = inread
        self.para   = para
        self.fext   = fext
        self.mydict = None
        self.process = process

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
        if tt.GetEntries()==0:
            print 'file has 0 entries ===%s=== must be deleted'%f
            return 0,False


        return tt.GetEntries(),True
#__________________________________________________________
    def check(self):

        ##CLEMENT FOR TEST, to be removed
        ldir=[x[0] for x in os.walk(self.indir)]
        #ldir=['/eos/experiment/fcc/hh/generation/mg5_amcatnlo/lhe/pp_ee_nlo/']
        #ldir=['/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v02/pp_ee_nlo/']

        #self.indict='test_checkoutput_root.json'
        #self.inread='testRead_checkoutput_root.json'
        ##CLEMENT FOR TEST, to be removed

        self.mydict=dicr.dicwriter(self.indict)
        readdic=isr.isreading(self.inread, self.indict)
        readdic.backup('checker')
        readdic.reading() 

        if not ut.testeos(self.para.eostest,self.para.eostest_size):
            print 'eos seems to have problems, should check, will exit'
            sys.exit(3)
    
        for l in ldir:
            All_files = glob.glob("%s/events_*%s"%(l,self.fext))
            if len(All_files)==0:continue
        
            keys=l.split('/')
            if keys[-1]!='':process=keys[-1]
            else:process=keys[len(keys)-2]
            
            print 'process from the input directory ',process
            if self.process!='' and self.process!=process: 
                continue
            ntot=0
            for f in All_files:
                if not os.path.isfile(f): 
                    print 'file does not exists... %s'%f
                    continue
                print '-----------',f
            
                jobid=f.split('_')[-1]
                jobid=jobid.replace(self.fext,'')
                userid=ut.find_owner(f)
                if self.mydict.jobexits(process,int(jobid)):
                    print 'already exists, continue'
                    continue

                if '.root' in self.fext:
                    nevts, check=self.checkFile_root(f, self.para.treename)
                    status='DONE'
                    if not check: status='BAD' 
                    dic = {'process':process, 
                           'jobid':jobid,
                           'nevents':nevts,
                           'status':status,
                           'out':l,
                           'size':os.path.getsize(f),
                           'user':userid,
                           'provenance':''
                           }
                    self.mydict.addjob(dic)
                    continue
                
                elif '.lhe.gz' in self.fext:
                    nevts,check=self.checkFile_lhe(f)
                    status='DONE'
                    if not check: status='BAD' 
                    dic = {'process':process, 
                           'jobid':jobid,
                           'nevents':nevts,
                           'status':status,
                           'out':l,
                           'size':os.path.getsize(f),
                           'user':userid
                           }
                    self.mydict.addjob(dic)
                    continue
                else:
                    print 'not correct file extension %s'%self.fext
    
        self.mydict.write()
        readdic.comparedics()
        readdic.finalize()
