cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCChh --reco --checkeos --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --check --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --merge --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --clean --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --cleanold --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --merge --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --web --prodtag $1 --detector ""
python bin/run.py --FCChh --reco --sample --prodtag $1 --detector ""


