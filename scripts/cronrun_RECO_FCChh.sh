cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCChh --reco --checkeos --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --check --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --merge --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --clean --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --cleanold --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --merge --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --web --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --sample --prodtag "${1}" --detector "" > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "Last run finished: `date`" > ${EVENTPRODUCER}/log/cronrun_RECO_FCChh.log
