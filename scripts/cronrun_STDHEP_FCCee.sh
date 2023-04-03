cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCCee --STDHEP --checkeos --prodtag spring2021
python bin/run.py --FCCee --STDHEP --check --prodtag spring2021
python bin/run.py --FCCee --STDHEP --merge --prodtag spring2021
python bin/run.py --FCCee --STDHEP --clean --prodtag spring2021
python bin/run.py --FCCee --STDHEP --cleanold --prodtag spring2021
python bin/run.py --FCCee --STDHEP --merge --prodtag spring2021
python bin/run.py --FCCee --STDHEP --web --prodtag spring2021

