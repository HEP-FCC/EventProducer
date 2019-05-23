#source /cvmfs/fcc.cern.ch/sw/0.8.2/init_fcc_stack.sh
source /cvmfs/fcc.cern.ch/sw/views/releases/externals/94.0.0/x86_64-slc6-gcc62-opt/setup.sh

#source /cvmfs/fcc.cern.ch/testing/sw/views/stable/x86_64-slc6-gcc62-opt/setup.sh
export EOS_MGM_URL="root://eospublic.cern.ch"
export EVENTPRODUCER=$PWD
export PYTHONPATH=$PWD/..:$PYTHONPATH

