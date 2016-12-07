# LHEventProducer

To send jobs starting from a gridpack, do the following:
   - place gridpack in eos '''/eos/fcc/hh/generation/mg5_amcatnlo/gridpacks'''
   - add to '''param.py''' the job name corresponding to the gridpack name

Then simply run:

'''
python sendJobs.py -n <NumberOfJobs> -e <NumberOfEventsPerJob> -q <BatchQueueName> -p <ProcessName>
'''

example:

'''
python sendJobs.py -n 1 -e 200 -q 1nh -p pp_hh_bbaa
'''


