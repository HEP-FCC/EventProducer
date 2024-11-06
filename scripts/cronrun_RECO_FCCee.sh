PROD_TAG="${1}"
DETECTOR="${2}"

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_RECO_FCCee.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --checkeos
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --check
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --merge
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --clean
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --cleanold
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --merge
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --web
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --sample

mkdir -p "${EVENTPRODUCER}/log"
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
