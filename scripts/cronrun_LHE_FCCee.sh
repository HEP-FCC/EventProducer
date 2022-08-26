cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --LHE --checkeos
python bin/run.py --FCCee --LHE --check
python bin/run.py --FCCee --LHE --merge
python bin/run.py --FCCee --LHE --clean
python bin/run.py --FCCee --LHE --cleanold
python bin/run.py --FCCee --LHE --merge
python bin/run.py --FCCee --LHE --web

