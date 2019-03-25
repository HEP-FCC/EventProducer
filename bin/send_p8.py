#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000
#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000 
#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000 -v fcc_v02
#python bin/run.py --FCC --reco --send --type p8 --condor -p p8_pp_jj_lo_tagger -n 10000 -N 10 -q workday --version fcc_v02


import os, sys
import commands
import time
import json
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my


class send_p8():

#__________________________________________________________
    def __init__(self,njobs, events, process, islsf, iscondor, queue, para, version):
        self.njobs    = njobs
        self.events   = events
        self.process  = process
        self.islsf    = islsf
        self.iscondor = iscondor
        self.queue    = queue
        self.user     = os.environ['USER']
        self.para     = para
        self.version  = version


#__________________________________________________________
    def send(self):

        Dir = os.getcwd()
        nbjobsSub=0

        p8list=self.para.pythialist
        outdir='%s%s/'%(self.para.delphes_dir,self.version)
        try:
            p8list[self.process]
        except KeyError, e:
            print 'process %s does not exist, exit'%self.process
            sys.exit(3)

        acctype='FCC'
        if 'HELHC' in self.para.module_name:  acctype='HELHC'

        logdir=Dir+"/BatchOutputs/%s/%s/%s/"%(acctype,self.version,self.process)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)

        yamldir = '%s/%s/%s'%(self.para.yamldir,self.version,self.process)
        if not ut.dir_exist(yamldir):
            os.system("mkdir -p %s"%yamldir)


        delphescards_mmr = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_mmr)
        if ut.file_exist(delphescards_mmr)==False and self.version != 'cms' and 'helhc' not in self.version:
            print 'delphes card does not exist: ',delphescards_mmr,' , exit'
            sys.exit(3)

        delphescards_mr = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_mr)
        if ut.file_exist(delphescards_mr)==False and self.version != 'cms' and 'helhc' not in self.version:
            print 'delphes card does not exist: ',delphescards_mr,' , exit'
            sys.exit(3)

        delphescards_base = '%s%s/%s'%(self.para.delphescards_dir,self.version,self.para.delphescard_base)
        if ut.file_exist(delphescards_base)==False:
            print 'delphes card does not exist: ',delphescards_base,' , exit'
            sys.exit(3)

        fccconfig = '%s%s'%(self.para.fccconfig_dir,self.para.fccconfig)
        if ut.file_exist(fccconfig)==False:
            print 'fcc config file does not exist: ',fccconfig,' , exit'
            sys.exit(3)


        print '======================================',self.process
        pythiacard='%s%s.cmd'%(self.para.pythiacards_dir,self.process)
        if ut.file_exist(pythiacard)==False:
            print 'pythia card does not exist: ',pythiacard,' , exit'
            sys.exit(3)

 
        if self.islsf==False and self.iscondor==False:
            print "Submit issue : LSF nor CONDOR flag defined !!!"
            sys.exit(3)

        condor_file_str=''
        while nbjobsSub<self.njobs:

            uid = ut.getuid2(self.user)
            myyaml = my.makeyaml(yamldir, uid)
            if not myyaml: 
                print 'job %s already exists'%uid
                continue
            outfile='%s/%s/events_%s.root'%(outdir,self.process,uid)
            if ut.file_exist(outfile):
                print 'file %s already exist, continue'%outfile
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

            commands.getstatusoutput('chmod 777 %s'%(frunfull))
            frun.write('#!/bin/bash\n')
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('source %s\n'%(self.para.stack))
            frun.write('mkdir job%s_%s\n'%(uid,self.process))
            frun.write('cd job%s_%s\n'%(uid,self.process))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('mkdir -p %s/%s\n'%(outdir,self.process))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_base))
            if 'fcc' in self.version:
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mmr))
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mr))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s config.py \n'%(fccconfig))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s card.cmd\n'%(pythiacard))
            frun.write('echo "" >> card.cmd\n')
            frun.write('echo "Random:seed = %s" >> card.cmd\n'%uid)
            if 'helhc' in self.version:
                frun.write('echo " Beams:eCM = 27000." >> card.cmd\n')
            frun.write('%s/run fccrun.py config.py --delphescard=card.tcl --inputfile=card.cmd --outputfile=events%s.root --nevents=%i\n'%(self.para.fccsw,uid,self.events))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events%s.root %s\n'%(uid,outfile))
            frun.write('cd ..\n')
            frun.write('rm -rf job%s_%s\n'%(uid,self.process))
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

        if self.iscondor==True :
            # clean string
            condor_file_str=condor_file_str.replace("//","/")
            #
            frunname_condor = 'job_desc_p8.cfg'
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
            frun_condor.write('request_memory = 2G\n')
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

