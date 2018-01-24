# EventProducer

This package is used to centrally produced events for FCC-hh, HE-LHC at a center of mass of 100 and 27TeV respectively. Any other future collider can also be supported by this framework. 
In order to use it, please get in contact with clement.helsens@cern.ch as running this package requieres specific rights.

[]() Clone and initialisation
-------------------------

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

[]() Generate LHE files from gripacks
-------------------------

To send jobs starting from a gridpack that does not exist but that you have produced, do the following:
   - place gridpack on eos 
     - for FCC ```/eos/experiment/fcc/hh/generation/gridpacks/```
     - for HELHC ```/eos/experiment/fcc/helhc/generation/gridpacks/```
   - if the gridpack is from Madgraph, name it ```mg_process```, if from powheg please name it ```pw_process```,
   - add to ```param_FCC.py``` or ```param_HELHC.py``` an entry corresponding to the gridpack name in the ```gridpacklist``` list, depending on the study.

If the gridpack already exists or has been properly added to the ```param```, then simply run:

```
python bin/run.py --FCC/HELHC --LHE --send -p <process> -n <nevents> -N <njobs> --lsf -q 1nh
```

example to send 10 jobs of 10 000 events of di-electron events using 1nh queue of lsf for HELHC:

```
python bin/run.py --HELHC --LHE --send -p mg_pp_ee_lo -n 10000 -N 10 --lsf -q 1nh
```

example to send 10 jobs of 10 000 events of ttz using 8nh queue of lsf for HE-LHC:

```
python HELHC bin/sendJobs.py -n 10 -e 10000 -q 8nh -p pp_ttz_5f
```

[]() Generate FCCSW files from the LHE and decay with Pyhtia8
--------------------------
1. make sure decay is in ```decaylist``` and ```branching_ratios``` of ```param.py``` or ```param_HELHC.py```
2. create appropriate pythia8 card, by appending standard card with decay syntax if needed and add it to the proper directory, example:
```
/eos/experiment/fcc/hh/utils/pythiacards/pythia_pp_ttz_5f_znunu.cmd
```

3. Run jobs:


```
python bin/sendJobs_FCCSW.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName> -d <PythiaDecay>
```

Example produce 10 jobs of FCC Delphes events of ttz decaying the Z to neutrinos. :

```
python bin/sendJobs_FCCSW.py -n 10 -p pp_ttz_5f -d znunu -q 8nh -v fcc_v02
``` 

Please note that the decay in pythia is optional.

[]() Generate FCCSW files from Pythia8
--------------------------

Pythia8 manual: http://home.thep.lu.se/~torbjorn/pythia81html/Welcome.html

1) Define process in pythialist in config/param.py
2) Write Pythia8 process card and put it in: /eos/experiment/fcc/hh/utils/pythiacards/

ex: pythia_pp_Zprime_10TeV_ttbar.cmd

3) send jobs

python bin/sendJobs_FCCSW_P8.py -n 10 -e 10000 -p pp_Zprime_10TeV_ttbar -q 8nh -v fcc_v02


[]() Cleaning up
--------------------------

Scripts are used to check that the jobs have been properly processed.
For LHE
```
python common/jobchecker.py LHE
python common/cleanfailed.py LHE
```

For FCCSW events version 02
```
python common/jobchecker.py FCC_fcc_v02
python common/cleanfailed.py FCC_fcc_v02
```

