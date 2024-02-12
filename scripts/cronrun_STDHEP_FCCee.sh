PROD_TAG="${1}"

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_STDHEP_FCCee.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --STDHEP --checkeos --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --check --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --clean --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --cleanold --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --merge --prodtag "${PROD_TAG}" > /dev/null
python bin/run.py --FCCee --STDHEP --web --prodtag "${PROD_TAG}" > /dev/null

mkdir -p "${EVENTPRODUCER}/log"
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
