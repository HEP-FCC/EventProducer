cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh
LOGFILE="${EVENTPRODUCER}/log/cronrun_LHE_FCCee.log"
echo "" > "${LOGFILE}"

SYNCLOCK="${EVENTPRODUCER}/.sync.lock"
# Making sure the last sync went OK and there is no .sync.lock file left
if [ -f "${SYNCLOCK}" ]; then
  echo "`date`  WARNING: Encountered git sync lock. Aborting..." >> "${LOGFILE}"

  exit 3
fi

python bin/run.py --FCCee --LHE --checkeos > /dev/null
python bin/run.py --FCCee --LHE --check > /dev/null
python bin/run.py --FCCee --LHE --merge > /dev/null
python bin/run.py --FCCee --LHE --clean > /dev/null
python bin/run.py --FCCee --LHE --cleanold > /dev/null
python bin/run.py --FCCee --LHE --merge > /dev/null
python bin/run.py --FCCee --LHE --web > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "`date`  INFO: Cron run finished." >> "${LOGFILE}"
