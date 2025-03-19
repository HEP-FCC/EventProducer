#!/bin/bash

PROD_TAG="${1}"
set --

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit 3

source init.sh

find "${EVENTPRODUCER}/log" -type f \
                            -name "cronrun_STDHEP_FCCee_${PROD_TAG}_*.log" \
                            -mtime +7 -exec rm {} \;
LOGFILE="${EVENTPRODUCER}/log/cronrun_STDHEP_FCCee_${PROD_TAG}_$(date +'%d-%m-%Y-%H-%M').log"
echo "$(date)  INFO: Cron run started." > "${LOGFILE}"

# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${EVENTPRODUCER}/.sync.lock" ]; then
  echo "$(date)  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --STDHEP --checkeos --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --check --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --merge --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --clean --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --cleanold --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --merge --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3
python bin/run.py --FCCee --STDHEP --web --prodtag "${PROD_TAG}" >> "${LOGFILE}" || exit 3

echo "$(date)  INFO: Cron run finished." >> "${LOGFILE}"
