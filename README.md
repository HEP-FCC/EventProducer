# EventProducer

[]() Clone and initialisation
-------------------------

If you do not attempt to contribute to the repository, simply clone it:
```
git clone git@github.com:clementhelsens/EventProducer.git
```

If you aim at contributing to the repository, you need to fork and then clone the forked repository:
```
git clone git@github.com:YOURGITUSERNAME/EventProducer.git
```

Then initialise:
```
source ./init.sh
```

[]() Generate LHE files
-------------------------

To send jobs starting from a gridpack, do the following:
   - place gridpack in eos ```/eos/fcc/hh/generation/mg5_amcatnlo/gridpacks```
   - add to ```param.py``` the job name corresponding to the gridpack name

Then simply run:

```
python sendJobs.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName>
```

example:

```
python sendJobs.py -n 1 -e 200 -q 1nh -p pp_hh_bbaa
```

[]() Generate FCCSW files 
--------------------------

First you need to export your FCCSW path (this is where you installed FCCSW):

```
export FCCUSERPATH=<UserFccPath>
```

Check dictionary (optional):

```
python jobchecker.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json
python cleanfailed.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json
python jobchecker.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json
python cleanfailed.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json
```

Run jobs:

```
python sendJobs_FCCSW.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName> -i <PythiaCard>
```

Example:

```
python sendJobs_FCCSW.py -i $FCCUSERPATH/Generation/data/Pythia_LHEinput.cmd -n 1 -e 200 -q 1nh -p pp_hh_bbaa --test
``` 

-
