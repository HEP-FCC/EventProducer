source /cvmfs/sft.cern.ch/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/Python-env.sh
source /cvmfs/sft.cern.ch/lcg/releases/LCG_87/ROOT/6.08.02/x86_64-slc6-gcc49-opt/ROOT-env.sh
source /afs/cern.ch/user/h/helsens/eosfcc.sh
cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python common/jobchecker.py LHE
python common/cleanfailed.py LHE

python common/jobchecker.py FCC
python common/cleanfailed.py FCC

python common/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json /afs/cern.ch/user/h/helsens/www/LHEevents.txt
python common/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json /afs/cern.ch/user/h/helsens/www/Delphesevents.txt

python common/makeSampleList.py  /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json