cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --checkeos
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --check
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --merge
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --clean
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --cleanold
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --merge
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --web
python bin/run.py --FCCee --reco --prodtag $1 --detector $2 --sample
