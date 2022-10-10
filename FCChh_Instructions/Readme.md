# Specific instructions for FCC-hh sample generation

## Autumn 2022

### Prerequisites & setting up 

To be able to use this framework, you need access rights to the dedicated eos area. Check if you can access this path `/eos/experiment/fcc/hh/generation/` - if not, you need to request access (*to clarify who can grant access and what the procedure should be*). 

Some fixes to the FCChh specific code needed to be implemented, that are currently only available in this fork and not in the main repo, so to run please clone this fork: 

``` git clone git@github.com:bistapf/EventProducer.git ```

and switch to the specific branch:

 ``` git checkout fcchh_evtgen_updates ``` 

### How to run LHE production with the new HH signal gridpacks 
