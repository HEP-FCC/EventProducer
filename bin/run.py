#python bin/run.py --HELHC --LHE --send -p mg_pp_ee_lo -n 10000 -N 100 --lsf -q 1nh --typelhe gp
#python bin/run.py --HELHC --LHE --check --process mg_gg_aa01j_mhcut_5f_HT_0_100
#python bin/run.py --HELHC --LHE --checkeos --process mg_gg_aa01j_mhcut_5f_HT_0_100
#python bin/run.py --HELHC --LHE --merge
#python bin/run.py --HELHC --LHE --web
#python bin/run.py --HELHC --LHE --remove -p mg_pp_ee_lo
#python bin/run.py --HELHC --LHE --clean -p mg_pp_ee_lo

#python bin/run.py --HELHC --reco --send -p mg_pp_tt_lo --type lhep8 -N 1 --lsf -q 1nh --version helhc_v01
#python bin/run.py --HELHC --reco --send -p p8_pp_Zprime_10TeV_ll -n 10000 --type p8 -N 1 --lsf -q 1nh --version helhc_v01
#python bin/run.py --HELHC --reco --check --version helhc_v01
#python bin/run.py --HELHC --reco --merge --version helhc_v01
#python bin/run.py --HELHC --reco --web --version helhc_v01
#python bin/run.py --HELHC --reco --remove -p mgp8_pp_tt_lo --version helhc_v01
#python bin/run.py --HELHC --reco --clean --version helhc_v01 -p p8_pp_Zprime_10TeV_ttbar

#python bin/run.py --FCC --LHE --send --version fcc_v02 -p mg_pp_ee_test --typelhe mg --mg5card pp_hh.mg5 --model loop_sm_hh.tar -N 2 -n 10000 -q 8nh --lsf
#python bin/run.py --FCC --LHE --send --condor -p mg_pp_tttt_5f -n 10000 -N 10 -q microcentury --typelhe gp


#python bin/run.py --FCCee --reco --send -p p8_ee_ZH_ecm240 -n 10000 --type p8 -N 1 --condor -q espresso --version fcc_v01


import sys

#__________________________________________________________
if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser()

    genTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    genTypeGroup.add_argument("--reco", action='store_true', help="reco events")
    genTypeGroup.add_argument("--LHE", action='store_true', help="LHE events")
    genTypeGroup.add_argument("--STDHEP", action='store_true', help="STDHEP events")

    accTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    accTypeGroup.add_argument("--FCC", action='store_true', help="100TeV FCC machine")
    accTypeGroup.add_argument("--HELHC", action='store_true', help="27TeV HE-LHC")
    accTypeGroup.add_argument("--FCCee", action='store_true', help="FCC-ee machine")

    jobTypeGroup = parser.add_mutually_exclusive_group(required = True) # Type of events to generate
    jobTypeGroup.add_argument("--check", action='store_true', help="run the jobchecker")
    jobTypeGroup.add_argument("--checkeos", action='store_true', help="run the checker for number of files in eos and in the merge yaml")
    jobTypeGroup.add_argument("--merge", action='store_true', help="merge the yaml for all the processes")
    jobTypeGroup.add_argument("--send", action='store_true', help="send the jobs")
    jobTypeGroup.add_argument("--clean", action='store_true', help="clean the dictionnary and eos from bad jobs")
    jobTypeGroup.add_argument("--cleanold", action='store_true', help="clean the yaml from old jobs (more than 72 hours)")
    jobTypeGroup.add_argument("--web", action='store_true', help="print the dictionnary for webpage")
    jobTypeGroup.add_argument("--remove", action='store_true', help="remove a specific process from the dictionary and from eos" )
    jobTypeGroup.add_argument("--sample", action='store_true', help="make the heppy sample list and proc dict" )

    sendjobGroup = parser.add_argument_group('type of jobs to send')
    sendjobGroup.add_argument('--type', type=str, required = '--send' in sys.argv and '--reco'  in sys.argv , help='type of jobs to send', choices = ['lhep8','p8','stdhep'])
    sendjobGroup.add_argument('--typelhe', type=str, required = '--send' in sys.argv and '--LHE'  in sys.argv , help='type of jobs to send', choices = ['gp_mg','gp_pw','mg','kkmc'])
    sendjobGroup.add_argument('--typestdhep', type=str, required = '--send' in sys.argv and '--STDHEP'  in sys.argv , help='type of jobs to send', choices = ['wzp6'])

    sendjobGroup.add_argument('-q', '--queue', type=str, default='workday', help='lxbatch queue (default: workday for HTCONDOR)', choices=['1nh','8nh','1nd','2nd','1nw','espresso','microcentury','longlunch','workday','tomorrow','testmatch','nextweek'])
    sendjobGroup.add_argument('--priority', type=str, default='group_u_FCC.local_gen', help='condor queue priority (default: group_u_FCC.local_gen)')
    sendjobGroup.add_argument('--ncpus', type=str, default='1', help='number of CPUs (1CPU=2Gb of RAM)')

#41873

    ###################
    # condor queues : #
    ###################
    # 20 mins -> espresso
    # 1h -> microcentury
    # 2h -> longlunch
    # 8h -> workday
    # 1d -> tomorrow
    # 3d -> testmatch
    # 1w -> nextweek
    sendjobGroup.add_argument('-n','--numEvents', type=int, help='Number of simulation events per job', default=10000)
    sendjobGroup.add_argument('-N','--numJobs', type=int, default = 10, help='Number of jobs to submit')



    mgGroup = parser.add_argument_group('mggroup')
    mgGroup.add_argument("--mg5card", type=str, help="MG5 configuration", default='card.mg5')
    mgGroup.add_argument("--cutfile", type=str, help="additional cuts", default='cuts.f')
    mgGroup.add_argument("--model", type=str, help="extra model", default='model.tgz')

    kkmcGroup = parser.add_argument_group('kkmcgroup')
    kkmcGroup.add_argument("--kkmccard", type=str, help="KKMC input card", default='card')

    
    batchGroup = parser.add_mutually_exclusive_group(required = '--send' in sys.argv) # Where to submit jobs
    batchGroup.add_argument("--lsf", action='store_true', help="Submit with LSF")
    batchGroup.add_argument("--condor", action='store_true', help="Submit with condor")
    batchGroup.add_argument("--local", action='store_true', help="run locally (will not copy files on eos")


    
    args, _ = parser.parse_known_args()
    sendOpt = args.type

    if args.FCC:
        import EventProducer.config.param_FCC as para
        print ('import FCC config')
    elif args.HELHC:
        import EventProducer.config.param_HELHC as para
        print ('import HE-LHC config')
    elif args.FCCee:
        import EventProducer.config.param_FCCee as para
        print ('import FCC-ee config')
    else:
        print ('problem, need to specify --FCC or --HELHC')
        sys.exit(3)

    versionGroup = parser.add_argument_group('recontruction version')
    versionGroup.add_argument('--version', type=str, required = '--reco' in sys.argv, help='Version to use', choices = para.fcc_versions)
    versionGroup.add_argument('--detector', type=str, default='', required = '--reco' in sys.argv, help='Detector to use', choices = para.detectors)

    
    decaylist=[]
    for key, value in para.decaylist.items():
        for v in value:
            if v  not in decaylist: decaylist.append(v)
    
    sendjobGroup.add_argument('-d', '--decay', type=str, default='', help='pythia8 decay when needed', choices=decaylist)
    sendjobGroup.add_argument('--pycard', type=str, default='p8_pp_default.cmd', help='pythia8 card')

    processlist=[]
    if (args.reco and args.type=="p8") or args.check or args.checkeos or args.clean or args.cleanold or args.merge or args.remove:
        for key, value in para.pythialist.items():
            processlist.append(key)
        for key, value in para.decaylist.items():
            newkey=key
            if key[0:3]=='mg_': newkey='mgp8_'+key[3:]
            if key[0:3]=='ch_': newkey='chp8_'+key[3:]
            if key[0:5]=='kkmc_': newkey='kkmcp8_'+key[5:]
            for v in value:
                processlist.append("%s_%s"%(newkey,v))
    if args.LHE or args.STDHEP or args.check or args.checkeos or args.clean or args.merge or args.reco:
        for key, value in para.gridpacklist.items():
            processlist.append(key)
    if args.reco and (args.remove or args.clean or args.cleanold):
        for key, value in para.gridpacklist.items():
            if key[0:3]=='mg_': processlist.append('mgp8_'+key[3:])
            if key[0:3]=='ch_': processlist.append('chp8_'+key[3:])
            if key[0:5]=='kkmc_': processlist.append('kkmcp8_'+key[5:])
    


    parser.add_argument('-p','--process', type=str, help='Name of the process to use to send jobs or for the check', default='', choices=processlist)
    parser.add_argument('--force', action='store_true', help='Force the type of process', default=False)

    args, _ = parser.parse_known_args()
    version = args.version
    print("version ",version)
    detector = args.detector
    training=False
    if version!=None:
        if 'training' in version: training=True

    sys.argv = []

    indir=None
    yamldir=None
    fext=None
    statfile=None

    if args.LHE:
        indir=para.lhe_dir
        fext=para.lhe_ext
        yamldir=para.yamldir+'lhe/'
        statfile=para.lhe_stat

    elif args.STDHEP:
        indir=para.stdhep_dir
        fext=para.stdhep_ext
        yamldir=para.yamldir+'stdhep/'
        statfile=para.stdhep_stat

    elif args.reco:
        indir='%s%s/%s'%(para.delphes_dir,version,detector)
        fext=para.delphes_ext
        yamldir=para.yamldir+version+'/'+detector+'/'
        statfile=para.delphes_stat.replace('VERSION',version).replace('DETECTOR',detector)
        print ('Running reco production system with version %s and detector %s'%(version,detector))

    else:
        print ('problem, need to specify --reco or --LHE')
        sys.exit(3)

    import EventProducer.common.utils as ut
    if not ut.testeos(para.eostest,para.eostest_size):
        print ('eos seems to have problems, should check, will exit')
        sys.exit(3)
    

    if args.check:
        print ('running the check')
        if args.process!='':
            print ('using a specific process ',args.process)
            if args.reco and args.process[0:3]=='mg_': args.process='mgp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='ch_': args.process='chp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='pw_': args.process='pwp8_'+args.process[3:]
            if args.reco and args.process[0:5]=='kkmc_' : args.process='kkmcp8_'+args.process[5:]
        import EventProducer.common.checker_yaml as chky
        print (args.process)
        checker=chky.checker_yaml(indir, para, fext, args.process,  yamldir)
        checker.check(args.force, statfile)


    elif args.checkeos:
        print ('running the checkeos')
        if args.process!='':
            print ('using a specific process ',args.process)
            if args.reco and args.process[0:3]=='mg_': args.process='mgp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='ch_': args.process='chp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='pw_': args.process='pwp8_'+args.process[3:]
            if args.reco and args.process[0:5]=='kkmc_' : args.process='kkmcp8_'+args.process[5:]
        import EventProducer.common.checker_eos as chkeos
        print (args.process)
        checkereos=chkeos.checker_eos(yamldir, indir, args.process)
                                    #(indirafs, indireos, process, version):

        checkereos.check(para)

    elif args.merge:
        print ('running the merger')
        if args.process!='':
            print ('using a specific process ',args.process)
            if args.reco and args.process[0:3]=='mg_': args.process='mgp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='ch_': args.process='chp8_'+args.process[3:]
            if args.reco and args.process[0:3]=='pw_': args.process='pwp8_'+args.process[3:]
            if args.reco and args.process[0:5]=='kkmc_' : args.process='kkmcp8_'+args.process[5:]
        import EventProducer.common.merger as mgr
        isLHE=args.LHE
        merger = mgr.merger( args.process, yamldir)
        merger.merge(args.force)

    elif args.send:
        print ('sending jobs')
        if args.lsf:
            print ('send to lsf')
            print ('queue  ', args.queue)
        elif args.condor:
            print ('send to condor')
            print ('queue  ', args.queue)
            print ('priority  ', args.priority)
            print ('ncpus     ', args.ncpus)
        elif args.local:
            print ('run locally')


        if args.LHE:
            
            if args.typelhe == 'gp_mg' or args.typelhe == 'gp_pw' :

                print ('preparing to send lhe jobs from madgraph/powheg gridpacks for process {}'.format(args.process))
                import EventProducer.bin.send_lhe as slhe
                sendlhe=slhe.send_lhe(args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.queue, args.priority, args.ncpus, para, args.typelhe)
                sendlhe.send()
            
            elif args.typelhe == 'mg':

                print ('preparing to send lhe jobs from madgraph standalone for process {}'.format(args.process))
                import EventProducer.bin.send_mglhe as mglhe
                sendlhe=mglhe.send_mglhe( args.lsf, args.condor, args.mg5card, args.cutfile, args.model, para, args.process, args.numJobs, args.numEvents, args.queue, args.priority, args.ncpus)
                sendlhe.send()

            elif args.typelhe == 'kkmc' :
                print ('preparing to send lhe jobs from KKMC for process {}'.format(args.process))
                import EventProducer.bin.send_kkmclhe as kkmclhe
                sendlhe=kkmclhe.send_kkmc( args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.local, args.queue, args.priority, args.ncpus, para, version )
                sendlhe.send()

            
        elif args.STDHEP:

            if args.typestdhep == 'wzp6' :
                print ('preparing to send Whizard jobs to produce stdhep files for process {}'.format(args.process))
                import EventProducer.bin.send_stdhep as sstdhep
                sendstdhep = sstdhep.send_stdhep( args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.local, args.queue, args.priority, args.ncpus, para, version, args.typestdhep)
                sendstdhep.send()


        elif args.reco:
            if sendOpt=='lhep8':
                print ('preparing to send FCCSW jobs from lhe')
                import EventProducer.bin.send_lhep8 as slhep8
                sendlhep8=slhep8.send_lhep8(args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.local, args.queue, args.priority, args.ncpus, para, version, args.decay, args.pycard, detector)
                sendlhep8.send(args.force)
            elif sendOpt=='p8':
                print ('preparing to send FCCSW jobs from pythia8 directly')
                import EventProducer.bin.send_p8 as sp8
                sendp8=sp8.send_p8(args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.local, args.queue, args.priority, args.ncpus, para, version, training, detector)
                sendp8.send()
            elif sendOpt=='stdhep':
                print ('preparing to send FCCSW jobs from stdhep')
                import EventProducer.bin.send_fromstdhep as sstdhep
                sendstdhep=sstdhep.send_fromstdhep(args.numJobs,args.numEvents, args.process, args.lsf, args.condor, args.local, args.queue, args.priority, args.ncpus, para, version, detector, args.decay)
                sendstdhep.send(args.force)



    elif args.web:
        import EventProducer.common.printer as prt
        if args.LHE: 
            print ('create web page for LHE')
            printdic=prt.printer(yamldir,para.lhe_web, False, True, para)
            printdic.run()

        elif args.STDHEP:
            print ('create web page for STDHEP')
            printdic=prt.printer(yamldir,para.stdhep_web, False, True, para)
            printdic.run()
            

        elif args.reco:
            print ('create web page for reco version %s'%version)
            webpage=para.delphes_web.replace('VERSION',version).replace('DETECTOR',detector)
            printdic=prt.printer(yamldir, webpage, True, False, para, detector, version)
            printdic.run()

    elif args.remove:
        if args.process=='':
            print ('need to specify a process, exit')
            sys.exit(3)
        if args.LHE: 
            print ('remove process %s from eos and database for LHE'%args.process)
        elif args.reco: 
            print ('remove process %s from eos and database for reco'%args.process)
        import EventProducer.common.removeProcess as rmp
        removeProcess = rmp.removeProcess(args.process, indir, yamldir)
        removeProcess.remove()
        

    elif args.clean:
        print ('clean the dictionnary and eos')
        import EventProducer.common.cleanfailed as clf
        clean=clf.cleanfailed(indir, yamldir, args.process)
        clean.clean()


    elif args.cleanold:
        print ('clean the dictionnary from old jobs that have not been checked')
        import EventProducer.common.cleanfailed as clf
        clean=clf.cleanfailed(indir, yamldir, args.process)
        clean.cleanoldjobs()

    elif args.sample:
        print ('make the heppy sample list and procDict')
        import EventProducer.common.makeSampleList as msl
        sample=msl.makeSampleList(para, version, detector)
        sample.makelist()

    else:
        print ('problem, need to specify --check or --send')
        sys.exit(3)
