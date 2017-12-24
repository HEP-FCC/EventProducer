#python bin/sendJobs_FCCSW.py -n 10 -p pp_h012j_5f -q 8nh -e -1 -d haa --test
#python bin/sendJobs_FCCSW.py secret -n 1 -e -1  -p "pp_h012j_5f" -q 1nh --test
#python bin/sendJobs_FCCSW.py -n 1 -p pp_h012j_5f -q 8nh -e -1 -v fcc_v02


import glob, os, sys,subprocess,cPickle
import commands
import time
import random
import json
from select import select

import EventProducer.common.dicwriter_FCC as dicr
import EventProducer.common.isreading as isr
secret=False
if sys.argv[1]=="secret":
    import EventProducer.config.param_test as para
    secret=True
else:
    import EventProducer.config.param as para

indictname=para.lhe_dic
indict=None
with open(indictname,'r') as f:
    indict = json.load(f)

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
def eosexist(myfile):
    cmd='ls %s'%(myfile)
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    if len(p.stderr.readline())==0:
        return True
    else: 
        return False


#__________________________________________________________
if __name__=="__main__":
    Dir = os.getcwd()
    
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option ('-n','--njobs', help='Number of jobs to submit',
                       dest='njobs',
                       default='10000')

    parser.add_option ('-i','--neventmax', help='Number events to produce (summing lhe input events)',
                       dest='ninput',
                       default='-1')

    parser.add_option ('-e', '--events',  help='Number of event per job. default is 100',
                       dest='events',
                       default='-1')

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
                      help='do not send to batch nor write to the dictonary')

    parser.add_option ('-d', '--decay',  help='decay in pythia 8 configuration file, example haa.      '
                       'Pythia cards for all the processes needs to be stored in %s'%para.pythiacards_dir,
                       dest='decay',
                       default='')

    parser.add_option ('-v', '--version',  help='version of the delphes card to use, options are: fcc_v01, cms',
                       dest='version',
                       default='fcc_v01')

    (options, args) = parser.parse_args()
    njobs      = int(options.njobs)
    events     = int(options.events)
    mode       = options.mode
    process    = options.process
    queue      = options.queue
    test       = options.test
    decay      = options.decay
    version    = options.version
    ninput     = int(options.ninput)
    rundir = os.getcwd()
    nbjobsSub=0

    if version not in para.fcc_versions:
        print 'version of the cards should be: fcc_v01, fcc_v02, cms'
        sys.exit(3)

#############
    fcc_dic=para.fcc_dic.replace('VERSION',version)
    readfcc_dic=para.readfcc_dic.replace('VERSION',version)

    outdict=dicr.dicwriter(fcc_dic)
    readdic=isr.isreading(readfcc_dic, fcc_dic)
#############

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

    readdic.backup('sendJobs_FCCSW')
    readdic.reading()

    processFound=False

################# Loop over the gridpacks
    for pr in para.gridpacklist:
        #print process, '    ',pr
        if process!='' and process !=pr:continue
        processFound=True


        try: 
            indict[pr]
        except KeyError, e:
            print 'I got a KeyError - reason "%s"' % str(e)
            continue
        print '======================================',process
        pythiacard='%spythia_%s.cmd'%(para.pythiacards_dir,pr)
        if decay!='':
            pythiacard='%spythia_%s_%s.cmd'%(para.pythiacards_dir,pr,decay)
            
        if eosexist(pythiacard)==False:
            print 'pythia card does not exist: ',pythiacard

            timeout = 60
            print "do you want to use the default pythia card [y/n] (60sec to reply)"
            rlist, _, _ = select([sys.stdin], [], [], timeout)
            if rlist:
                s = sys.stdin.readline()
                if s=="y\n":
                    print 'use default card'
                    pythiacard='%spythia_default.cmd'%(para.pythiacards_dir)
                else:
                    print 'exit'
                    readdic.comparedics()
                    readdic.finalize()
                    sys.exit(3)
            else:
                print "timeout, use default card"
                pythiacard='%spythia_default.cmd'%(para.pythiacards_dir)

        pr_noht=''
        if '_HT_' in pr:
            ssplit=pr.split('_')
            stest=''
            for s in xrange(0,len(ssplit)-3):
                stest+=ssplit[s]+'_'
            pr_noht= stest[0:len(stest)-1]

        #check that the specified decay exists
        if pr in para.decaylist and decay != '' and '_HT_' not in pr:
            if decay not in para.decaylist[pr]:
                print 'decay ==%s== does not exist for process ==%s=='%(decay,process)
                readdic.comparedics()
                readdic.finalize()
                sys.exit(3)

        #check that the specified decay exists
        if pr_noht in para.decaylist and decay != '' and '_HT_' in pr:
            if decay not in para.decaylist[pr_noht]:
                print 'decay ==%s== does not exist for process ==%s=='%(decay,process)
                readdic.comparedics()
                readdic.finalize()
                sys.exit(3)
        pr_decay=pr
        if decay!='':
            pr_decay=pr+'_'+decay
        print '====',pr_decay,'===='

        i=0
        nevtmax=0
        njobstmp=njobs
        ################# continue if job already exist and process if not
        while i<njobstmp:
            if outdict.jobexits(sample=pr_decay,jobid=i): 
                print 'job i ',i,'  exists, continue'
                i+=1
                njobstmp+=1
                continue
            else:
                print 'job ',i,' does not exists'

            LHEexist=False
            LHEfile=''
            ################# break if already exist
            for j in indict[pr]:
                if i==int(j['jobid']) and j['status']=='done':
                    LHEexist=True
                    LHEfile=j['out']
                    break
                
            ################# if no LHE proceed
            if not LHEexist:
                print 'LHE does not exists: ',i,', continue'
                i+=1
                njobstmp+=1
                if i>len(indict[pr]): break
                continue


            logdir=Dir+"/BatchOutputs/%s/%s/"%(version,pr_decay)
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
            frun.write('mkdir job%i_%s\n'%(i,pr_decay))
            frun.write('cd job%i_%s\n'%(i,pr_decay))
            frun.write('export EOS_MGM_URL=\"root://eospublic.cern.ch\"\n')
            if secret:
                frun.write('mkdir -p %s\n'%(para.delphes_dir))
                frun.write('mkdir -p %s/%s\n'%(para.delphes_dir,pr_decay))
            else:
                frun.write('mkdir -p %s/%s\n'%(para.delphes_dir,version))
                frun.write('mkdir -p %s%s/%s\n'%(para.delphes_dir,version,pr_decay))

            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(LHEfile))
            frun.write('gunzip -c %s > events.lhe\n'%LHEfile.split('/')[-1])          
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_base))
            if 'fcc' in version:
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mmr))
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s .\n'%(delphescards_mr))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s config.py \n'%(fccconfig))
            frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py %s card.cmd\n'%(pythiacard))
            frun.write('echo "Beams:LHEF = events.lhe" >> card.cmd\n')
           
            frun.write('%s/run fccrun.py config.py --delphescard=card.tcl --inputfile=card.cmd --outputfile=events%i.root --nevents=%i\n'%(para.fccsw,i,events))
            
            if secret:
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events%i.root %s/%s/events%i.root\n'%(i,para.delphes_dir,pr_decay,i))
            else:
                frun.write('python /afs/cern.ch/work/h/helsens/public/FCCutils/eoscopy.py events%i.root %s%s/%s/events%i.root\n'%(i,para.delphes_dir,version,pr_decay,i))
            
            frun.write('cd ..\n')
            frun.write('rm -rf job%i_%s\n'%(i,pr_decay))

            if mode=='batch':
                cmdBatch="bsub -M 2000000 -R \"rusage[pool=2000]\" -q %s -cwd%s %s" %(queue, logdir,logdir+'/'+frunname)
                batchid=-1
                if test==False:
                    job,batchid=SubmitToBatch(cmdBatch,10)
                    nbjobsSub+=job
                    if secret:
                        outdict.addjob(sample=pr_decay,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s/%s/events%i.root'%(para.delphes_dir,pr_decay,i),batchid=batchid,script='%s/%s'%(logdir,frunname),inputlhe=LHEfile,plots='none')
                    else:
                        outdict.addjob(sample=pr_decay,jobid=i,queue=queue,nevents=events,status='submitted',log='%s/LSFJOB_%i'%(logdir,int(batchid)),out='%s%s/%s/events%i.root'%(para.delphes_dir,version,pr_decay,i),batchid=batchid,script='%s/%s'%(logdir,frunname),inputlhe=LHEfile,plots='none')
            elif mode=='local':
                os.system('./tmp/%s'%frunname)

            else: 
                print 'unknow running mode: %s'%(mode)
            i+=1

            if ninput>0:nevtmax+=int(j['nevents'])
            print '===============================================',nevtmax,'   ',ninput
            if (nevtmax>=ninput and ninput>0):
                print 'succesfully sent %i  jobs'%nbjobsSub
                outdict.write()
                readdic.comparedics()
                readdic.finalize()
                print 'ere'
                sys.exit(3)
    if processFound==False: 
        print 'process ===========',process,'============ not found in param.py, please check'
    else:
        print 'succesfully sent %i  jobs'%nbjobsSub
    outdict.write()
    readdic.comparedics()
    readdic.finalize()


    

