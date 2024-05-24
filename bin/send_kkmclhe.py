#!/usr/bin/env python3
import os, sys
import subprocess
import time
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_kkmc():

#__________________________________________________________
    def __init__(self,njobs,events, process, islsf, iscondor, islocal, queue, priority, ncpus, para, version):
        self.njobs    = njobs
        self.events   = events
        self.process  = process
        self.islsf    = islsf
        self.iscondor = iscondor
        self.islocal  = islocal
        self.queue    = queue
        self.priority = priority
        self.ncpus    = ncpus
        self.user     = os.environ['USER']
        self.para     = para
        self.version  = version

#__________________________________________________________
    def send(self):
        Dir = os.getcwd()
        nbjobsSub=0

        print("njobs=",self.njobs)

        lhedir=self.para.lhe_dir
        print("lhedir =",lhedir)
        gpdir=self.para.gp_dir

        acctype='FCC'
        if 'HELHC' in self.para.module_name:  acctype='HELHC'
        elif 'FCCee' in self.para.module_name:  acctype='FCCee'

        logdir=Dir+"/BatchOutputs/%s/lhe/%s"%(acctype,self.process)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)


        if not self.islocal:
             yamldir = '%s/lhe/%s'%(self.para.yamldir,self.process)
             if not ut.dir_exist(yamldir):
                 os.system("mkdir -p %s"%yamldir)

        kkmccard = '%s%s.input'%(self.para.kkmccards_dir, self.process)
        kkmccard = kkmccard.replace('_VERSION_',self.version)

        if ut.file_exist(kkmccard)==False:
            print ('KKMC card does not exist: ',kkmccard,' , exit')
            if '_EvtGen_' not in self.process:
                sys.exit(3)


        if self.islsf==False and self.iscondor==False and self.islocal==False:
            print ("Submit issue : LSF nor CONDOR nor Local flag defined !!!")
            sys.exit(3)

        condor_file_str=''
        while nbjobsSub<self.njobs:
            uid = int(ut.getuid2())

            if not self.islocal:
                myyaml = my.makeyaml(yamldir, uid)
                if not myyaml: 
                    print ('job %s already exists'%uid)
                    continue

                outfile='%s/%s/events_%s.lhe.gz'%(lhedir,self.process,uid)
                if ut.file_exist('%s/%s/events_%s.lhe.gz'%(lhedir,self.process,uid)):
                    print ('already exist, continue')
                    continue

            if self.islocal:
                outfile = '%s/events_%s.lhe.gz'%(logdir,uid)
                if ut.file_exist(outfile):
                    print ('file %s already locally exist, continue'%outfile)
                    continue


            frunname = 'job%s.sh'%(uid) 
            frunfull = '%s/%s'%(logdir,frunname)

            frun = None
            try:
                frun = open(frunfull, 'w')
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                time.sleep(10)
                frun = open(frunfull, 'w')
                
            numberOfEvents = '%10.i'%(self.events)
            #seed_truncated = uid % 10000000000

            #seed_truncated = uid & 0x7FFFFFFF   #  seed should be < 2^31
            #theSeed  = '%10.i'%seed_truncated
            theSeed  = '%10.i'%uid

            subprocess.getstatusoutput('chmod 777 %s'%frunfull)
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('mkdir job%s_%s\n'%(uid,self.process))
            frun.write('cd job%s_%s\n'%(uid,self.process))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source %s\n'%(self.para.defaultstack))
            #frun.write('source /cvmfs/sft.cern.ch/lcg/views/LCG_97a_FCC_4/x86_64-centos7-gcc8-opt/setup.sh \n')
            if self.islocal==False:
                frun.write('mkdir %s%s\n'%(lhedir,self.process))

            frun.write('cp -r /afs/cern.ch/user/e/eperez/FCC/FCCSW/KKMC/KKMCee-4.32.01/dizet-6.45 dizet \n')
            frun.write('cp /afs/cern.ch/user/e/eperez/FCC/FCCSW/KKMC/KKMCee-4.32.01/.KK2f_defaults ./. \n')
            frun.write('mkdir ffbench \n')
            frun.write('cd ffbench \n')
            frun.write('cp /afs/cern.ch/user/e/eperez/FCC/FCCSW/KKMC/KKMCee-4.32.01/ffbench/ProdMC.exe ./. \n')
            frun.write('mkdir run \n')
            frun.write('cd run \n')
            
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %s pro.input\n'%(kkmccard))
            frun.write('cp /afs/cern.ch/user/e/eperez/FCC/FCCSW/KKMC/KKMCee-4.32.01/my_iniseed  ./iniseed \n')
            frun.write('cp /afs/cern.ch/user/e/eperez/FCC/FCCSW/KKMC/KKMCee-4.32.01/ffbench/semaphore.start ./semaphore \n')

            #frun.write('cd process/\n')
            #frun.write('./run.sh %i %i\n'%(self.events,int(uid.lstrip('0'))))
            
            #frun.write('sed -i -e "s/DUMMYSEED/${SEED}/g" pro.input \n')
            frun.write('sed -i -e "s/N_EVENTS/%s/g" pro.input \n'%numberOfEvents)
            frun.write('sed -i -e "s/1111111111/%s/g" iniseed \n'%theSeed)
            #frun.write('echo "seed = %s"  >> header.sin \n'%(uid))

            #frun.write('echo "n_events = %i" > header.sin \n'%(self.events))
            #frun.write('echo "seed = %s"  >> header.sin \n'%(uid))

            frun.write('../ProdMC.exe \n')
            frun.write('echo "finished run"\n') 
            frun.write('gzip LHE_OUT.LHE \n')
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py LHE_OUT.LHE.gz %s\n'%(outfile))
            frun.write('echo "lhe.gz file successfully copied on eos"\n')
            frun.write('cp pro.output %s/pro.output_%s \n'%(logdir,str(uid)))
            frun.write('cd ../../..\n')
            frun.write('rm -rf ffbench \n')
            frun.write('rm -rf dizet \n')


            #frun.write('rm -rf job%s_%s\n'%(uid,self.process))
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

            elif self.islocal==True:
                print ('will run locally')
                nbjobsSub+=1
                os.system('%s'%frunfull)

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
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                time.sleep(10)
                frun_condor = open(frunfull_condor, 'w')
            subprocess.getstatusoutput('chmod 777 %s'%frunfull_condor)
            #
            frun_condor.write('executable     = $(filename)\n')
            frun_condor.write('Log            = %s/condor_job.%s.$(ClusterId).$(ProcId).log\n'%(logdir,str(uid)))
            frun_condor.write('Output         = %s/condor_job.%s.$(ClusterId).$(ProcId).out\n'%(logdir,str(uid)))
            frun_condor.write('Error          = %s/condor_job.%s.$(ClusterId).$(ProcId).error\n'%(logdir,str(uid)))
            frun_condor.write('getenv         = True\n')
            frun_condor.write('environment    = "LS_SUBCWD=%s"\n'%logdir) # not sure
            #frun_condor.write('requirements   = ( (OpSysAndVer =?= "CentOS7") && (Machine =!= LastRemoteHost) )\n')
            #frun_condor.write('requirements   = ( (OpSysAndVer =?= "SLCern6") && (Machine =!= LastRemoteHost) )\n')
            frun_condor.write('requirements    = ( (OpSysAndVer =?= "AlmaLinux9") && (Machine =!= LastRemoteHost) && (TARGET.has_avx2 =?= True) )\n')

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
            print (cmdBatch)
            job=ut.SubmitToCondor(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
            nbjobsSub+=job    
    
        print ('succesfully sent %i  job(s)'%nbjobsSub)

