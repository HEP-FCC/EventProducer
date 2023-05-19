#!/usr/bin/env python3
import os, sys
import subprocess
import time
import json
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my


class send_p8():

#__________________________________________________________
    def __init__(self,njobs, events, process, islsf, iscondor, islocal, queue, priority, ncpus, para, version, training, detector):
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
        self.training = training
        self.detector = detector

#__________________________________________________________
    def send(self):

        Dir = os.getcwd()
        nbjobsSub=0

        p8list=self.para.pythialist
        outdir='%s%s/%s/'%(self.para.delphes_dir,self.version,self.detector)
        try:
            p8list[self.process]
        except KeyError as e:
            print ('process %s does not exist, exit'%self.process)
            sys.exit(3)

        acctype='FCC'
        if 'FCCee' in self.para.module_name:  acctype='FCCee'

        logdir=Dir+"/BatchOutputs/%s/%s/%s/%s/"%(acctype,self.version,self.detector,self.process)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)

        if not self.islocal:
            yamldir = '%s/%s/%s/%s'%(self.para.yamldir,self.version,self.detector,self.process)
            if not ut.dir_exist(yamldir):
                os.system("mkdir -p %s"%yamldir)

        delphescards_base = '%scard_%s.tcl'%(self.para.delphescards_dir,self.detector)
        delphescards_base=delphescards_base.replace('_VERSION_',self.version)
        if ut.file_exist(delphescards_base)==False:
            print ('delphes card does not exist: ',delphescards_base,' , exit')
            sys.exit(3)

        pythiacard='%s%s.cmd'%(self.para.pythiacards_dir,self.process)
        pythiacard=pythiacard.replace('_VERSION_',self.version)
        if ut.file_exist(pythiacard)==False:
            if '_EvtGen' not in self.process:
                print ('pythia card does not exist: ',pythiacard,' exit')
                
                sys.exit(3)


 
        if self.islsf==False and self.iscondor==False and self.islocal==False:
            print ("Submit issue : LSF nor CONDOR not Local flag defined !!!")
            sys.exit(3)

        condor_file_str=''
        while nbjobsSub<self.njobs:

            uid = ut.getuid2()
            if self.training: uid = ut.getuidtraining()
            if not self.islocal:
                myyaml = my.makeyaml(yamldir, uid)
                if not myyaml: 
                    print ('job %s already exists'%uid)
                    continue
                outfile='%s/%s/events_%s.root'%(outdir,self.process,uid)
                if ut.file_exist(outfile):
                    print ('file %s already exist on eos, continue'%outfile)
                    continue

            if  self.islocal:
                outfile='%s/events_%s.root'%(logdir,uid)
                if ut.file_exist(outfile):
                    print ('file %s already locally exist, continue'%outfile)
                    continue


            frunname = 'job%s.sh'%(uid)
            frunfull = '%s/%s'%(logdir,frunname)
            print ('frunname  ',frunname)
            print ('frunfull  ',frunfull)
            frun = None
            try:
                frun = open(frunfull, 'w')
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                time.sleep(10)
                frun = open(frunfull, 'w')

            subprocess.getstatusoutput('chmod 777 %s'%(frunfull))
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('source %s\n'%(self.para.prodTag[self.version]))
            #frun.write('source /cvmfs/sw.hsf.org/contrib/spack/share/spack/setup-env.sh\n')
            #frun.write('spack load --first k4simdelphes build_type=Release ^evtgen+photos\n')

            proc_trunc = self.process[:37] + ( self.process[37:] and 'More')            
            frun.write('mkdir job%s_%s\n'%(uid,proc_trunc))
            frun.write('cd job%s_%s\n'%(uid,proc_trunc))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            if self.islocal==False:
                frun.write('mkdir -p %s/%s\n'%(outdir,self.process))
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %s card.tcl\n'%(delphescards_base))

            if '_EvtGen' not in self.process:
                frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %s card.cmd\n'%(pythiacard))
                frun.write('echo "" >> card.cmd\n')
                frun.write('echo "Random:seed = %s" >> card.cmd\n'%uid)
                frun.write('echo "Main:numberOfEvents = %i" >> card.cmd\n'%(self.events))


            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py /eos/experiment/fcc/ee/generation/FCC-config/%s/FCCee/Delphes/edm4hep_%s.tcl edm4hep.tcl\n'%(self.version,self.detector))
            
            if '_EvtGen' not in self.process:
                frun.write('DelphesPythia8_EDM4HEP card.tcl edm4hep.tcl card.cmd events_%s.root\n'%(uid)) 
            else:
                evtgendir=self.para.evtgencards_dir.replace('_VERSION_',self.version)
                frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %sDECAY.DEC .\n'%(evtgendir))
                frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %sevt.pdl .\n'%(evtgendir))
                decfile='%s%s.dec'%(evtgendir,self.process.split('_')[-1])
                if ut.file_exist(decfile)==False and self.process.split('_')[-1]!='EvtGen':
                    print ('evtgen user dec file does not exist: ',decfile,' , exit')
                    sys.exit(3)

                if self.process.split('_')[-1]!='EvtGen':
                    frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py %s user.dec\n'%(decfile))
                    
                if 'Zbb' in self.process:
                    frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py /eos/experiment/fcc/ee/generation/FCC-config/%s/FCCee/Generator/Pythia8/p8_ee_Zbb_ecm91_EVTGEN.cmd card.cmd\n'%(self.version))
                    
                elif 'Zcc' in self.process:
                    frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py /eos/experiment/fcc/ee/generation/FCC-config/%s/FCCee/Generator/Pythia8/p8_ee_Zcc_ecm91_EVTGEN.cmd card.cmd\n'%(self.version))
                    frun.write('export PATH=/afs/cern.ch/work/f/fccsw/public/FCCutils/k4SimDelphes-00-01-06/install/bin:${PATH}\n')
                    frun.write('export LD_LIBRARY_PATH=/afs/cern.ch/work/f/fccsw/public/FCCutils/k4SimDelphes-00-01-06/install//lib64:${LD_LIBRARY_PATH}\n')
                    frun.write('Run a hacked version of k4SimDelphes-00-01-06 adding c-mesons to the list\n')
                    frun.write('echo \"==================================================================\"\n')
                    frun.write('echo \"==================================================================\"\n')
                    frun.write('echo \"==================================================================\"\n')
                    frun.write('which DelphesPythia8EvtGen_EDM4HEP_k4Interface\n')
                    frun.write('echo \"==================================================================\"\n')
                    frun.write('echo \"==================================================================\"\n')
                    frun.write('echo \"==================================================================\"\n')                    
                    
                else:
                    print ('can not run evt gen with other events than Z->bb or Z->cc exit')
                    sys.exit(3)

                frun.write('echo "Main:numberOfEvents = %i" >> card.cmd\n'%(self.events))
                frun.write('echo "Random:seed = %s" >> card.cmd\n'%uid)

                tmppr=self.process.split('_')[-1]
                tmppr=tmppr[0:3]
                
                pdgid=-9999
                bsignal=''
                if 'Bu2' == tmppr: 
                    pdgid=521
                    bsignal='Bu_SIGNAL'
                elif 'Bd2' == tmppr: 
                    pdgid=511
                    bsignal='Bd_SIGNAL'
                elif 'Bc2' == tmppr: 
                    pdgid=541
                    bsignal='Bc_SIGNAL'
                elif 'Bs2' == tmppr: 
                    pdgid=531
                    bsignal='Bs_SIGNAL'
                elif 'Lb2' == tmppr: 
                    pdgid=5122
                    bsignal='Lb_SIGNAL'

                elif 'Dd2' == tmppr:
                    pdgid=411
                    bsignal='Dd_SIGNAL'
                elif 'Ds2' == tmppr:
                    pdgid=431
                    bsignal='Ds_SIGNAL'                   
                elif 'Lc2' == tmppr:
                    pdgid=4122
                    bsignal='Lc_SIGNAL'
                    
                else:
                    if tmppr!="EvtGen":
                        print('pdg id not found, exit')
                        sys.exit(3)
                if tmppr!="EvtGen":
                    frun.write('DelphesPythia8EvtGen_EDM4HEP_k4Interface card.tcl edm4hep.tcl card.cmd events_%s.root DECAY.DEC evt.pdl user.dec %s %s 1\n'%(uid,pdgid,bsignal))
                elif tmppr=="EvtGen":
                    frun.write('DelphesPythia8EvtGen_EDM4HEP_k4Interface card.tcl edm4hep.tcl card.cmd events_%s.root DECAY.DEC evt.pdl\n'%(uid))

            #frun.write('xrdcp -N -v events_%s.root root://eospublic.cern.ch/%s\n'%(uid,outfile))
            #if ut.file_exist(outfile)==False:
            #    frun.write('cp events_%s.root %s\n'%(uid,outfile))
            #if ut.file_exist(outfile)==False:
            frun.write('python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py events_%s.root %s\n'%(uid,outfile))
            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(uid,proc_trunc))
            frun.close()

            if self.islsf==True :
              cmdBatch="bsub -M 2000000 -R \"pool=20000\" -q %s -o %s -cwd %s %s" %(self.queue, logdir+'/job%s/'%(uid),logdir+'/job%s/'%(uid),frunfull)
              job,batchid=ut.SubmitToLsf(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))

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
            frunname_condor = 'job_desc_p8_%s.cfg'%(self.process)
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

