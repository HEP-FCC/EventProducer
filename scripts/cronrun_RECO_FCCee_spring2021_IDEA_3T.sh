cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --checkeos
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --check
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --merge
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --clean
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --cleanold
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --merge
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --web
python bin/run.py --FCCee --reco --version spring2021 --detector IDEA_3T --sample
