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

#__________________________________________________________
    def send(self):
        Dir = os.getcwd()
        nbjobsSub=0

        gplist=self.para.gridpacklist
        lhedir=self.para.lhe_dir
        gpdir=self.para.gp_dir

        gptotest='%s/%s.tar.gz'%(gpdir,self.process)
        if ut.file_exist(gptotest)==False:
            print 'Gridpack=======',gptotest,'======= does not exist'
            sys.exit(3)


        processFound=False
        for pr in gplist:
            if self.process in pr: 
                processFound=True

        if not processFound:
            print 'process ',self.process,' not found, exit'
            sys.exit(3)

        logdir=Dir+"/BatchOutputs/%s"%(pr)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)

        for i in xrange(self.njobs):
            uid = int(ut.getuid(self.user))
            uid = ut.getuid2(self.user)

            print 'uid  ',uid, '    ',type(uid)
            if ut.file_exist('%s/%s/events_%s_%s.lhe.gz'%(lhedir,pr, self.user,uid)):
                print 'already exist, continue'
                continue

            frunname = 'job%s.sh'%(uid) 
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
            frun.write('mkdir job%s_%s\n'%(uid,pr))
            frun.write('cd job%s_%s\n'%(uid,pr))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source %s\n'%(self.para.stack))
            frun.write('mkdir %s\n'%(lhedir))
            frun.write('mkdir %s%s\n'%(lhedir,pr))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s/%s.tar.gz .\n'%(gpdir,self.process))
            frun.write('tar -zxf %s.tar.gz\n'%pr)
            frun.write('cd process/\n')
            frun.write('./run.sh %i %i\n'%(self.events,int(uid)))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events.lhe.gz %s/%s/events_%s_%s.lhe.gz\n'%(lhedir,pr, self.user,uid))
            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(uid,pr))

            cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -o %s -cwd %s %s" %(self.queue,logdir+'/job%s/'%(uid),logdir+'/job%s/'%(uid),logdir+'/'+frunname)
            print cmdBatch
                
            batchid=-1
            job,batchid=ut.SubmitToLsf(cmdBatch,10)
            nbjobsSub+=job    
        print 'succesfully sent %i  jobs'%nbjobsSub
  
    

