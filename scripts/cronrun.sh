source /cvmfs/sft.cern.ch/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/Python-env.sh
source /afs/cern.ch/user/h/helsens/eosfcc.sh
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/jobchecker.py LHE
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/cleanfailed.py LHE

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/jobchecker.py FCC
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/cleanfailed.py FCC

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json /afs/cern.ch/user/h/helsens/www/LHEevents.txt
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json /afs/cern.ch/user/h/helsens/www/Delphesevents.txt

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/common/makeSampleList.py  /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json