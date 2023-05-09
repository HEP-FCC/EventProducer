cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_STDHEP_FCChh.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCChh --reco --checkeos --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --check --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --merge --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --clean --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --cleanold --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --merge --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --web --prodtag "${1}" --detector "" > /dev/null
python bin/run.py --FCChh --reco --sample --prodtag "${1}" --detector "" > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
