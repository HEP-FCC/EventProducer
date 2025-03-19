#!/bin/bash

PROD_TAG="${1}"
DETECTOR="${2}"
set --

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit 3

source init.sh

find "${EVENTPRODUCER}/log" -type f \
                            -name "cronrun_RECO_FCCee_${PROD_TAG}_${DETECTOR}_*.log" \
                            -mtime +7 -exec rm {} \;
LOGFILE="${EVENTPRODUCER}/log/cronrun_RECO_FCCee_${PROD_TAG}_${DETECTOR}_$(date +'%d-%m-%Y-%H-%M').log"
echo "$(date)  INFO: Cron run started." > "${LOGFILE}"

# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${EVENTPRODUCER}/.sync.lock" ]; then
  echo "$(date)  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --checkeos >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --check >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --merge >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --clean >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --cleanold >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --merge >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --web >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --reco --prodtag "${PROD_TAG}" --detector "${DETECTOR}" --sample >> "${LOGFILE}" || exit 3

echo "$(date)  INFO: Cron run finished." >> "${LOGFILE}"
