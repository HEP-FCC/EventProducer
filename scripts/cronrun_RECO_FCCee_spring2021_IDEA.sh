cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --checkeos
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --check
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --merge
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --clean
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --cleanold
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --merge
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --web
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA --sample
