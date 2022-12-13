#!/usr/bin/env python3
import os, sys
import subprocess
import time
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_stdhep():

#__________________________________________________________
    def __init__(self,njobs,events, process, islsf, iscondor, islocal, queue, priority, ncpus, para, version, typestdhep, training):
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
        self.typestdhep  = typestdhep
        self.training = training

#__________________________________________________________
    def send(self):
        Dir = os.getcwd()
        nbjobsSub=0

        print("njobs=",self.njobs)

        stdhepdir=self.para.stdhep_dir
        # From winter2023 onwards, the stdhep files are store in stdehp/prodTag or stdhep/prodTag/training
        if not( 'spring2021' in self.version or 'pre_fall2022' in self.version or 'dev' in self.version ):
            prodtag = self.version.replace("_training","")
            stdhepdir=stdhepdir+"/%s/"%(prodtag)
        if self.typestdhep == 'wzp6' and self.training:
            stdhepdir = stdhepdir + "training/"
        print("stdhepdir =",stdhepdir)
        gpdir=self.para.gp_dir

        acctype='FCC'
        if 'HELHC' in self.para.module_name:  acctype='HELHC'
        elif 'FCCee' in self.para.module_name:  acctype='FCCee'

        logdir=Dir+"/BatchOutputs/%s/stdhep/%s"%(acctype,self.process)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)


        if not self.islocal:
             yamldir = '%s/stdhep/%s'%(self.para.yamldir,self.process)    # for pre-winter2023 tags
             if self.training:
                  yamldir = '%s/stdhep/training/%s'%(self.para.yamldir,self.process)
             if not( 'spring2021' in self.version or 'pre_fall2022' in self.version or 'dev' in self.version ):   # winter2023 and later:
                  prodtag = self.version.replace("_training","")
                  yamldir = '%s/stdhep/%s/%s'%(self.para.yamldir,prodtag,self.process)
                  if self.training:
                      yamldir = '%s/stdhep/%s/training/%s'%(self.para.yamldir,prodtag,self.process)
             print("yamldir = ",yamldir)
             if not ut.dir_exist(yamldir):
                 os.system("mkdir -p %s"%yamldir)

        if self.typestdhep == 'wzp6':
            whizardcard='%s%s.sin'%(self.para.whizardcards_dir, 'v3.0.3/'+self.process)     # Whizard 2.8.5, with Pythia6 interface
            if 'spring2021' in self.version or 'pre_fall2022' in self.version or 'dev' in self.version:
                whizardcard='%s%s.sin'%(self.para.whizardcards_dir, 'v2.8.5/'+self.process)     # Whizard 2.8.5, with Pythia6 interface
	  

        whizardcard=whizardcard.replace('_VERSION_',self.version)
        if ut.file_exist(whizardcard)==False:
            print ('Whizard card does not exist: ',whizardcard,' , exit')
            if '_EvtGen_' not in self.process:
                sys.exit(3)


        if self.islsf==False and self.iscondor==False and self.islocal==False:
            print ("Submit issue : LSF nor CONDOR nor Local flag defined !!!")
            sys.exit(3)

        condor_file_str=''
        while nbjobsSub<self.njobs:
            #uid = int(ut.getuid(self.user))
            if self.typestdhep == 'wzp6':
                uid = ut.getuid2(self.user)
                if self.training: 
                      #print("---- INFO: using getuidtraining")
                      uid = ut.getuidtraining(self.user)

            if not self.islocal:
                myyaml = my.makeyaml(yamldir, uid)
                if not myyaml: 
                    print ('job %s already exists'%uid)
                    continue

                outfile='%s/%s/events_%s.stdhep.gz'%(stdhepdir,self.process,uid)
                if ut.file_exist('%s/%s/events_%s.stdhep.gz'%(stdhepdir,self.process,uid)):
                    print ('already exist, continue')
                    continue

            if self.islocal:
                outfile = '%s/events_%s.stdhep.gz'%(logdir,uid)
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
                
            subprocess.getstatusoutput('chmod 777 %s'%frunfull)
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('mkdir job%s_%s\n'%(uid,self.process))
            frun.write('cd job%s_%s\n'%(uid,self.process))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source %s\n'%(self.para.defaultstack))
            #frun.write('mkdir %s\n'%(stdhepdir))
            if self.islocal==False:
                frun.write('mkdir -p %s%s\n'%(stdhepdir,self.process))
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %s thecard.sin\n'%(whizardcard))
            #frun.write('cd process/\n')
            #frun.write('./run.sh %i %i\n'%(self.events,int(uid.lstrip('0'))))
            
            frun.write('echo "n_events = %i" > header.sin \n'%(self.events))
            frun.write('echo "seed = %s"  >> header.sin \n'%(uid))
            frun.write('cat header.sin thecard.sin > card.sin \n') 

            frun.write('whizard card.sin \n')
            frun.write('echo "finished run"\n')
            frun.write('gzip proc.stdhep \n')
            #frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py events.lhe.gz %s/%s/events_%s.lhe.gz\n'%(lhedir,self.process ,uid))
            #frun.write('xrdcp -N -v proc.stdhep.gz root://eospublic.cern.ch/%s/%s/events_%s.lhe.gz\n'%(stdhepdir,self.process ,uid))
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py proc.stdhep.gz %s\n'%(outfile))
            frun.write('echo "stdhep.gz file successfully copied on eos"\n')

            frun.write('cd ..\n')
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
            frunname_condor = 'job_desc_stdhep.cfg'
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
            frun_condor.write('requirements    = ( (OpSysAndVer =?= "CentOS7") && (Machine =!= LastRemoteHost) && (TARGET.has_avx2 =?= True) )\n')

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

