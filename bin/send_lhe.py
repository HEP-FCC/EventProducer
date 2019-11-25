#!/usr/bin/env python
import os, sys
import commands
import time
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_lhe():

#__________________________________________________________
    def __init__(self,njobs,events, process, islsf, iscondor, queue, priority, ncpus, para, typelhe):
        self.njobs    = njobs
        self.events   = events
        self.process  = process
        self.islsf    = islsf
        self.iscondor = iscondor
        self.queue    = queue
        self.priority = priority
        self.ncpus    = ncpus
        self.user     = os.environ['USER']
        self.para     = para
        self.typelhe  = typelhe

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

        try:
            gplist[self.process]
        except KeyError, e:
            print 'process %s does not exist as gridpack, exit'%self.process
            sys.exit(3)

        acctype='FCC'
        if 'HELHC' in self.para.module_name:  acctype='HELHC'
        elif 'FCCee' in self.para.module_name:  acctype='FCCee'

        logdir=Dir+"/BatchOutputs/%s/lhe/%s"%(acctype,self.process)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)


        yamldir = '%s/lhe/%s'%(self.para.yamldir,self.process)
        if not ut.dir_exist(yamldir):
            os.system("mkdir -p %s"%yamldir)


        if self.islsf==False and self.iscondor==False:
            print "Submit issue : LSF nor CONDOR flag defined !!!"
            sys.exit(3)

        condor_file_str=''
        while nbjobsSub<self.njobs:
            #uid = int(ut.getuid(self.user))
            if self.typelhe == 'gp_mg':
                uid = ut.getuid2(self.user)
            elif self.typelhe == 'gp_pw':
                uid = ut.getuid3(self.user)

            myyaml = my.makeyaml(yamldir, uid)
            if not myyaml: 
                print 'job %s already exists'%uid
                continue

            if ut.file_exist('%s/%s/events_%s.lhe.gz'%(lhedir,self.process,uid)):
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
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('mkdir job%s_%s\n'%(uid,self.process))
            frun.write('cd job%s_%s\n'%(uid,self.process))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source %s\n'%(self.para.stack))
            frun.write('mkdir %s\n'%(lhedir))
            frun.write('mkdir %s%s\n'%(lhedir,self.process))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s/%s.tar.gz .\n'%(gpdir,self.process))
            frun.write('tar -zxf %s.tar.gz\n'%self.process)
            frun.write('cd process/\n')
            frun.write('./run.sh %i %i\n'%(self.events,int(uid.lstrip('0'))))
            #frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events.lhe.gz %s/%s/events_%s.lhe.gz\n'%(lhedir,self.process ,uid))
            frun.write('xrdcp -N -v events.lhe.gz root://eospublic.cern.ch/%s/%s/events_%s.lhe.gz\n'%(lhedir,self.process ,uid))

            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(uid,self.process))
            frun.close()

            if self.islsf==True :
              cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -o %s -cwd %s %s" %(self.queue,logdir+'/job%s/'%(uid),logdir+'/job%s/'%(uid),logdir+'/'+frunname)
              #print cmdBatch

              batchid=-1
              job,batchid=ut.SubmitToLsf(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
              nbjobsSub+=job
            elif self.iscondor==True :
              condor_file_str+=frunfull+" "
              nbjobsSub+=1

        if self.iscondor==True :
            # clean string
            condor_file_str=condor_file_str.replace("//","/")
            #
            frunname_condor = 'job_desc_lhe.cfg'
            frunfull_condor = '%s/%s'%(logdir,frunname_condor)
            frun_condor = None
            try:
                frun_condor = open(frunfull_condor, 'w')
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(10)
                frun_condor = open(frunfull_condor, 'w')
            commands.getstatusoutput('chmod 777 %s'%frunfull_condor)
            #
            frun_condor.write('executable     = $(filename)\n')
            frun_condor.write('Log            = %s/condor_job.%s.$(ClusterId).$(ProcId).log\n'%(logdir,str(uid)))
            frun_condor.write('Output         = %s/condor_job.%s.$(ClusterId).$(ProcId).out\n'%(logdir,str(uid)))
            frun_condor.write('Error          = %s/condor_job.%s.$(ClusterId).$(ProcId).error\n'%(logdir,str(uid)))
            frun_condor.write('getenv         = True\n')
            frun_condor.write('environment    = "LS_SUBCWD=%s"\n'%logdir) # not sure
            frun_condor.write('requirements   = ( (OpSysAndVer =?= "CentOS7") && (Machine =!= LastRemoteHost) )\n')
            #frun_condor.write('requirements   = ( (OpSysAndVer =?= "SLCern6") && (Machine =!= LastRemoteHost) )\n')
            frun_condor.write('on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n')
            frun_condor.write('max_retries    = 3\n')
            frun_condor.write('+JobFlavour    = "%s"\n'%self.queue)
            frun_condor.write('+AccountingGroup = "%s"\n'%self.priority)
            frun_condor.write('RequestCpus = %s\n'%self.ncpus)

            frun_condor.write('queue filename matching files %s\n'%condor_file_str)
            frun_condor.close()
            #
            nbjobsSub=0
            cmdBatch="condor_submit %s"%frunfull_condor
            print cmdBatch
            job=ut.SubmitToCondor(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
            nbjobsSub+=job    
    
        print 'succesfully sent %i  job(s)'%nbjobsSub

