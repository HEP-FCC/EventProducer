# Specific instructions for FCC-hh sample generation

## Autumn 2022 (updated Spring 2023) 

### Prerequisites & setting up 

To be able to use this framework, you need access rights to the dedicated `eos`-area. Check if you can access this path `/eos/experiment/fcc/hh/generation/` - if not, you need to request access (*to clarify who can grant access and what the procedure should be*). 

For running on condor (which currently seems to be the only viable option even for a tester, as running locally doesn't seem to be supported) it is also helpful to be a member of the `group_u_FCC.local_gen` group (*how to be added?*). 

Some fixes to the FCChh specific code needed to be implemented that are currently only available in this fork and not in the main repo, so to run the FCChh tester please clone this fork: 

``` git clone git@github.com:bistapf/EventProducer.git ```

and switch to the specific branch:

 ``` git checkout fcchh_evtgen_updates ``` 

 Once done, `source init.sh` for setting up the environment. 
 
### Producing edm4hep events from existing LHE files with `DelphesPythia8_EDM4HEP`

You can see which LHE events are available in this `\eos\` area: `/eos/experiment/fcc/hh/generation/lhe/`. To run existing LHE events through Pythia+Delphes and store the output in edm4hep format, follow these steps: 

0. If you have never used this framework to generate events before, you must add yourself to the list of users in `config/users.py`.

1. Make sure the that `config/param_FCChh.py` is correctly setup for the process you want to run, i.e. : The version of the production must be listed in the `prodTag` directory, specifying how the software stack is setup. For the Spring 23 production, we will use `fcc_v05_scenarioI`. 
Then, you must be sure that in `/eos/experiment/fcc/hh/utils/delphescards/` a directory with the name of your version exists, which contains the Delphes card you want to use and all parametrization files it uses - their names are given in the `delphescard_base, delphescard_mr, delphescard_mmr, delphescard_emr` variables in the config file. Again, for `fcc_v05_scenarioI` this is already setup using the [scenario I Delphes card](https://github.com/bistapf/delphes/blob/master/cards/FCC/scenarios/FCChh_I.tcl).  
Last `pythialist` or `decaylist` must contain the name of your process/LHE file (*to be clarified which is the correct approach*). For example, for the di-Higgs signals (with k_l = 1) the name of LHE is `pw_pp_hh_lambda100_5f` - the Higgses are not decayed there yet. This step is done in Pythia, with DelphesPythia8_EDM4HEP, using the cards from `/eos/experiment/fcc/hh/utils/pythiacards/`. Currently, cards for bbaa, bbtata, bbZZ (inc.), bbZZ (Z-leptonic = 4l, llvv + 4v), bbZZ (4l), bbWW (inc.) and 4b exist and are ready to be used. If you want to add new decay, place the Pythia card in the eos area and make sure to add is name to the `decaylist`. 

2. Finally, jobs to produce events using `DelphesPythia8_EDM4HEP` are submitted by calling: 
```python bin/run.py --FCChh --reco --send  -p <LHE_process_name> --type lhep8 --decay <decay_name> --pycard <pythia_card> -N <number_of_jobs> --condor -q <queue_name> --detector "" --prodtag <version>```. 

Here, `number_of_jobs` determines how many events we produce - 1 job processes one LHE file, which commonly has 1k events. So 100 jobs will produce 1 million events. 

For example, to produce 500k pp->HH->4b events from the existing HH LHE, we run: 
```python bin/run.py --FCChh --reco --send  -p pw_pp_hh_lambda100_5f --type lhep8 --decay hhbbbb --pycard pwp8_pp_hh_5f_hhbbbb.cmd -N 50 --condor  -q workday --detector "" --prodtag fcc_v05_scenarioI```

Optionally we can add: --customEDM4HEPOutput <path_to_config_file>` to this command, in case we want to store more collections in the edm4hep output than in the common setup. For example, the electrons/muons/photons before/after isolation and overlap removal. A file to use for this setup comes with this repo, it's called `edm4hep_output_config.tcl` (in the top level). 

3. Monitor the jobs on condor. Their logs will be written into `EventProducer/BatchOutputs`. 

4. If all works well (and you didn't change it in the config file), the output files will be written to `/eos/experiment/fcc/hh/generation/DelphesEvents/<version>/<process_name>`. 

*To-Do: Instructions for merging files, managing and cleaning up, fixing the database`. 

### How to run LHE production with the new HH signal gridpacks 

If you have a gridpack for the event generation, you can produce LHE events from it in the following steps: 

0. If you have never used this framework to generate events before, you must add yourself to the list of users in `config/users.py`. (*why is this necessary and are there any restrictions here?*)

1. Copy your gridpack to the FCChh gridpack eos directory `/eos/experiment/fcc/hh/generation/gridpacks/`. For this example we will use the tester gridpack called `mg_pp_vbf_hh_angela.tar.gz`, which is for VBF HH signal with C2V = 2 (and CV = kl = 1 ?). 

2. Add the name of your gridpack to the `gridpacklist` in `config/param_FCChh.py`. For `mg_pp_vbf_hh_angela` this is already done, if you are working on the `fcchh_evtgen_updates` branch. 

3. Run the event generation from your gridpack with the following command:

``` python bin/run.py --FCChh --LHE --send --condor --typelhe gp_mg -p mg_pp_vbf_hh_angela --prodtag fcc_v04 -n 10 -N 1 -q longlunch --detector "" ``` 

This will submit 1 job to generate 10 events from the testergridpack to condor. The logs of this job will be found in `./BatchOutputs/FCC/lhe/mg_pp_vbf_hh_angela` and the output Les Houches files will be in `/eos/experiment/fcc/hh/generation/lhe/mg_pp_vbf_hh_angela`. 

### To-do before proper production:
- Build and copy to the `eos`-area all the gridpacks for the new signals *(maybe add instructions on how to do this somewhere here too?)*
- Give correct names to the gridpacks (i.e. the full process names)
- Add the gridpacks to the param_FCChh properly (i.e. with description, cross-section, etc?)
- The arguments `prodtag` and `detector` are currently placeholders as they are required from the FCC-ee production. Should be adapted for FCC-hh production. 
- Fix/update the FCChh LHE database


#testing setup for delphesizing:
DelphesPythia8_EDM4HEP /eos/user/b/bistapf/new_FCChh_cards/FCChh_I.tcl /afs/cern.ch/work/h/helsens/public/k4SimDelphes_PythiaStuff/examples/edm4hep_output_config.tcl ./pythia_config/tester_pwp8_pp_hh_5f_hhbbww.cmd /eos/user/b/bistapf/FCChh_EvtGen/pwp8_pp_hh_5f_hhbbWW_tester_new_card.root
