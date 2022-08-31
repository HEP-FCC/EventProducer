cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCChh --LHE --checkeos
python bin/run.py --FCChh --LHE --check
python bin/run.py --FCChh --LHE --merge
python bin/run.py --FCChh --LHE --clean
python bin/run.py --FCChh --LHE --cleanold
python bin/run.py --FCChh --LHE --merge
python bin/run.py --FCChh --LHE --web

