source /cvmfs/sft.cern.ch/lcg/releases/LCG_87/Python/2.7.10/x86_64-slc6-gcc49-opt/Python-env.sh
source /cvmfs/sft.cern.ch/lcg/releases/LCG_87/ROOT/6.08.02/x86_64-slc6-gcc49-opt/ROOT-env.sh
source /afs/cern.ch/user/h/helsens/eosfcc.sh
cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python common/jobchecker.py LHE
python common/cleanfailed.py LHE

python common/jobchecker.py FCC_fcc_v01
python common/cleanfailed.py FCC_fcc_v01

python common/jobchecker.py FCC_fcc_v02
python common/cleanfailed.py FCC_fcc_v02


python common/jobchecker.py FCC_cms
python common/cleanfailed.py FCC_cms

python common/baddone.py  LHE

python common/printdicts.py LHE /afs/cern.ch/user/h/helsens/www/LHEevents.txt
python common/printdicts.py FCC_fcc_v01 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v01.txt
python common/printdicts.py FCC_fcc_v02 /afs/cern.ch/user/h/helsens/www/Delphesevents_fcc_v02.txt
python common/printdicts.py FCC_cms /afs/cern.ch/user/h/helsens/www/Delphesevents_cms.txt

python common/makeSampleList.py fcc_v01
python common/makeSampleList.py cms

