#!/usr/bin/env python3

import argparse
import sys


# _____________________________________________________________________________
def main():
    parser = argparse.ArgumentParser()

    genTypeGroup = parser.add_mutually_exclusive_group(
        required=True
    )  # Type of events to generate
    genTypeGroup.add_argument("--reco", action="store_true", help="reco events")
    genTypeGroup.add_argument("--LHE", action="store_true", help="LHE events")
    genTypeGroup.add_argument("--STDHEP", action="store_true", help="STDHEP events")

    accTypeGroup = parser.add_mutually_exclusive_group(
        required=True
    )  # Type of events to generate
    accTypeGroup.add_argument("--FCChh", action="store_true", help="100TeV FCC machine")
    accTypeGroup.add_argument("--FCCee", action="store_true", help="FCC-ee machine")

    jobTypeGroup = parser.add_mutually_exclusive_group(
        required=True
    )  # Type of events to generate
    jobTypeGroup.add_argument("--check", action="store_true", help="run the jobchecker")
    jobTypeGroup.add_argument(
        "--checkeos",
        action="store_true",
        help="run the checker for number of files in eos and in the merge yaml",
    )
    jobTypeGroup.add_argument(
        "--merge", action="store_true", help="merge the yaml for all the processes"
    )
    jobTypeGroup.add_argument("--send", action="store_true", help="send the jobs")
    jobTypeGroup.add_argument(
        "--clean",
        action="store_true",
        help="clean the dictionnary and eos from bad jobs",
    )
    jobTypeGroup.add_argument(
        "--cleanold",
        action="store_true",
        help="clean the yaml from old jobs (more than 72 hours)",
    )
    jobTypeGroup.add_argument(
        "--web", action="store_true", help="print a dictionary for the webpage"
    )
    jobTypeGroup.add_argument(
        "--remove",
        action="store_true",
        help="remove a specific process from the dictionary and from eos",
    )
    jobTypeGroup.add_argument(
        "--sample", action="store_true", help="make the proc dict"
    )

    sendjobGroup = parser.add_argument_group("type of jobs to send")
    sendjobGroup.add_argument(
        "--type",
        type=str,
        required="--send" in sys.argv and "--reco" in sys.argv,
        help="type of jobs to send",
        choices=["lhep8", "p8", "stdhep"],
    )
    sendjobGroup.add_argument(
        "--typelhe",
        type=str,
        required="--send" in sys.argv and "--LHE" in sys.argv,
        help="type of jobs to send",
        choices=["gp_mg", "gp_pw", "mg", "kkmc"],
    )
    sendjobGroup.add_argument(
        "--typestdhep",
        type=str,
        required="--send" in sys.argv and "--STDHEP" in sys.argv,
        help="type of jobs to send",
        choices=["wzp6"],
    )

    sendjobGroup.add_argument(
        "-q",
        "--queue",
        type=str,
        default="workday",
        help="lxbatch queue (default: workday for HTCONDOR)",
        choices=[
            "1nh",
            "8nh",
            "1nd",
            "2nd",
            "1nw",
            "espresso",
            "microcentury",
            "longlunch",
            "workday",
            "tomorrow",
            "testmatch",
            "nextweek",
        ],
    )
    sendjobGroup.add_argument(
        "--priority",
        type=str,
        default="group_u_FCC.local_gen",
        help="condor queue priority (default: group_u_FCC.local_gen)",
    )
    sendjobGroup.add_argument(
        "--ncpus", type=str, default="1", help="number of CPUs (1CPU=2Gb of RAM)"
    )

    # 41873

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
    sendjobGroup.add_argument(
        "-n",
        "--numEvents",
        type=int,
        help="Number of simulation events per job",
        default=10000,
    )
    sendjobGroup.add_argument(
        "-N", "--numJobs", type=int, default=10, help="Number of jobs to submit"
    )

    # option for running FCC-hh Delphes card validation, using an adapted edm4hep_output config, should only work with option reco.
    sendjobGroup.add_argument(
        "--customEDM4HEPOutput",
        type=str,
        default="",
        help="Use a custom edm4hep output config card, by providing the path.",
    )

    mgGroup = parser.add_argument_group("mggroup")
    mgGroup.add_argument(
        "--mg5card", type=str, help="MG5 configuration", default="card.mg5"
    )
    mgGroup.add_argument(
        "--cutfile", type=str, help="additional cuts", default="cuts.f"
    )
    mgGroup.add_argument("--model", type=str, help="extra model", default="model.tgz")
    # option to run LHE production with MG in centos7 container
    mgGroup.add_argument(
        "--centos7",
        action="store_true",
        help="Legacy option to run MG5 LHE production in centos7 container.",
    )

    kkmcGroup = parser.add_argument_group("kkmcgroup")
    kkmcGroup.add_argument(
        "--kkmccard", type=str, help="KKMC input card", default="card"
    )

    batchGroup = parser.add_mutually_exclusive_group(
        required="--send" in sys.argv
    )  # Where to submit jobs
    batchGroup.add_argument("--lsf", action="store_true", help="Submit with LSF")
    batchGroup.add_argument("--condor", action="store_true", help="Submit with condor")
    batchGroup.add_argument(
        "--local", action="store_true", help="run locally (will not copy files on eos"
    )

    args, _ = parser.parse_known_args()
    sendOpt = args.type

    if (
        args.customEDM4HEPOutput
        and not args.reco
        and not (args.type == "lhep8" or args.type == "p8")
    ):
        parser.error(
            "Option --customEDM4HEPOutput only works for producing edm4hep output, so if --reco and --type lhep8 or p8 options are set."
        )

    if args.centos7 and not args.typelhe == "mg":
        parser.error(
            "Option --centos7 is currently only supported for legacy running of LHE generation with MG."
        )

    if args.FCChh:
        import EventProducer.config.param_FCChh as para

        print("INFO: Importing base FCC-hh config...")
    elif args.FCCee:
        import EventProducer.config.param_FCCee as para

        print("INFO: Importing FCC-ee config...")
    else:
        print("ERROR: One needs to specify --FCChh or --FCCee!\nAborting...")
        sys.exit(3)

    prodTag = [i for i in para.prodTag]
    prodTagGroup = parser.add_argument_group("production tag")
    prodTagGroup.add_argument(
        "--prodtag",
        type=str,
        required="--reco" in sys.argv,
        help="Version to use",
        choices=prodTag,
    )
    prodTagGroup.add_argument(
        "--detector",
        type=str,
        default="",
        required="--reco" in sys.argv,
        choices=para.detectors,
        help="Detector to use",
    )

    args, _ = parser.parse_known_args()

    decaylist = []
    for key, value in para.decaylist.items():
        for v in value:
            if v not in decaylist:
                decaylist.append(v)

    sendjobGroup.add_argument(
        "-d",
        "--decay",
        type=str,
        default="",
        help="pythia8 decay when needed",
        choices=decaylist,
    )
    sendjobGroup.add_argument(
        "--pycard", type=str, default="p8_ee_default.cmd", help="pythia8 card"
    )

    processlist = []
    if (
        (args.reco and args.type == "p8")
        or args.check
        or args.checkeos
        or args.clean
        or args.cleanold
        or args.merge
        or args.remove
    ):
        for key, value in para.pythialist.items():
            processlist.append(key)
        for key, value in para.decaylist.items():
            newkey = key
            if key[0:3] == "mg_":
                newkey = "mgp8_" + key[3:]
            if key[0:3] == "ch_":
                newkey = "chp8_" + key[3:]
            if key[0:5] == "kkmc_":
                newkey = "kkmcp8_" + key[5:]
            for v in value:
                processlist.append("%s_%s" % (newkey, v))
    if (
        args.LHE
        or args.STDHEP
        or args.check
        or args.checkeos
        or args.clean
        or args.merge
        or args.reco
    ):
        for key, value in para.gridpacklist.items():
            processlist.append(key)
    if args.reco and (args.remove or args.clean or args.cleanold):
        for key, value in para.gridpacklist.items():
            if key[0:3] == "mg_":
                processlist.append("mgp8_" + key[3:])
            if key[0:3] == "ch_":
                processlist.append("chp8_" + key[3:])
            if key[0:5] == "kkmc_":
                processlist.append("kkmcp8_" + key[5:])

    parser.add_argument(
        "-p",
        "--process",
        type=str,
        help="Name of the process to use to send jobs or for the check",
        default="",
        choices=processlist,
    )
    parser.add_argument(
        "--force", action="store_true", help="Force the type of process", default=False
    )

    args, _ = parser.parse_known_args()
    version = args.prodtag
    print("INFO: Running version:", version)
    detector = args.detector
    training = False
    if version != None:
        if "training" in version:
            training = True

    sys.argv = []

    indir = None
    yamldir = None
    fext = None
    statfile = None

    if args.LHE:
        indir = para.lhe_dir
        fext = para.lhe_ext
        yamldir = para.yamldir + "lhe/"
        statfile = para.lhe_stat

    elif args.STDHEP:
        fext = para.stdhep_ext
        aprodtag = version.replace("_training", "")
        yamldir = para.yamldir + "stdhep/" + aprodtag + "/"
        indir = para.stdhep_dir + "/" + aprodtag + "/"
        if training:
            yamldir = para.yamldir + "stdhep/" + aprodtag + "/training/"
            indir = para.stdhep_dir + aprodtag + "/training/"
        if (
            "spring2021" in version or "pre_fall2022" in version or "dev" in version
        ):  # for proTags older than winter2023
            indir = para.stdhep_dir
            yamldir = para.yamldir + "stdhep/"
            if training:
                yamldir = para.yamldir + "stdhep/training/"
                indir = para.stdhep_dir + "/training/"
        statfile = para.stdhep_stat.replace("VERSION", version)
        print("yamldir = ", yamldir)
        print("indir = ", indir)

    elif args.reco:
        indir = "%s%s/%s" % (para.delphes_dir, version, detector)
        fext = para.delphes_ext
        yamldir = para.yamldir + version + "/" + detector + "/"
        statfile = para.delphes_stat.replace("VERSION", version).replace(
            "DETECTOR", detector
        )
        print("INFO: Operating on Reco samples:")
        print(f"        - version: {version}")
        print(f"        - detector: {detector}")

    else:
        print("ERROR: Please specify --reco, --STDHEP or --LHE!")
        print("Aborting...")
        sys.exit(3)

    import EventProducer.common.utils as ut

    if not ut.testeos(para.eostest, para.eostest_size):
        print("eos seems to have problems, should check, will exit")
        sys.exit(3)

    if args.check:
        print("running the check")
        if args.process != "":
            print("using a specific process ", args.process)
            if args.reco and args.process[0:3] == "mg_":
                args.process = "mgp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "ch_":
                args.process = "chp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "pw_":
                args.process = "pwp8_" + args.process[3:]
            if args.reco and args.process[0:5] == "kkmc_":
                args.process = "kkmcp8_" + args.process[5:]
        import EventProducer.common.checker_yaml as chky

        print(args.process)
        checker = chky.CheckerYAML(indir, para, fext, args.process, yamldir)
        checker.check(args.force, statfile)

    elif args.checkeos:
        print("running the checkeos")
        if args.process != "":
            print("using a specific process ", args.process)
            if args.reco and args.process[0:3] == "mg_":
                args.process = "mgp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "ch_":
                args.process = "chp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "pw_":
                args.process = "pwp8_" + args.process[3:]
            if args.reco and args.process[0:5] == "kkmc_":
                args.process = "kkmcp8_" + args.process[5:]
        import EventProducer.common.checker_eos as chkeos

        print(args.process)
        checkereos = chkeos.CheckerEOS(yamldir, indir, args.process)
        # (indirafs, indireos, process, version):

        checkereos.check(para)

    elif args.merge:
        print("running the merger")
        if args.process != "":
            print("using a specific process ", args.process)
            if args.reco and args.process[0:3] == "mg_":
                args.process = "mgp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "ch_":
                args.process = "chp8_" + args.process[3:]
            if args.reco and args.process[0:3] == "pw_":
                args.process = "pwp8_" + args.process[3:]
            if args.reco and args.process[0:5] == "kkmc_":
                args.process = "kkmcp8_" + args.process[5:]
        import EventProducer.common.merger as mgr

        isLHE = args.LHE
        merger = mgr.Merger(args.process, yamldir)
        merger.merge(args.force)

    elif args.send:
        print("sending jobs")
        if args.lsf:
            print("send to lsf")
            print("queue  ", args.queue)
        elif args.condor:
            print("send to condor")
            print("queue  ", args.queue)
            print("priority  ", args.priority)
            print("ncpus     ", args.ncpus)
        elif args.local:
            print("run locally")

        if args.LHE:
            if args.typelhe == "gp_mg" or args.typelhe == "gp_pw":
                print(
                    "preparing to send lhe jobs from madgraph/powheg gridpacks for process {}".format(
                        args.process
                    )
                )
                import EventProducer.bin.send_lhe as slhe

                sendlhe = slhe.send_lhe(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    args.typelhe,
                )
                sendlhe.send()

            elif args.typelhe == "mg":
                print(
                    "preparing to send lhe jobs from madgraph standalone for process {}".format(
                        args.process
                    )
                )
                import EventProducer.bin.send_mglhe as mglhe

                sendlhe = mglhe.send_mglhe(
                    args.lsf,
                    args.condor,
                    args.mg5card,
                    args.cutfile,
                    args.model,
                    para,
                    args.process,
                    args.numJobs,
                    args.numEvents,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    do_EL7=args.centos7,
                )
                sendlhe.send()

            elif args.typelhe == "kkmc":
                print(
                    "preparing to send lhe jobs from KKMC for process {}".format(
                        args.process
                    )
                )
                import EventProducer.bin.send_kkmclhe as kkmclhe

                sendlhe = kkmclhe.send_kkmc(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.local,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    version,
                )
                sendlhe.send()

        elif args.STDHEP:
            if args.typestdhep == "wzp6":
                print(
                    "preparing to send Whizard jobs to produce stdhep files for process {}".format(
                        args.process
                    )
                )
                import EventProducer.bin.send_stdhep as sstdhep

                sendstdhep = sstdhep.send_stdhep(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.local,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    version,
                    args.typestdhep,
                    training,
                )
                sendstdhep.send()

        elif args.reco:
            if sendOpt == "lhep8":
                print("preparing to send FCCSW jobs from lhe")
                import EventProducer.bin.send_lhep8 as slhep8

                sendlhep8 = slhep8.send_lhep8(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.local,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    version,
                    args.decay,
                    args.pycard,
                    detector,
                    args.customEDM4HEPOutput,
                )
                sendlhep8.send(args.force)
            elif sendOpt == "p8":
                print("preparing to send FCCSW jobs from pythia8 directly")
                import EventProducer.bin.send_p8 as sp8

                sendp8 = sp8.send_p8(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.local,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    version,
                    training,
                    detector,
                    args.customEDM4HEPOutput,
                )
                sendp8.send()
            elif sendOpt == "stdhep":
                print("preparing to send FCCSW jobs from stdhep")
                import EventProducer.bin.send_fromstdhep as sstdhep

                sendstdhep = sstdhep.send_fromstdhep(
                    args.numJobs,
                    args.numEvents,
                    args.process,
                    args.lsf,
                    args.condor,
                    args.local,
                    args.queue,
                    args.priority,
                    args.ncpus,
                    para,
                    version,
                    detector,
                    args.decay,
                )
                sendstdhep.send(args.force)

    elif args.web:
        import EventProducer.common.printer as prt

        if args.LHE:
            print("INFO: Creating LHE output files for the web page...")
            printdic = prt.Printer(yamldir, para.lhe_web, para, False)
            printdic.run()

        elif args.STDHEP:
            print("INFO: Creating STDHEP output files for the web page...")
            stdhep_webfile = para.stdhep_web.replace("VERSION", version)
            printdic = prt.Printer(yamldir, stdhep_webfile, para, False)
            printdic.run()

        elif args.reco:
            print("INFO: Creating Reco output files for the web page...")
            webpage_file = para.delphes_web.replace("VERSION", version)
            webpage_file = webpage_file.replace("DETECTOR", detector)
            webpage_file = webpage_file.replace("_.", ".")
            printdic = prt.Printer(yamldir, webpage_file, para, True)
            printdic.run()

    elif args.remove:
        if args.process == "":
            print("need to specify a process, exit")
            sys.exit(3)
        if args.LHE:
            print("remove process %s from eos and database for LHE" % args.process)
        elif args.reco:
            print("remove process %s from eos and database for reco" % args.process)
        import EventProducer.common.removeProcess as rmp

        removeProcess = rmp.removeProcess(args.process, indir, yamldir)
        removeProcess.remove()

    elif args.clean:
        print("INFO: Clean the dictionary and EOS")
        import EventProducer.common.cleanfailed as clf

        clean = clf.CleanFailed(indir, yamldir, args.process)
        clean.clean()

    elif args.cleanold:
        print("INFO: Cleaning old jobs that have not been checked...")
        import EventProducer.common.cleanfailed as clf

        clean = clf.CleanFailed(indir, yamldir, args.process)
        clean.cleanoldjobs()

    elif args.sample:
        print("INFO: Generating procDict JSON...")
        import EventProducer.common.makeSampleList as msl

        sample = msl.MakeSampleList(para, version, detector)
        sample.makelist()

    else:
        print("problem, need to specify --check or --send")
        sys.exit(3)


# _____________________________________________________________________________
if __name__ == "__main__":
    main()
