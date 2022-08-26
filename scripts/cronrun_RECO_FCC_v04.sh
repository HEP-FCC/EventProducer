cd /afs/cern.ch/user/h/helsens/FCCsoft/Generators/EventProducer/
source ./init.sh

python bin/run.py --FCC --reco --checkeos --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --check --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --merge --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --clean --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --cleanold --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --merge --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --web --version fcc_v04 --detector ""
python bin/run.py --FCC --reco --sample --version fcc_v04 --detector ""


