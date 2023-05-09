cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_STDHEP_FCCee.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --STDHEP --checkeos --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --check --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --clean --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --cleanold --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${1}" > /dev/null
python bin/run.py --FCCee --STDHEP --web --prodtag "${1}" > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
