#!/bin/bash
unset LD_LIBRARY_PATH
unset PYTHONHOME
unset PYTHONPATH

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

source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc14-opt/setup.sh;

# Create a local fake f2py3.11 pointing to f2py
mkdir -p $PWD/f2py_bin
ln -sf $(dirname $(which python3))/f2py $PWD/f2py_bin/f2py3.11

# Prepend it to PATH
export PATH=$PWD/f2py_bin:$PATH

echo "python3 location: $(which python3)"
echo "python3 --version: $(python3 --version)"
echo "numpy version: $(python3 -c 'import numpy; print(numpy.__version__)')"
echo "f2py3.11 location: $(which f2py3.11)"
head -5 $(which f2py3.11)



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
echo "OUTDIR = ${OUTDIR}"
mkdir -p ${OUTDIR}

echo "Current working directory = ${PWD}"

# check if this run is decayed or not
if [ -d "${PWD}/DUMMYPROCESS/Events/run_01_decayed_1" ]; then
  echo "Found directory: ${PWD}/DUMMYPROCESS/Events/run_01_decayed_1"
  echo "Using MadSpin decayed events"
  INFILE="${PWD}/DUMMYPROCESS/Events/run_01_decayed_1/unweighted_events.lhe.gz"
else
  echo "Did NOT find directory: ${PWD}/DUMMYPROCESS/Events/run_01_decayed_1"
  echo "Using standard events"
  INFILE="${PWD}/DUMMYPROCESS/Events/run_01/unweighted_events.lhe.gz"
fi

echo "Input file path = ${INFILE}"

if [ -f "${INFILE}" ]; then
  echo "Input file exists, ready to copy."
else
  echo "ERROR: Input file does not exist!"
  echo "Listing Events directory for debug:"
  ls -lh ${PWD}/DUMMYPROCESS/Events/
  echo "Listing inside run_01_decayed_1 if exists:"
  ls -lh ${PWD}/DUMMYPROCESS/Events/run_01_decayed_1 || echo "run_01_decayed_1 not found"
  echo "Listing inside run_01:"
  ls -lh ${PWD}/DUMMYPROCESS/Events/run_01 || echo "run_01 not found"
  exit 1
fi

# Copy file
echo "Running xrdcp command:"
echo "xrdcp -N -v ${INFILE} root://eospublic.cern.ch/${OUTDIR}/events_${JOBID}.lhe.gz"
xrdcp -N -v ${INFILE} root://eospublic.cern.ch/${OUTDIR}/events_${JOBID}.lhe.gz
