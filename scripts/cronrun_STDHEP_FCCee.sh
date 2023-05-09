cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCCee --STDHEP --checkeos --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --check --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --clean --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --cleanold --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --web --prodtag "${1}" > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "Last run finished: `date`" > ${EVENTPRODUCER}/log/cronrun_STDHEP_FCCee.log
