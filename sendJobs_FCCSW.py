#python sendJobs_FCCSW.py -n 10 -p pp_w012j_5f -q 8nh -e -1 -i $FCCUSERPATH/Generation/data/Pythia_LHEinput.cmd

import glob, os, sys,subprocess,cPickle
import commands
import time
import random
import param
import json
import dicwriter_FCC as dicr


#python sendJobs_FCCSW.py -n 1 -p BBB_4p


FCCSW=os.environ["FCCUSERPATH"]
indictname='/afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json'
indict=None
with open(indictname) as f:
    indict = json.load(f)
outdict=dicr.dicwriter('/afs/cern.ch/work/h/helsens/public/FCCDicts/PyhtiaDelphesdict_%s.json'%param.version)

#__________________________________________________________
def getCommandOutput(command):
    p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout,stderr = p.communicate()
    return {"stdout":stdout, "stderr":stderr, "returncode":p.returncode}


#__________________________________________________________
def SubmitToBatch(cmd,nbtrials):
    submissionStatus=0
    for i in range(nbtrials):            
        outputCMD = getCommandOutput(cmd)
        stderr=outputCMD["stderr"].split('\n')
        jobid=outputCMD["stdout"].split()[1].replace("<","").replace(">","")

        for line in stderr :
            if line=="":
                print "------------GOOD SUB"
                submissionStatus=1
                break
            else:
                print "++++++++++++ERROR submitting, will retry"
                print "Trial : "+str(i)+" / "+str(nbtrials)
                time.sleep(10)
                break
            
        if submissionStatus==1:
            return 1,jobid
        
        if i==nbtrials-1:
            print "failed sumbmitting after: "+str(nbtrials)+" trials, will exit"
            return 0,jobid

#__________________________________________________________
if __name__=="__main__":
    Dir = os.getcwd()
    
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option ('-n','--njobs', help='Number of jobs to submit',
                       dest='njobs',
                       default='10')

    parser.add_option ('-e', '--events',  help='Number of event per job. default is 100',
                       dest='events',
                       default='10000')

    parser.add_option ('-m', '--mode',  help='Running mode [batch, local]. Default is batch',
                       dest='mode',
                       default='batch')

    parser.add_option ('-p', '--process',  help='process, example B_4p',
                       dest='process',
                       default='')

    parser.add_option ('-q', '--queue',  help='lxbatch queue, default 8nh',
                       dest='queue',
                       default='8nh')

    parser.add_option('-t','--test',
                      action='store_true', dest='test', default=False,
                      help='don\'t send to batch nor write to the dictonary')

    parser.add_option ('-i', '--inputfile',  help='pythia 8 configuration file, example $FCCUSERPATH/Generation/data/Pythia_LHEinput.cmd',
                       dest='inputfile',
                       default='')

    (options, args) = parser.parse_args()
    njobs    = int(options.njobs)
    events   = int(options.events)
    mode     = options.mode
    process  = options.process
    queue    = options.queue
    test     = options.test
    pythiacard = options.inputfile
    rundir = os.getcwd()
    nbjobsSub=0

    for pr in param.gridpacklist:
        if process!='' and process !=pr:continue

        i=0
        njobstmp=njobs
        while i<njobstmp:
            if outdict.jobexits(sample=pr,jobid=i): 
                print 'job i ',i,'  exists    njobs ',njobs
                i+=1
                njobstmp+=1
                continue
            else:
                print 'job does not exists: ',i

            LHEexist=False
            LHEfile=''
            for j in indict[pr]:
                if i==j['jobid'] and j['status']=='done':
                    LHEexist=True
                    LHEfile=j['out']
                    break
                
            if not LHEexist:
                print 'LHE does not exist, continue'
                i+=1
                njobstmp+=1
                if i>len(indict[pr]): break
                continue

            logdir=Dir+"BatchOutputs/%s/%s/"%(param.version,pr)
            os.system("mkdir -p %s"%logdir)
            frunname = 'job%i.sh'%(i)
            frun = open(logdir+'/'+frunname, 'w')
            commands.getstatusoutput('chmod 777 %s/%s'%(logdir,frunname))
            frun.write('#!/bin/bash\n')
            frun.write('localdir=$PWD\n')
            frun.write('cd %s\n'%(FCCSW))
            frun.write('source ./init.sh\n')
            frun.write('cd $localdir\n')
            frun.write('mkdir job%i_%s\n'%(i,pr))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source /afs/cern.ch/project/eos/installation/client/etc/setup.sh\n')
            frun.write('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select mkdir %s%s/n'%(para.outdir_delphes,pr))
            frun.write('cd job%i_%s\n'%(i,pr))
            frun.write('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp %s .\n'%(LHEfile))
            frun.write('gunzip -c %s > events.lhe\n'%LHEfile.split('/')[-1])
            frun.write('cp %sSim/SimDelphesInterface/options/PythiaDelphes_config.py .\n'%(FCCSW))
#            frun.write('cp %sGeneration/data/Pythia_LHEinput_batch.cmd card.cmd\n'%(FCCSW))
            frun.write('cp %s card.cmd\n'%(pythiacard))
            frun.write('echo "Beams:LHEF = events.lhe" >> card.cmd\n')
            frun.write('cp %sSim/SimDelphesInterface/data/FCChh_DelphesCard_Baseline_v01.tcl card.tcl\n'%(FCCSW))
            frun.write('cp %sSim/SimDelphesInterface/data/muonMomentumResolutionVsP.tcl .\n'%(FCCSW))
            frun.write('cp %sSim/SimDelphesInterface/data/momentumResolutionVsP.tcl .\n'%(FCCSW))
            frun.write('%s/run fccrun.py PythiaDelphes_config.py --delphescard=card.tcl --inputfile=card.cmd --outputfile=events%i.root --nevents=%i\n'%(FCCSW,i,events))
            frun.write('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp events%i.root %s%s/events%i.root\n'%(i,param.outdir_delphes,pr,i))
            frun.write('cd ..\n')
            frun.write('rm -rf job%i_%s\n'%(i,pr))
            print pr

            if mode=='batch':
                cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -cwd%s %s" %(queue, logdir,logdir+'/'+frunname)
                batchid=-1
                if test==False:
                    job,batchid=SubmitToBatch(cmdBatch,10)
                    nbjobsSub+=job
                    outdict.addjob(sample=pr,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s%s/events%i.root'%(param.outdir_delphes,pr,i),batchid=batchid,script='%s/%s'%(logdir,frunname),inputlhe=LHEfile,plots='none')
            elif mode=='local':
                os.system('./tmp/%s'%frunname)

            else: 
                print 'unknow running mode: %s'%(mode)
            i+=1
    print 'succesfully sent %i  jobs'%nbjobsSub
    outdict.write()



    

