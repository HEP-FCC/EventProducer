#python check_outputs.py /eos/experiment/fcc/hh/simulation/samples/v01
import glob, os, sys
import commands
import time
import random
from datetime import datetime
import ROOT as r
import json
import EventProducer.common.utils as ut
import EventProducer.common.checker as chk
import EventProducer.common.send_lhe as slhe


#__________________________________________________________
if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('-p','--process', type=str, help='Name of the process to use to send jobs or for the check', default='')

    genTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    genTypeGroup.add_argument("--reco", action='store_true', help="reco events")
    genTypeGroup.add_argument("--LHE", action='store_true', help="LHE events")

    accTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    accTypeGroup.add_argument("--FCC", action='store_true', help="100TeV FCC machine")
    accTypeGroup.add_argument("--HELHC", action='store_true', help="27TeV HE-LHC")

    jobTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    jobTypeGroup.add_argument("--check", action='store_true', help="run the jobchecker")
    jobTypeGroup.add_argument("--send", action='store_true', help="send the jobs")

    checkTypeGroup = parser.add_argument_group('arguments for check')
    checkTypeGroup.add_argument("--dir", help="input directory, optional", default='')

    sendjobGroup = parser.add_argument_group('type of jobs to send')
    sendjobGroup.add_argument('--type', type=str, required = '--send' in sys.argv, help='type of jobs to send', choices = ['lhe','lhep8','p8'])
    sendjobGroup.add_argument('-q', '--queue', type=str, default='8nh', help='lxbatch queue (default: 8nh)', choices=['1nh','8nh','1nd','2nd','1nw'])
    sendjobGroup.add_argument('-n','--numEvents', type=int, help='Number of simulation events per job', default=10000)
    sendjobGroup.add_argument('-N','--numJobs', type=int, default = 10, help='Number of jobs to submit')
    
    args, _ = parser.parse_known_args()

    batchGroup = parser.add_mutually_exclusive_group(required = args.send) # Where to submit jobs
    batchGroup.add_argument("--lsf", action='store_true', help="Submit with LSF")
    batchGroup.add_argument("--condor", action='store_true', help="Submit with condor")

    args, _ = parser.parse_known_args()
    sendOpt = args.type
    

    if args.FCC:
        import EventProducer.config.param as para
        print 'import FCC config'
    elif args.HELHC:
        import EventProducer.config.param_HELHC as para
        print 'import HE-LHC config'
    else:
        print 'problem, need to specify --FCC or --HELHC'
        sys.exit(3)

    if args.check:
        print 'running the check'
    elif args.send:
        print 'sending jobs'
    else:
        print 'problem, need to specify --check or --send'
        sys.exit(3)


    versionGroup = parser.add_argument_group('recontruction version')
    versionGroup.add_argument('--version', type=str, required = '--reco' in sys.argv, help='Version to use', choices = para.fcc_versions)
    args, _ = parser.parse_known_args()
    version = args.version

    indict=None
    inread=None
    indir=None
    fext=None
    if args.LHE:
        indict=para.lhe_dic
        inread=para.readlhe_dic
        indir=para.lhe_dir
        fext=para.lhe_ext
        print 'Running LHE production system'
    elif args.reco:
        indict=para.fcc_dic.replace('VERSION',version)
        inread=para.readfcc_dic.replace('VERSION',version)
        indir='%s%s'%(para.delphes_dir,version)
        fext=para.delphes_ext
        print 'Running reco production system with version %s'%version
    else:
        print 'problem, need to specify --reco or --LHE'
        sys.exit(3)

    if not ut.testeos(para.eostest,para.eostest_size):
        print 'eos seems to have problems, should check, will exit'
        sys.exit(3)
    

    if args.check:
        if args.dir!='':
            print 'using a specific input directory ',args.dir
            indir=args.dir
        if args.process!='':
            print 'using a specific process ',args.process
        checker=chk.checker(indict, indir, inread, para, fext, args.process)
        checker.check()

    
    elif args.send:
        
        if args.lsf:
            print 'send to lsf'
            print 'queue  ', args.queue
        elif args.condor:
            print 'send to condor'
            print 'queue  ', args.queue
 
        if sendOpt=='lhe':
            print 'preparing to send lhe jobs from madgraph gridpacks'
            sendlhe=slhe.send_lhe(njobs,events, args.sample, args.lsf, args.queue)

        elif sendOpt=='lhep8':
            print 'preparing to send FCCSW jobs from lhe'
        elif sendOpt=='p8':
            print 'preparing to send FCCSW jobs from pythia8'

