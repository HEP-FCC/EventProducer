#!/usr/bin/env bash
unset LD_LIBRARY_PATH
unset PYTHONHOME
unset PYTHONPATH

source /cvmfs/sft.cern.ch/lcg/releases/LCG_88/gcc/4.9.3/x86_64-slc6/setup.sh
source /cvmfs/sft.cern.ch/lcg/releases/LCG_88/Python/2.7.13/x86_64-slc6-gcc49-opt/Python-env.sh
source /cvmfs/sft.cern.ch/lcg/releases/LCG_88/ROOT/6.08.06/x86_64-slc6-gcc49-opt/bin/thisroot.sh
export PYTHIA8=/afs/cern.ch/work/s/selvaggi/private/pythia8226

SCRIPTFILE=${1}
PROCESSNAME=${2}
OUTPUTDIR=${3}
SEED=${4}
NEVENTS=${5}
CUTFILE=${6}
MODELFILE=${7}

mkdir job
cd job

cp -r /eos/experiment/fcc/hh/utils/generators/MG5_aMC_v2.6.1.tar.gz .
tar -xzvf MG5_aMC_v2.6.1.tar.gz
cd MG5_aMC_v2_6_1

# parse script file
cp ${SCRIPTFILE} .
SCRIPT=$(basename $SCRIPTFILE)

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
    cp ${CUTFILE} outdir/SubProcesses/cuts.f
else
    echo "cuts.f file not specified, using the default one"
fi;


# now run MG5 job
echo "Launching process..."
./bin/mg5_aMC config01

# copy output where specified
OUTDIR=${OUTPUTDIR}/${PROCESSNAME}
OUTFILE=${OUTDIR}/events_${SEED}.lhe.gz

echo "Copying LHE file to ${OUTFILE}"
mkdir -p ${OUTDIR}
cp -r DUMMYPROCESS/Events/run_01/unweighted_events.lhe.gz ${OUTDIR}/events_${SEED}.lhe.gz
