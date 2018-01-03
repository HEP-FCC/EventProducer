#!/usr/bin/env python
import os, sys
import commands
import time
import random
import EventProducer.common.utils as ut

class send_lhe():

#__________________________________________________________
    def __init__(self,njobs,events, process, islsf, queue, para):
        self.njobs   = njobs
        self.events  = events
        self.process = process
        self.islsf   = islsf
        self.queue   = queue
        self.user    = os.environ['USER']
        self.para    = para
        self.batch   = 'condor'
        if self.islsf:
            self.batch='lsf'
#__________________________________________________________
    def send(self):
        Dir = os.getcwd()
        nbjobsSub=0
    
        gptotest='%s/%s.tar.gz'%(self.para.gp_dir,self.process)
        if ut.eosexist(gptotest)==False:
            print 'Gridpack=======',gptotest,'======= does not exist'
            sys.exit(3)

        processFound=False
        for pr in self.para.gridpacklist:
            if '*' in self.process:
                if (self.process!='') and (self.process not in pr): continue
            else:
                if (self.process!='') and (self.process != pr): continue
            processFound=True
            
            logdir=Dir+"/BatchOutputs/%s"%(pr)
            os.system("mkdir -p %s"%logdir)

            for i in xrange(self.njobs):
                uid = int(ut.getuid(self.user))
                frunname = 'job%i.sh'%(uid) 
                frunfull = '%s/%s'%(logdir,frunname)

                frun = None
                try:
                    frun = open(frunfull, 'w')
                except IOError as e:
                    print "I/O error({0}): {1}".format(e.errno, e.strerror)
                    time.sleep(10)
                    frun = open(frunfull, 'w')

                commands.getstatusoutput('chmod 777 %s'%frunfull)
                frun.write('unset LD_LIBRARY_PATH\n')
                frun.write('unset PYTHONHOME\n')
                frun.write('unset PYTHONPATH\n')
                frun.write('mkdir job%i_%s\n'%(uid,pr))
                frun.write('cd job%i_%s\n'%(uid,pr))
                frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
                frun.write('source %s\n'%(self.para.stack))
                frun.write('mkdir %s\n'%(self.para.lhe_dir))
                frun.write('mkdir %s%s\n'%(self.para.lhe_dir,pr))
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s/%s.tar.gz .\n'%(self.para.gp_dir,pr))
                frun.write('tar -zxf %s.tar.gz\n'%pr)
                frun.write('cd process/\n')
                frun.write('./run.sh %i %i\n'%(self.events,uid))
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events.lhe.gz %s/%s/events_%s_%s_%i.lhe.gz\n'%(self.para.lhe_dir,pr,self.batch, self.user,uid))
                frun.write('cd ..\n')
                frun.write('rm -rf job%i_%s\n'%(uid,pr))

                cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -o %s -cwd %s %s" %(self.queue,logdir+'/job%s/'%(str(uid)),logdir+'/job%s/'%(str(uid)),logdir+'/'+frunname)
                print cmdBatch
                
                batchid=-1
                job,batchid=ut.SubmitToLsf(cmdBatch,10)
                nbjobsSub+=job    
        print 'succesfully sent %i  jobs'%nbjobsSub
  
    

