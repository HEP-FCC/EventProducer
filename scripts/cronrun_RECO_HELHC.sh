cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --HELHC --reco --checkeos --version helhc_v01
python bin/run.py --HELHC --reco --check --version helhc_v01
python bin/run.py --HELHC --reco --merge --version helhc_v01
python bin/run.py --HELHC --reco --clean --version helhc_v01
python bin/run.py --HELHC --reco --cleanold --version helhc_v01
python bin/run.py --HELHC --reco --merge --version helhc_v01
python bin/run.py --HELHC --reco --web --version helhc_v01
#python bin/run.py --HELHC --reco --sample --version helhc_v01

