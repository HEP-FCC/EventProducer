#!/usr/bin/env python3
import os, sys
import subprocess
import time
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_sherpa():

#__________________________________________________________
    def __init__(self, njobs, events, process, islsf, iscondor, islocal, queue, priority, ncpus, para, version, training, detector, custom_edm4hep_config):
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
        self.custom_edm4hep_config = custom_edm4hep_config

#__________________________________________________________
    def send(self):

        Dir = os.getcwd()
        nbjobsSub=0

        shlist=self.para.sherpalist
        outdir='%s%s/%s/'%(self.para.delphes_dir,self.version,self.detector)
        try:
            shlist[self.process]
        except KeyError:
            print ('process %s does not exist in sherpalist, exit'%self.process)
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

        # Delphes detector card + edm4hep output config of the campaign
        delphescards_base = '%scard_%s.tcl'%(self.para.delphescards_dir,self.detector)
        delphescards_base = delphescards_base.replace('_VERSION_',self.version)
        if ut.file_exist(delphescards_base)==False:
            print ('delphes card does not exist: ',delphescards_base,' , exit')
            sys.exit(3)

        # Sherpa input card for this process
        sherpacard = '%s%s.yaml'%(self.para.sherpacards_dir,self.process)
        sherpacard = sherpacard.replace('_VERSION_',self.version)
        if ut.file_exist(sherpacard)==False:
            print ('sherpa card does not exist: ',sherpacard,' , exit')
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

            if self.islocal:
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

            proc_trunc = self.process[:37] + ( self.process[37:] and 'More')
            eoscopy = 'python /afs/cern.ch/work/f/fccsw/public/FCCutils/eoscopy.py'

            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH PYTHONHOME PYTHONPATH\n')
            frun.write('mkdir job%s_%s\n'%(uid,proc_trunc))
            frun.write('cd job%s_%s\n'%(uid,proc_trunc))
            frun.write('export EOS_MGM_URL="root://eospublic.cern.ch"\n')
            if self.islocal==False:
                frun.write('mkdir -p %s/%s\n'%(outdir,self.process))

            # single stack for the whole job (the campaign stack ships Sherpa AND k4SimDelphes)
            frun.write('source %s\n'%(self.para.prodTag[self.version]))
            # fail the job on any error so condor retries it (exit code otherwise masked by the final rm)
            frun.write('set -e\n')
            # Sherpa needs an LHAPDF sets dir to initialise even for e+e- (unused by the ee ME)
            frun.write('for d in /cvmfs/sw-nightlies.hsf.org/key4hep/releases/*/x86_64-almalinux9-*-opt/lhapdfsets/*/share/lhapdfsets; do [ -d "$d" ] && export LHAPDF_DATA_PATH="$d" && break; done\n')

            # generation: Sherpa -> events.hepmc (HepMC3 ascii, filename set in the card);
            # the first pass integrates the ME (Results/ grids), then generates -- one call does both
            frun.write('%s %s card.yaml\n'%(eoscopy,sherpacard))
            # seed as plain int (avoid leading-zero uids being parsed as invalid/octal)
            frun.write('Sherpa -f card.yaml -e %i -R %i\n'%(self.events,int(uid)))

            # reco: HepMC3 -> EDM4hep in one step (Sherpa writes HepMC3; the HepMC2
            # reader would silently produce zero events on a HepMC3 file)
            frun.write('%s %s card.tcl\n'%(eoscopy,delphescards_base))
            if self.custom_edm4hep_config:
                frun.write('cp %s edm4hep.tcl\n'%(self.custom_edm4hep_config))
            else:
                frun.write('%s /eos/experiment/fcc/ee/generation/FCC-config/%s/FCCee/Delphes/edm4hep_%s.tcl edm4hep.tcl\n'%(eoscopy,self.version,self.detector))
            frun.write('DelphesHepMC3_EDM4HEP card.tcl edm4hep.tcl events_%s.root events.hepmc\n'%(uid))

            frun.write('%s events_%s.root %s\n'%(eoscopy,uid,outfile))
            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(uid,proc_trunc))
            frun.close()

            if self.islsf==True :
              cmdBatch="bsub -M 2000000 -R \"pool=20000\" -q %s -o %s -cwd %s %s" %(self.queue, logdir+'/job%s/'%(uid),logdir+'/job%s/'%(uid),frunfull)
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
            condor_file_str=condor_file_str.replace("//","/")
            frunname_condor = 'job_desc_sherpa_%s.cfg'%(self.process)
            frunfull_condor = '%s/%s'%(logdir,frunname_condor)
            frun_condor = None
            try:
                frun_condor = open(frunfull_condor, 'w')
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                time.sleep(10)
                frun_condor = open(frunfull_condor, 'w')
            subprocess.getstatusoutput('chmod 777 %s'%frunfull_condor)

            frun_condor.write('executable     = $(filename)\n')
            frun_condor.write('Log            = %s/condor_job.%s.$(ClusterId).log\n'%(logdir,str(uid)))
            frun_condor.write('Output         = %s/condor_job.%s.$(ClusterId).$(ProcId).out\n'%(logdir,str(uid)))
            frun_condor.write('Error          = %s/condor_job.%s.$(ClusterId).$(ProcId).error\n'%(logdir,str(uid)))
            frun_condor.write('getenv         = True\n')
            frun_condor.write('environment    = "LS_SUBCWD=%s"\n'%logdir)
            frun_condor.write('requirements    = ( (OpSysAndVer =?= "AlmaLinux9") && (Machine =!= LastRemoteHost) && (TARGET.has_avx2 =?= True) )\n')
            frun_condor.write('on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n')
            frun_condor.write('max_retries    = 3\n')
            frun_condor.write('+JobFlavour    = "%s"\n'%self.queue)
            frun_condor.write('+AccountingGroup = "%s"\n'%self.priority)
            frun_condor.write('RequestCpus = %s\n'%self.ncpus)
            frun_condor.write('queue filename matching files %s\n'%condor_file_str)
            frun_condor.close()

            nbjobsSub=0
            cmdBatch="condor_submit %s"%frunfull_condor
            print (cmdBatch)
            job=ut.SubmitToCondor(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
            nbjobsSub+=job

        print ('succesfully sent %i  job(s)'%nbjobsSub)
