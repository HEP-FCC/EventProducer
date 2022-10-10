# Specific instructions for FCC-hh sample generation

## Autumn 2022

### Prerequisites & setting up 

To be able to use this framework, you need access rights to the dedicated `eos`-area. Check if you can access this path `/eos/experiment/fcc/hh/generation/` - if not, you need to request access (*to clarify who can grant access and what the procedure should be*). 

For running on condor (which currently seems to be the only viable option even for a tester, as running locally doesn't seem to be supported) it is also helpful to be a member of the `group_u_FCC.local_gen` group (*how to be added?*). 

Some fixes to the FCChh specific code needed to be implemented that are currently only available in this fork and not in the main repo, so to run the FCChh tester please clone this fork: 

``` git clone git@github.com:bistapf/EventProducer.git ```

and switch to the specific branch:

 ``` git checkout fcchh_evtgen_updates ``` 

 Once done, `source init.sh` for setting up the environment. 

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