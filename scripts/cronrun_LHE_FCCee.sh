cd /afs/cern.ch/user/f/fccsw/private/EventProducer/
source ./init.sh

python bin/run.py --FCCee --LHE --checkeos > /dev/null
python bin/run.py --FCCee --LHE --check > /dev/null
python bin/run.py --FCCee --LHE --merge > /dev/null
python bin/run.py --FCCee --LHE --clean > /dev/null
python bin/run.py --FCCee --LHE --cleanold > /dev/null
python bin/run.py --FCCee --LHE --merge > /dev/null
python bin/run.py --FCCee --LHE --web > /dev/null

mkdir -p ${EVENTPRODUCER}/log
echo "Last run finished: `date`" > ${EVENTPRODUCER}/log/cronrun_LHE_FCCee.log
