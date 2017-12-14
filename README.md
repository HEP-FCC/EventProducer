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
python bin/sendJobs.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName>
```

example:

```
python bin/sendJobs.py -n 10 -e 10000 -q 8nh -p pp_ttz_5f
```

[]() Generate FCCSW files 
--------------------------

First you need to export your FCCSW path (this is where you installed FCCSW):

```
export FCCUSERPATH=<UserFccPath>
```

Check dictionary (optional):

```
python common/jobchecker.py LHE
python common/cleanfailed.py LHE

```

Run jobs:

```
python bin/sendJobs_FCCSW.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName> -i <PythiaCard>
```

Example:

```
python bin/sendJobs_FCCSW.py -i $FCCUSERPATH/Generation/data/Pythia_LHEinput.cmd -n 1 -e 200 -q 1nh -p pp_hh_bbaa --test
``` 

-
