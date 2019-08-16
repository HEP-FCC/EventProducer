cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --checkeos --version fcc_v01
python bin/run.py --FCCee --reco --check --version fcc_v01
python bin/run.py --FCCee --reco --merge --version fcc_v01
python bin/run.py --FCCee --reco --clean --version fcc_v01
python bin/run.py --FCCee --reco --cleanold --version fcc_v01
python bin/run.py --FCCee --reco --merge --version fcc_v01
python bin/run.py --FCCee --reco --web --version fcc_v01
python bin/run.py --FCCee --reco --sample --version fcc_v01


