#!/bin/bash

PROD_TAG="${1}"
DETECTOR="${2}"
set --

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit 3

source init.sh

find "${EVENTPRODUCER}/log" -type f \
                            -name "cronrun_RECO_FCChh_${PROD_TAG}_${DETECTOR}_*.log" \
                            -mtime +7 -exec rm {} \;
LOGFILE="${EVENTPRODUCER}/log/cronrun_RECO_FCChh_${PROD_TAG}_${DETECTOR}_$(date +'%d-%m-%Y-%H-%M').log"
echo "$(date)  INFO: Cron run started." > "${LOGFILE}"

# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${EVENTPRODUCER}/.sync.lock" ]; then
  echo "$(date)  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCChh --reco --checkeos --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --check --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --merge --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --clean --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --cleanold --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --merge --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --web --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCChh --reco --sample --prodtag "${PROD_TAG}" --detector "${DETECTOR}" >> "${LOGFILE}" || exit 3

echo "$(date)  INFO: Cron run finished." >> "${LOGFILE}"
