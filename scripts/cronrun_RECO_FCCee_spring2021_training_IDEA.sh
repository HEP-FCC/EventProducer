cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --checkeos
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --check
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --merge
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --clean
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --cleanold
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --merge
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --web
python bin/run.py --FCCee --reco --version spring2021_training --detector IDEA --sample
