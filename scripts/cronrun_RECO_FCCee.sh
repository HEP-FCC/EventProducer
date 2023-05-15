cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_RECO_FCCee.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --checkeos > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --check > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --merge > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --clean > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --cleanold > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --merge > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --web > /dev/null
python bin/run.py --FCCee --reco --prodtag "${1}" --detector "${2}" --sample > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
