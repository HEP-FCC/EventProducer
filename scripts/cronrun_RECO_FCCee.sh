cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --checkeos > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --check > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --merge > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --clean > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --cleanold > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --merge > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --web > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --sample > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "Last run finished: `date`" > ${EVENTPRODUCER}/log/cronrun_RECO_FCCee.log
