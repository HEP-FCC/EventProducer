EventProducer
=============

This package is used to centrally produced events for FCC-hh, HE-LHC at a center of mass of 100 and 27TeV respectively and for FCC-ee. Any other future collider can also be supported by this framework. 
In order to use it, please get in contact with clement.helsens@cern.ch as running this package requieres specific rights.

This branch ```spring2021``` is intended for FCC-ee event generation. Therefore all following examples will be specified for FCC-ee.

Table of contents
=================
  * [EventProducer](#eventproducer)
  * [Table of contents](#table-of-contents)
  * [Clone and initialisation](#clone-and-initilisation)
  * [Generate LHE events from gridpacks](#generate-lhe-events-from-gridpacks)
  * [Generate LHE files directly from MG5](#generate-lhe-files-directly-from-mg5)
  * [Generate FCCSW files from the LHE and decay with Pyhtia8](#generate-fccsw-files-from-the-lhe-and-decay-with-pyhtia8)
  * [Generate FCCSW files from Pythia8](#generate-fccsw-files-from-pythia8)
  * [Expert mode](#expert-mode)
     * [Updating the database](#updating-the-database)
     * [Cleaning bad jobs](#cleaning-bad-jobs)
     * [Update the webpage](#update-the-webpage)
     * [Create the sample list for analyses](#create-the-sample-list-for-analyses)

Clone and initialisation
========================

If you do not attempt to contribute to the repository, simply clone it:
```
git clone git@github.com:FCC-hh-framework/EventProducer.git
```

If you aim at contributing to the repository, you need to fork and then clone the forked repository:
```
git clone git@github.com:YOURGITUSERNAME/EventProducer.git
```

Then initialise:
```
source ./init.sh
```

In order to run batch generation, please add your CERN user name to the userlist in ```config/users.py```

Generate LHE files from gripacks
================================

To send jobs starting from a gridpack that does not exist but that you have produced, do the following:
   - place gridpack on eos 
     - for FCC-hh ```/eos/experiment/fcc/hh/generation/gridpacks/```
     - for HELHC ```/eos/experiment/fcc/helhc/generation/gridpacks/```
     - for FCC-ee ```/eos/experiment/fcc/ee/generation/gridpacks/```
   - if the gridpack is from Madgraph, name it ```mg_process``` (and call option ```gp_mg``` when running generation commands), if from powheg please name it ```pw_process``` (and call option ```gp_pw```),
   - add to ```config/param_FCCee.py``` an entry corresponding to the gridpack name in the ```gridpacklist``` list, depending on the study.

If the gridpack already exists or has been properly added to the ```param```, then simply run:

```
python bin/run.py --FCCee --LHE --send --condor --typelhe <gp> -p <process> -n <nevents> -N <njobs> -q <queue> --version <version> --detector <detector>
```

example to send 10 jobs of 10 000 events of di-electron events with Mll> 2TeV using longlunch queue of HTCondor for HELHC:

```
python bin/run.py --FCCee --LHE --send --condor --typelhe gp_mg -p mg_ee_zhh_ecm365 -n 10000 -N 10 -q longlunch --version spring2021 --detector IDEA
```

The options ```--ncpus``` and ```--priority``` can also be specified to increase the numbers of cpus on the cluster and to change the priority queue. 


Generate LHE files directly from MG5
=====================================

To send jobs directly from MG5, you need a configuration file (see in ```mg5/examples``` directory ```*.mg5```) and, optionally:
   - a ```cuts.f``` file (containing additional cuts)
   - a model (see in ```models``` directory for instance)

**N.B.** At the moment no example is generated for FCC-ee this way. Below is an example for FCC-hh.

As before, you need to add the process to the ```config/param_FCC.py``` file. Thn you can run with the following command:

```
python bin/run.py --FCC --LHE --send --condor --typelhe mg -p mg_pp_hh_test --mg5card mg5/examples/pp_hh.mg5 --model mg5/models/loop_sm_hh.tar -N 2 -n 10000 -q workday  --memory 16000. --disk 8000.
```

The options ```--ncpus``` and ```--priority``` can also be specified to increase the numbers of cpus on the cluster and to change the priority queue. 



Generate FCCSW files from the LHE and decay with Pyhtia8
========================================================

1. if you want to let pythia decay without specifiying anything, you can use the default card, but if you have requested extra partons at matrix element, you might need to specify matching parameters to your pythia card
1. if you want to use a specific decay, make sure that the decay you want is in ```decaylist``` and ```branching_ratios``` of the ```param```
1. then create appropriate pythia8 card, by appending standard card with decay syntax if needed and add it to the proper directory.
For FCC-ee this directory is
```
/eos/experiment/fcc/ee/generation/FCC-config/spring2021/FCCee/Generator/Pythia8/
```
**N.B.**: please do not write there directly. Cards should be added by making a PR to https://github.com/HEP-FCC/FCC-config/tree/spring2021.

1. Run jobs:

```
python bin/run.py --FCC/HELHC --reco --send --type lhep8 --condor -p <process> -N <njobs> -q <queue> --version <version> --detector <detector>
```

Example produce 10 jobs of FCC Delphes events of ttz decaying the Z to neutrinos. :

```
python bin/run.py --FCCee --reco --send --type lhep8 --condor -p mg_ee_zhh_ecm365 -N 10 -q workday --version spring2021 --detector IDEA
``` 

Please note that the decay in pythia is optional, and that there is no need to specify the number of events to run on as it will by default run over all the events present in the LHE file

The options ```--ncpus``` and ```--priority``` can also be specified to increase the numbers of cpus on the cluster and to change the priority queue. 


Generate FCCSW files from Pythia8
=================================

The Pythia8 manual is available here: http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html

1. Define process in pythialist in the ```param``` corresponding to your job flavour
1. Write Pythia8 process card and put it in: ```/eos/experiment/fcc/ee/generation/FCC-config/spring2021/FCCee/Generator/Pythia8``` by making a PR to https://github.com/HEP-FCC/FCC-config/tree/spring2021, 
for example ```p8_ee_Zbb_ecm91.cmd```

1. send jobs

```
python bin/run.py --FCC/HELHC/FCCee --reco --send --type p8 --condor -p <process>  --pycard <pythia_card> -n <nevents> -N <njobs> -q <queue> --version <version> --detector <detector>
```

Example produce 1 job of 10000 events of ZH at FCC-ee 240GeV

```
python bin/run.py --FCCee --reco --send --type p8 -p p8_ee_ZH_ecm240 -n 10000 -N 1 --condor -q longlunch --version spring2021 --detector IDEA
```

The options ```--ncpus``` and ```--priority``` can also be specified to increase the numbers of cpus on the cluster and to change the priority queue. 

**Important**: If ```--pycard``` option not specified, this step wil lrun with the default pythia8 card (in this case ```p8_ee_default.cmd```), that does not include specific decays nor specific matching/merging parameters. 


Expert mode
===========
The following commands should be run with care, as they update the database, webapge etc...
They run every two hours with crontab, thus you will eventually know when your sample is ready to be used.
The ```--force``` option is used to force the script to run as to optimze running time, processes that have not been flagged will not be checked.

Updating the database
==========================
1) First one need to check the eos directories that have been populated with new files. 
Example for LHE:
```
python bin/run.py --FCCee --LHE --checkeos [--process process] [--force]
```

Example for Delphes events:
```
python bin/run.py --FCCee --reco --checkeos --version helhc_v01 [--process process] [--force]
```

2) Second one need to check the quality of the files that have been produced. 
Example for LHE:
```
python bin/run.py --FCCee --LHE --check [--process process] [--force]
```

Example for Delphes events:
```
python bin/run.py --FCCee --reco --check --version helhc_v01 [--process process] [--force]
```

3) Then the checked files needs to be merged:
Example for LHE:
```
python bin/run.py --FCCee --LHE --merge [--process process] [--force]
```

Example for Delphes events:
```
python bin/run.py --FCCee --reco --merge --version helhc_v01 [--process process] [--force]
```

Cleaning bad jobs
=================
To clean jobs that are flagged as bad, the following command can be used for LHE:
```
python bin/run.py --FCCee --LHE --clean [--process process]
```

and for Delphes
```
python bin/run.py --FCCee --reco --clean --version spring2021 [--process process]
```

As the code checks the files that are in the end written on eos, we need to clean also old jobs that don't produced outputs 3 days after they started.
To do so run the following command for LHE
```
python bin/run.py --FCCee --LHE --cleanold [--process process]
```

and for Delphes
```
python bin/run.py --FCCee --reco --cleanold --version spring2021 [--process process]
```

If you want to completly remove a process, the following command can be used with care for LHE:

```
python bin/run.py --FCCee --LHE --remove --process process 
```

and for Delphes
```
python bin/run.py --FCCee --reco --remove --process process --version spring2021
```


Update the webpage
==================

The webpage can be updated after the files have been checked and merged by running for LHE
```
python bin/run.py --FCCee --LHE --web
```

and for Delphes
```
python bin/run.py --FCCee --reco --web --version spring2021
```


Create the sample list for analyses
===================================

To create the list of samples to be used in physics analyses
```
python bin/run.py --FCCee --reco --sample --version spring2021
```

