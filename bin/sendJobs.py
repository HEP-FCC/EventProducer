#Script to send jobs to batch running examples:
#
#To run 10 jobs of 10000 events a single process pp_hh_bbaa on the 1nd queue:
#python bin/sendJobs.py -n 10 -e 10000  -p "pp_hh_bbaa" -q 1nd
#
#To run 10 jobs of 10000 events for all processes that contains pp_hh_bbaa  on the 1nd queue:
#python bin/sendJobs.py -n 10 -e 10000  -p "pp_hh_bbaa*" 
#
#To run 10 jobs of 10000 events for all processes in that exists in the config/param.py:
#python bin/sendJobs.py -n 10 -e 10000 -q "1nd"
#
#To run a test job
#python bin/sendJobs.py -n 1 -e 1  -p "pp_hh_bbaa" -q 1nd --test

#!/usr/bin/env python
import json, sys
import glob, os, sys,subprocess,cPickle
import commands
import time
import random
import EventProducer.common.dicwriter as dicr
import EventProducer.common.isreading as isr
import EventProducer.config.param as para

mydict=dicr.dicwriter(para.lhe_dic)
readdic=isr.isreading(para.readlhe_dic, para.lhe_dic)

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

        for line in stderr :
            if line=="":
                print "------------GOOD SUB"
                submissionStatus=1
                break
            else:
                print "++++++++++++ERROR submitting, will retry"
                print "error: ",stderr
                print "Trial : "+str(i)+" / "+str(nbtrials)
                time.sleep(10)
                break
            
        if submissionStatus==1:
            jobid=outputCMD["stdout"].split()[1].replace("<","").replace(">","")
            return 1,jobid
        
        if i==nbtrials-1:
            print "failed sumbmitting after: "+str(nbtrials)+" trials, will exit"
            return 0,0


#__________________________________________________________
def SubmitToCondor(cmd,nbtrials):
    submissionStatus=0
    for i in xrange(nbtrials):            
        outputCMD = getCommandOutput(cmd)
        stderr=outputCMD["stderr"].split('\n')
        stdout=outputCMD["stdout"].split('\n')

        if len(stderr)==1 and stderr[0]=='' :
            print "------------GOOD SUB"
            submissionStatus=1
        else:
            print "++++++++++++ERROR submitting, will retry"
            print "Trial : "+str(i)+" / "+str(nbtrials)
            print "stderr : ",stderr
            print "stderr : ",len(stderr)

            time.sleep(10)
 

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

    parser.add_option ('-p', '--process',  help='Specify here the process. Examples:                    '
'1) pp_vh012j_5f: will send only the process that matches exactely pp_vh012j_5f                        '
'2) pp_vh012j_5f*: will send all the processes that contains pp_vh012j_5f                                  '
'3) If nothing specified, will proceed with sending all existing processes, take care!',
                       dest='process',
                       default='')

    parser.add_option ('-q', '--queue',  help='lxbatch queue, default 8nh',
                       dest='queue',
                       default='8nh')

    parser.add_option("-t","--test",
                      action="store_true", dest="test", default=False,
                      help="don't send to batch nor write the the dictonary")

    (options, args) = parser.parse_args()
    njobs    = int(options.njobs)
    events   = int(options.events)
    mode     = options.mode
    process  = options.process
    queue    = options.queue
    test     = options.test
    rundir = os.getcwd()
    nbjobsSub=0

    readdic.backup('sendJobs')
    readdic.reading()

    processfound=False
    for pr in para.gridpacklist:
        if '*' in process:
            if (process!='') and (process not in pr): continue
        else:
            if (process!='') and (process != pr): continue
        processFound=True
        i=0
        njobstmp=njobs
        while i<njobstmp:
            if mydict.jobexits(sample=pr,jobid=i): 
                print 'job i ',i,'  exists    njobs ',njobs
                i+=1
                njobstmp+=1
                continue

            else:
                print 'job does not exists: ',i

            logdir=Dir+"/BatchOutputs/%s"%(pr)
            eosbase='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select'


            os.system("mkdir -p %s"%logdir+'/job%s/'%str(i))
            os.system('export LSB_JOB_REPORT_MAIL="N"')
            frunname = 'job%i.sh'%(i)
            frun = open(logdir+'/job%s/'%str(i)+frunname, 'w')
            commands.getstatusoutput('chmod 777 %s/%s'%(logdir+'/job%s'%str(i),frunname))
            frun.write('unset LD_LIBRARY_PATH\n')
            frun.write('unset PYTHONHOME\n')
            frun.write('unset PYTHONPATH\n')
            frun.write('mkdir job%i_%s\n'%(i,pr))
            frun.write('cd job%i_%s\n'%(i,pr))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            frun.write('source /afs/cern.ch/project/eos/installation/client/etc/setup.sh\n')
            frun.write('source %s\n'%(para.stack))
            frun.write('%s mkdir %s%s\n'%(eosbase, para.lhe_dir,pr))
            frun.write('%s cp %s/%s.tar.gz .\n'%(eosbase,para.gp_dir,pr))
            frun.write('tar -zxf %s.tar.gz\n'%pr)
            frun.write('cd process/\n')
            frun.write('./run.sh %i %i\n'%(events,i+1))
            frun.write('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select cp events.lhe.gz %s/%s/events%i.lhe.gz\n'%(para.lhe_dir,pr,i))
            frun.write('cd ..\n')
            frun.write('rm -rf job%i_%s\n'%(i,pr))
            print pr

            if mode=='batch':
                    #cmdBatch = 'bsub -o %s%s/%s/log_job%i.log -q 8nh %s/tmp/%s'%(para.outdir,pr,ht.replace('.tar.gz',''),i,Dir,frunname)
                cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -outdir %s -cwd %s %s" %(queue,logdir+'/job%s/'%(str(i)),logdir+'/job%s/'%(str(i)),logdir+'/job%s/'%(str(i))+frunname)
                #print cmdBatch
                
                batchid=-1
                if test==False:
                    job,batchid=SubmitToBatch(cmdBatch,10)
                    nbjobsSub+=job
                    if job==1:
                        mydict.addjob(sample=pr,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s%s/events%i.lhe.gz'%(para.lhe_dir,pr,i),batchid=batchid,script='%s/%s'%(logdir,frunname))

            elif mode=='local':
                os.system('./tmp/%s'%frunname)

            else: 
                print 'unknow running mode: %s'%(mode)
            i+=1

    if processFound==False: 
        print 'process ===========',process,'============ not fonund in param.py, please check'
    else:
        print 'succesfully sent %i  jobs'%nbjobsSub
    mydict.write()
    readdic.comparedics()
    readdic.finalize()
    

