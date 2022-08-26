cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --STDHEP --checkeos --version spring2021
python bin/run.py --FCCee --STDHEP --check --version spring2021
python bin/run.py --FCCee --STDHEP --merge --version spring2021
python bin/run.py --FCCee --STDHEP --clean --version spring2021
python bin/run.py --FCCee --STDHEP --cleanold --version spring2021
python bin/run.py --FCCee --STDHEP --merge --version spring2021
python bin/run.py --FCCee --STDHEP --web --version spring2021

