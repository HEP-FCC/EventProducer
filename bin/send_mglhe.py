#!/usr/bin/env python
import os, sys
import commands
import time
import EventProducer.common.utils as ut
import EventProducer.common.makeyaml as my

class send_mglhe():

#__________________________________________________________
    def __init__(self, islsf, mg5card, cutfile, model, para, procname, njobs, nev, queue, memory, disk):
        self.islsf     = islsf
        self.user      = os.environ['USER']
        self.mg5card   =  mg5card
        self.cutfile   =  cutfile
        self.model     =  model
        self.para      =  para
        self.procname  =  procname
        self.njobs     =  njobs
        self.nev       =  nev
        self.queue     =  queue
        self.memory    =  memory
        self.disk      =  disk

#__________________________________________________________
    def send(self):
        Dir = os.getcwd()
        nbjobsSub=0

        # output dir
        outdir=self.para.lhe_dir

        logdir=Dir+"/BatchOutputs/lhe/%s"%(self.procname)
        if not ut.dir_exist(logdir):
            os.system("mkdir -p %s"%logdir)

        yamldir = '%s/lhe/%s'%(self.para.yamldir,self.procname)
        if not ut.dir_exist(yamldir):
            os.system("mkdir -p %s"%yamldir)

        outdir  = os.path.abspath(outdir)
        mg5card = os.path.abspath(self.mg5card)
        cuts    = os.path.abspath(self.cutfile)
        model   = os.path.abspath(self.model)

        jobsdir = './BatchOutputs/lhe/' + self.procname

        if not os.path.exists(jobsdir):
           os.makedirs(jobsdir)
           os.makedirs(jobsdir+'/std/')
           os.makedirs(jobsdir+'/cfg/')

        while nbjobsSub<self.njobs:
            #uid = int(ut.getuid(self.user))
            uid = ut.getuid2(self.user)
            myyaml = my.makeyaml(yamldir, uid)
            if not myyaml: 
                print 'job %s already exists'%uid
                continue

            if ut.file_exist('%s/%s/events_%s.lhe.gz'%(outdir,self.procname,uid)):
                print 'already exist, continue'
                continue
    
            print 'Submitting job '+str(uid)+' out of '+str(self.njobs)
            seed = str(uid)
            basename =  self.procname+ '_'+seed

            cmdBatch = 'bsub -o '+jobsdir+'/std/'+basename +'.out -e '+jobsdir+'/std/'+basename +'.err -q '+self.queue
            cmdBatch += ' -R "rusage[mem={}:pool={}]"'.format(self.memory,self.disk)
            cmdBatch +=' -J '+basename+' "./bin/submitMG.sh '+mg5card+' '+self.procname+' '+outdir+' '+seed+' '+str(self.nev)+' '+cuts+' '+model+'"'

            print cmdBatch
                
            batchid=-1
            job,batchid=ut.SubmitToLsf(cmdBatch,10)
            nbjobsSub+=job

        print 'succesfully sent %i  jobs'%nbjobsSub
  
    

