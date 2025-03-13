#!/bin/bash

set --

cd /afs/cern.ch/user/f/fccsw/private/EventProducer/ || exit 1

source ./init.sh

find "${EVENTPRODUCER}/log" -type f \
	                    -name "cronrun_LHE_FCChh_*.log" \
			    -mtime +7 -exec rm {} \;
LOGFILE="${EVENTPRODUCER}/log/cronrun_LHE_FCChh_$(date +'%d-%m-%Y-%H-%M').log"
echo "`date`  INFO: Cron run started." > "${LOGFILE}"

# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${EVENTPRODUCER}/.sync.lock" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCChh --LHE --checkeos >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --check >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --merge >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --clean >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --cleanold >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --merge >> "${LOGFILE}" || exit 1
python bin/run.py --FCChh --LHE --web >> "${LOGFILE}" || exit 1

echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
