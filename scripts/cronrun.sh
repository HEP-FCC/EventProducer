source /afs/cern.ch/user/h/helsens/eosfcc.sh
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/jobchecker.py LHE
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/cleanfailed.py LHE

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/jobchecker.py FCC
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/cleanfailed.py FCC

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/LHEdict.json /afs/cern.ch/user/h/helsens/www/LHEevents.txt
python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/printdicts.py /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json /afs/cern.ch/user/h/helsens/www/Delphesevents.txt

python /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/makeSampleList.py  /afs/cern.ch/work/h/helsens/public/FCCDicts/PythiaDelphesdict_v0_0.json