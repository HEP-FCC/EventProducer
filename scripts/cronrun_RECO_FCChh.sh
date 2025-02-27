PROD_TAG="${1}"
DETECTOR="${2}"
set --

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit 1

source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_RECO_FCChh_${PROD_TAG}_${DETECTOR}.log"
echo "`date`  INFO: Cron run started." > "${LOGFILE}"

# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${EVENTPRODUCER}/.sync.lock" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCChh --reco --checkeos --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --check --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --merge --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --clean --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --cleanold --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --merge --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --web --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --reco --sample --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 1

mkdir -p "${EVENTPRODUCER}/log"
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
