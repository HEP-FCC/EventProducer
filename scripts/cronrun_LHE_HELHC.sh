cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --HELHC --LHE --checkeos
python bin/run.py --HELHC --LHE --check
python bin/run.py --HELHC --LHE --merge
python bin/run.py --HELHC --LHE --clean
python bin/run.py --HELHC --LHE --cleanold
python bin/run.py --HELHC --LHE --merge
python bin/run.py --HELHC --LHE --web
