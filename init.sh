#source /cvmfs/sw.hsf.org/spackages2/key4hep-stack/2021-04-30/x86_64-centos7-gcc8.3.0-opt/t5gcd6ltt2ikybap2ndoztsg5uyorxzg/setup.sh
source /cvmfs/sw.hsf.org/key4hep/setup.sh
#source /cvmfs/sw.hsf.org/spackages2/key4hep-stack/2021-05-12/x86_64-centos7-gcc8.3.0-opt/iyafnfo5muwvpbxcoa4ygwoxi2smkkwa/setup.sh
#spack load --first k4simdelphes build_type=Release ^evtgen+photos

export EOS_MGM_URL="root://eospublic.cern.ch"
export EVENTPRODUCER=$PWD
export PYTHONPATH=$PWD/..:$PYTHONPATH

mkdir -p "${EVENTPRODUCER}/log"
