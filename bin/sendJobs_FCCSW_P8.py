#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000
#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000 
#python bin/sendJobs_FCCSW_P8.py -n 1 -p pp_Zprime_5TeV_ll -e 10000 -v fcc_v02


import glob, os, sys,subprocess,cPickle
import commands
import time
import random
import json
import importlib
import ntpath

#import EventProducer.config.param as para
import EventProducer.common.dicwriter_FCC as dicr
import EventProducer.common.isreading as isr

class send_lhe():

#__________________________________________________________
    def __init__(self,njobs, events, process, islsf, queue, para, version):
        self.njobs   = njobs
        self.events  = events
        self.process = process
        self.islsf   = islsf
        self.queue   = queue
        self.user    = os.environ['USER']
        self.para    = para
        self.version = version


#__________________________________________________________
    def send(self):

        Dir = os.getcwd()
        rundir = os.getcwd()
        nbjobsSub=0

  

    version    = options.version
    fakeadd    = options.fakeadd
    rundir = os.getcwd()
    nbjobsSub=0

    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, cms'
        sys.exit(3)

    fcc_dic=para.fcc_dic.replace('VERSION',version)
    readfcc_dic=para.readfcc_dic.replace('VERSION',version)

    outdict=dicr.dicwriter(fcc_dic)
    readdic=isr.isreading(readfcc_dic, fcc_dic)

    delphescards_mmr = '%s%s/%s'%(para.delphescards_dir,version,para.delphescard_mmr)
    if eosexist(delphescards_mmr)==False and version != 'cms':
        print 'delphes card does not exist: ',delphescards_mmr
        sys.exit(3)

    delphescards_mr = '%s%s/%s'%(para.delphescards_dir,version,para.delphescard_mr)
    if eosexist(delphescards_mr)==False and version != 'cms':
        print 'delphes card does not exist: ',delphescards_mr
        sys.exit(3)

    delphescards_base = '%s%s/%s'%(para.delphescards_dir,version,para.delphescard_base)
    if eosexist(delphescards_base)==False:
        print 'delphes card does not exist: ',delphescards_base
        sys.exit(3)

    fccconfig = '%s%s'%(para.fccconfig_dir,para.fccconfig)
    if eosexist(fccconfig)==False:
        print 'fcc config file does not exist: ',fccconfig
        sys.exit(3)

    readdic.backup('sendJobs_FCCSW_P8')
    readdic.reading()

    print '======================================',process
    pythiacard='%spythia_%s.cmd'%(para.pythiacards_dir,process)
    if eosexist(pythiacard)==False:
        print 'pythia card does not exist: ',pythiacard
        readdic.comparedics()
        readdic.finalize()
        sys.exit(3)

    i=0
    njobstmp=njobs
    ################# continue if job already exist and process if not
    while i<njobstmp:
        if outdict.jobexits(sample=process,jobid=i): 
            print 'job i ',i,'  exists    njobs ',njobs
            i+=1
            njobstmp+=1
            continue
        else:
            print 'job does not exists: ',i,' sending'


        logdir=Dir+"/BatchOutputs/%s/%s/"%(version,process)
        os.system("mkdir -p %s"%logdir)
        frunname = 'job%i.sh'%(i)

        frun = None
        try:
            frun = open(logdir+'/'+frunname, 'w')
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            time.sleep(10)
            frun = open(logdir+'/'+frunname, 'w')


        commands.getstatusoutput('chmod 777 %s/%s'%(logdir,frunname))
        frun.write('#!/bin/bash\n')
        frun.write('unset LD_LIBRARY_PATH\n')
        frun.write('unset PYTHONHOME\n')
        frun.write('unset PYTHONPATH\n')
        frun.write('source %s\n'%(para.stack))
        frun.write('mkdir job%i_%s\n'%(i,process))
        frun.write('cd job%i_%s\n'%(i,process))
        frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
        frun.write('mkdir -p %s%s/%s\n'%(para.delphes_dir,version,process))
        frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_base))
        if 'fcc' in version:
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mmr))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mr))
        frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s config.py \n'%(fccconfig))
        frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s card.cmd\n'%(pythiacard))           
        frun.write('%s/run fccrun.py config.py --delphescard=card.tcl --inputfile=card.cmd --outputfile=events%i.root --nevents=%i\n'%(para.fccsw,i,events))
        frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events%i.root %s%s/%s/events%i.root\n'%(i,para.delphes_dir,version,process,i))
        frun.write('cd ..\n')
        frun.write('rm -rf job%i_%s\n'%(i,process))

        if mode=='batch':
            cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -cwd%s %s" %(queue, logdir,logdir+'/'+frunname)
            batchid=-1
            if test==False and fakeadd==False:
                job,batchid=SubmitToBatch(cmdBatch,10)
                nbjobsSub+=job
                outdict.addjob(sample=process,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s%s/%s/events%i.root'%(para.delphes_dir,version,process,i),batchid=batchid,script='%s/%s'%(logdir,frunname),inputlhe='Pythia8',plots='none')
            elif test==False and fakeadd==True:
                outdict.addjob(sample=process,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s%s/%s/events%i.root'%(para.delphes_dir,version,process,i),batchid=batchid,script='%s/%s'%(logdir,frunname),inputlhe='Pythia8',plots='none')
        elif mode=='local':
            os.system('./tmp/%s'%frunname)

        else: 
            print 'unknow running mode: %s'%(mode)
        i+=1

    print 'succesfully sent %i  jobs'%nbjobsSub
    outdict.write()
    readdic.comparedics()
    readdic.finalize()


    

