# this bash script load pythia8 environmentfrom LCG and compile pythia8 macro that computes cross sections

#export PYTHIA8_XML=/cvmfs/sft.cern.ch/lcg/releases/MCGenerators/pythia8/230-6eb2a/x86_64-mac1012-clang90-opt/share/Pythia8/xmldoc/
#export PYTHIA8DATA=$PYTHIA8_XML
#source /cvmfs/sft.cern.ch/lcg/releases/LCG_92/gcc/7.2.0/x86_64-slc6/setup.sh

g++ py8crossSection.cc -o py8crossSection.exe -I/cvmfs/sft.cern.ch/lcg/views/LCG_94/x86_64-centos7-gcc62-opt/include/ -L/cvmfs/sft.cern.ch/lcg/views/LCG_94/x86_64-centos7-gcc62-opt/lib/ -Wl,-rpath,/cvmfs/sft.cern.ch/lcg/views/LCG_96/x86_64-centos7-gcc62-opt/lib/ -lpythia8;

