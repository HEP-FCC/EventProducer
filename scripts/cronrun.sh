cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh


python bin/run.py --HELHC --LHE --check
python bin/run.py --HELHC --LHE --merge
python bin/run.py --HELHC --LHE --checkeos
python bin/run.py --HELHC --LHE --clean
python bin/run.py --HELHC --LHE --merge
python bin/run.py --HELHC --LHE --web


python bin/run.py --HELHC --reco --check --version helhc_v01
python bin/run.py --HELHC --reco --merge --version helhc_v01
python bin/run.py --HELHC --reco --clean --version helhc_v01
python bin/run.py --HELHC --reco --checkeos --version helhc_v01
python bin/run.py --HELHC --reco --merge --version helhc_v01
python bin/run.py --HELHC --reco --web --version helhc_v01
python bin/run.py --HELHC --reco --sample --version helhc_v01


python bin/run.py --FCC --LHE --check
python bin/run.py --FCC --LHE --merge
python bin/run.py --FCC --LHE --checkeos
python bin/run.py --FCC --LHE --clean
python bin/run.py --FCC --LHE --merge
python bin/run.py --FCC --LHE --web


python bin/run.py --FCC --reco --check --version fcc_v02
python bin/run.py --FCC --reco --merge --version fcc_v02
python bin/run.py --FCC --reco --checkeos --version fcc_v02
python bin/run.py --FCC --reco --clean --version fcc_v02
#python bin/run.py --FCC --reco --cleanold --version fcc_v02
python bin/run.py --FCC --reco --merge --version fcc_v02
python bin/run.py --FCC --reco --web --version fcc_v02
#python bin/run.py --FCC --reco --sample --version fcc_v02
