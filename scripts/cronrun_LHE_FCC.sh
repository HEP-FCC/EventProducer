cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCC --LHE --checkeos
python bin/run.py --FCC --LHE --check
python bin/run.py --FCC --LHE --merge
python bin/run.py --FCC --LHE --clean
python bin/run.py --FCC --LHE --cleanold
python bin/run.py --FCC --LHE --merge
python bin/run.py --FCC --LHE --web

