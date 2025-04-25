#!/bin/bash
#unset LD_LIBRARY_PATH
#unset PYTHONHOME
#unset PYTHONPATH

# source /cvmfs/sft.cern.ch/lcg/views/LCG_89/x86_64-centos7-gcc7-opt/setup.sh 
# export LHAPDF_DATA_PATH=/afs/cern.ch/work/b/bistapf/lhapdf/LHAPDF-6.1.6/install/share/LHAPDF/

# source /afs/cern.ch/work/s/selvaggi/private/EventProducerHH/init.sh

SCRIPTFILE=${1}
PROCESSNAME=${2}
OUTPUTDIR=${3}
JOBID=${4}
NEVENTS=${5}
CUTFILE=${6}
MODELFILE=${7}

mkdir job
cd job

echo "copying madgraph tarball ..."
# cp  /eos/experiment/fcc/hh/utils/generators/MG5_aMC_v2.5.5.tar.gz .
cp  /eos/experiment/fcc/hh/utils/generators/MG5_aMC_v3.6.3pre.tar.gz .
echo "finished copying madgraph tarball version 3.6.3pre"
tar -xzf MG5_aMC_v3.6.3pre.tar.gz

echo "finished untaring madgraph tarball version 3.6.3pre"
cd MG5_aMC_v3.6.3pre

# parse script file
cp ${SCRIPTFILE} .

echo "Copying script file ${SCRIPTFILE}"
SCRIPT=$(basename $SCRIPTFILE)

SEED=$((10#$JOBID))


# replace dummyvalues
echo "Replacing dummy values"
sed -i -e "s/DUMMYSEED/${SEED}/g" ${SCRIPT}
sed -i -e "s/DUMMYNEVENTS/${NEVENTS}/g" ${SCRIPT}

# split into proc and run
echo "Splitting input config file..."
csplit --digits=2  --quiet --prefix=config ${SCRIPT} "/DELIMITER/+1" "{*}"

# add cuts.f if specified
if [ -f "${MODELFILE}" ]; then
    echo "Adding model tarball"
    cp ${MODELFILE} models
    echo $(basename $MODELFILE)
    tar -xzvf models/$(basename $MODELFILE)
    tar -xvf models/$(basename $MODELFILE)
else
    echo "model file not specified."
fi;

# create process
echo "Configuring process..."
./bin/mg5_aMC config00

# add cuts.f if specified
if [ -f "${CUTFILE}" ]; then
    echo "Adding cuts.f file"
    cp ${CUTFILE} DUMMYPROCESS/SubProcesses/cuts.f
else
    echo "cuts.f file not specified, using the default one"
fi;


# now run MG5 job
echo "Launching process..."
./bin/mg5_aMC config01

# copy output where specified
OUTDIR=${OUTPUTDIR}/${PROCESSNAME}
OUTFILE=${OUTDIR}/events_${JOBID}.lhe.gz

echo "Copying LHE file to ${OUTFILE}"
mkdir -p ${OUTDIR}

# check if this run is decayed or not
if [ -d "${PWD}/DUMMYPROCESS/Events/run_01_decayed_1" ]; then
  INFILE="${PWD}/DUMMYPROCESS/Events/run_01/unweighted_events.lhe.gz"
else
  INFILE="${PWD}/DUMMYPROCESS/Events/run_01_decayed_1/unweighted_events.lhe.gz"
fi

#source /cvmfs/sft.cern.ch/lcg/views/LCG_96/x86_64-centos7-gcc8-opt/setup.sh
xrdcp -N -v ${INFILE} root://eospublic.cern.ch/${OUTDIR}/events_${JOBID}.lhe.gz
