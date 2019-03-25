#python bin/sendJobs_FCCSW.py -n 10 -p pp_h012j_5f -q 8nh -e -1 -d haa --test
#python bin/sendJobs_FCCSW.py secret -n 1 -e -1  -p "pp_h012j_5f" -q 1nh --test
#python bin/sendJobs_FCCSW.py -n 1 -p pp_h012j_5f -q 8nh -e -1 -v fcc_v02
#python bin/run.py --FCC --reco --send --condor -p mg_pp_tttt_5f --type lhep8 -N 20 -q tomorrow --version fcc_v02

import os, sys
import commands
import time
import yaml
import glob
from select import select
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_lhep8():

#__________________________________________________________
    def __init__(self,njobs, events, process, islsf, iscondor, queue, para, version, decay):
        self.njobs    = njobs
        self.events   = -1
        self.process  = process
        self.islsf    = islsf
        self.iscondor = iscondor
        self.queue    = queue
        self.para     = para
        self.version  = version
        self.decay    = decay
        self.user     = os.environ['USER']


#__________________________________________________________
    def send(self, force):

        Dir = os.getcwd()
    
        gplist=self.para.gridpacklist
        outdir='%s%s/'%(self.para.delphes_dir,self.version)
        try:
            gplist[self.process]
        except KeyError, e:
            print 'process %s does not exist as gridpack'%self.process
            sys.exit(3)

        delphescards_mmr = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_mmr)
        if ut.file_exist(delphescards_mmr)==False and self.version != 'cms' and 'helhc' not in self.version:
            print 'delphes card does not exist: ',delphescards_mmr
            sys.exit(3)

        delphescards_mr = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_mr)
        if ut.file_exist(delphescards_mr)==False and self.version != 'cms' and 'helhc' not in self.version:
            print 'delphes card does not exist: ',delphescards_mr
            sys.exit(3)

        delphescards_base = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_base)
        if ut.file_exist(delphescards_base)==False:
            print 'delphes card does not exist: ',delphescards_base
            sys.exit(3)

        fccconfig = '%s%s'%(self.para.fccconfig_dir,self.para.fccconfig)
        if ut.file_exist(fccconfig)==False:
            print 'fcc config file does not exist: ',fccconfig
            sys.exit(3)


        print '======================================',self.process
        pythiacard='%s%s.cmd'%(self.para.pythiacards_dir,self.process.replace('mg_pp','p8_pp').replace('mg_gg','p8_gg'))
        if self.decay!='':
            pythiacard='%s%s_%s.cmd'%(self.para.pythiacards_dir,self.process.replace('mg_pp','p8_pp').replace('mg_gg','p8_gg'),self.decay)
            
        if ut.file_exist(pythiacard)==False and not force:
            print 'pythia card does not exist: ',pythiacard
            timeout = 60
            print "do you want to use the default pythia card [y/n] (60sec to reply)"
            rlist, _, _ = select([sys.stdin], [], [], timeout)
            if rlist:
                s = sys.stdin.readline()
                if s=="y\n":
                    print 'use default card'
                    pythiacard='%sp8_pp_default.cmd'%(self.para.pythiacards_dir)
                else:
                    print 'exit'
                    sys.exit(3)
            else:
                print "timeout, use default card"
                pythiacard='%sp8_pp_default.cmd'%(self.para.pythiacards_dir)
        elif ut.file_exist(pythiacard)==False and force:
            print "force argument, use default card"
            pythiacard='%sp8_pp_default.cmd'%(self.para.pythiacards_dir)

        pr_noht=''
        if '_HT_' in self.process:
            ssplit=self.process.split('_')
            stest=''
            for s in xrange(0,len(ssplit)-3):
                stest+=ssplit[s]+'_'
            pr_noht= stest[0:len(stest)-1]

        #check that the specified decay exists
        if self.process in self.para.decaylist and self.decay != '' and '_HT_' not in self.process:
            if self.decay not in self.para.decaylist[self.process]:
                print 'decay ==%s== does not exist for process ==%s=='%(self.decay,self.process)
                sys.exit(3)

        #check that the specified decay exists
        if pr_noht in self.para.decaylist and self.decay != '' and '_HT_' in self.process:
            if self.decay not in self.para.decaylist[pr_noht]:
                print 'decay ==%s== does not exist for process ==%s=='%(self.decay,self.process)
                sys.exit(3)
        pr_decay=self.process
        if self.decay!='':
            pr_decay=self.process+'_'+self.decay
        print '====',pr_decay,'===='

        processp8 = pr_decay.replace('mg_pp','mgp8_pp').replace('mg_gg','mgp8_gg')

        acctype='FCC'
        if 'HELHC' in self.para.module_name:  acctype='HELHC'

        logdir=Dir+"/BatchOutputs/%s/%s/%s/"%(acctype,self.version,processp8)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)
     
        yamldir = '%s/%s/%s'%(self.para.yamldir,self.version,processp8)
        if not ut.dir_exist(yamldir):
            os.system("mkdir -p %s"%yamldir)

        yamllhedir = '%s/lhe/%s'%(self.para.yamldir,self.process)
  
        All_files = glob.glob("%s/events_*.yaml"%yamllhedir)
        if len(All_files)==0:
            print 'there is no LHE files checked for process %s exit'%self.process
            sys.exit(3)

        if len(All_files)<self.njobs:
            print 'only %i LHE file exists, will not run all the jobs requested'%len(All_files)

        nbjobsSub=0
        ntmp=0

        if self.islsf==False and self.iscondor==False:
            print "Submit issue : LSF nor CONDOR flag defined !!!"
            sys.exit(3)

        condor_file_str=''
        for i in xrange(len(All_files)):

            if nbjobsSub == self.njobs: break

            tmpf=None
            with open(All_files[i], 'r') as stream:
                try:
                    tmpf = yaml.load(stream)
                    if ut.getsize(All_files[i])==0:continue
                    if tmpf['processing']['status']!='DONE': continue
                    
                except yaml.YAMLError as exc:
                    print(exc)

            jobid=tmpf['processing']['jobid']

            myyaml = my.makeyaml(yamldir, jobid)
            if not myyaml: 
                print 'job %s already exists'%jobid
                continue

            outfile='%s/%s/events_%s.root'%(outdir,processp8,jobid)
            if ut.file_exist(outfile):
                print 'outfile already exist, continue  ',outfile

            frunname = 'job%s.sh'%(jobid)
            frunfull = '%s/%s'%(logdir,frunname)

            frun = None
            try:
                frun = open(frunfull, 'w')
            except IOError as e:
                print "I/O error({0}): {1}".format(e.errno, e.strerror)
                time.sleep(10)
                frun = open(frunfull, 'w')



            commands.getstatusoutput('chmod 777 %s'%(frunfull))
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('source %s\n'%(self.para.stack))
            frun.write('mkdir job%s_%s\n'%(jobid,processp8))
            frun.write('cd job%s_%s\n'%(jobid,processp8))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('mkdir -p %s%s/%s\n'%(self.para.delphes_dir,self.version,processp8))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(tmpf['processing']['out']))
            frun.write('gunzip -c %s > events.lhe\n'%tmpf['processing']['out'].split('/')[-1])          
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_base))
            if 'fcc' in self.version:
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mmr))
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mr))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s config.py \n'%(fccconfig))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s card.cmd\n'%(pythiacard))
            frun.write('echo "Beams:LHEF = events.lhe" >> card.cmd\n')
            frun.write('echo "Random:seed = %s" >> card.cmd\n'%jobid)
            if 'helhc' in self.version:
                frun.write('echo " Beams:eCM = 27000." >> card.cmd\n')
            frun.write('%s/run fccrun.py config.py --delphescard=card.tcl --inputfile=card.cmd --outputfile=events_%s.root --nevents=%i\n'%(self.para.fccsw,jobid,self.events))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events_%s.root %s\n'%(jobid,outfile))
            
            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(jobid,processp8))
            frun.close()

            if self.islsf==True :
              cmdBatch="bsub -M 3000000 -R \"pool=40000\" -q %s -o %s -cwd %s %s" %(self.queue, logdir+'/job%s/'%(jobid), logdir+'/job%s/'%(jobid),frunfull)

              batchid=-1
              job,batchid=ut.SubmitToLsf(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
              nbjobsSub+=job
            elif self.iscondor==True :
              condor_file_str+=frunfull+" "
              nbjobsSub+=1

        if self.iscondor==True :
            frunname_condor = 'job_desc.cfg'
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
            frun_condor.write('Log            = condor_job_$(ProcId).log\n')
            frun_condor.write('Output         = condor_job_$(ProcId).out\n')
            frun_condor.write('Error          = condor_job_$(ProcId).error\n')
            frun_condor.write('getenv         = True\n')
            frun_condor.write('environment    = "LS_SUBCWD=%s"\n'%logdir) # not sure
            frun_condor.write('request_memory = 4G\n')
            # tmp
            frun_condor.write('requirements   = ( (OpSysAndVer =?= "SLCern6") && (CERNEnvironment =?= "qa") &&  (Machine =!= LastRemoteHost) )\n')
            # final to use when nodes have the fix
            #frun_condor.write('requirements   = ( (OpSysAndVer =?= "SLCern6") &&  (Machine =!= LastRemoteHost) )\n')
            frun_condor.write('on_exit_remove = (ExitBySignal == False) && (ExitCode == 0)\n')
            frun_condor.write('max_retries    = 3\n')
            frun_condor.write('+JobFlavour    = "%s"\n'%self.queue)
            frun_condor.write('queue filename matching files %s\n'%condor_file_str)
            frun_condor.close()
            #
            nbjobsSub=0
            cmdBatch="condor_submit %s/%s"%(logdir,frunname_condor)
            print cmdBatch
            job=ut.SubmitToCondor(cmdBatch,10,"%i/%i"%(nbjobsSub,self.njobs))
            nbjobsSub+=job

        print 'succesfully sent %i  job(s)'%nbjobsSub
  

