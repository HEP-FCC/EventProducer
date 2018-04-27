import os

cardini = 'p8_pp_Zprime'
cardend= 'TeV_ll.cmd'

masses = dict()
masses[27] = [1,2,4,6, 8, 10, 12, 14, 16]
masses[100] =  [2,5,10,15,20,25,30,35,40]

outdir_local = dict()
outdir_local[27] = '27TeV'
outdir_local[100] = '100TeV'

outdir_eos = dict()
outdir_eos[27] = '/eos/experiment/fcc/helhc/utils/pythiacards'
outdir_eos[100] = '/eos/experiment/fcc/hh/utils/pythiacards'

dummycard="""
Random:setSeed = on
Main:numberOfEvents = 1000         ! number of events to generate
Main:timesAllowErrors = 5          ! how many aborts before run stops

! 2) Settings related to output in init(), next() and stat().
Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 100             ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

Beams:idA = 2212                   ! first beam, p = 2212, pbar = -2212
Beams:idB = 2212                   ! second beam, p = 2212, pbar = -2212

! 4) Hard process : ttbar pair production at 100TeV
Beams:eCM = DUMMYECM  ! CM energy of collision

NewGaugeBoson:ffbar2gmZZprime = on
Zprime:gmZmode = 3
Zprime:universality = on                     // Sets couplings the same/different for generations of quarks

32:onMode = off
32:onIfAny = 15 13 11
32:m0 = DUMMYMASS

! write down parameters for Zprime model: DUMMYMODEL
Zprime:vd   = DUMMY_VD
Zprime:ad   = DUMMY_AD
Zprime:vu   = DUMMY_VU
Zprime:au   = DUMMY_AU
Zprime:ve   = DUMMY_VE
Zprime:ae   = DUMMY_AE
Zprime:vnue = DUMMY_VNUE
Zprime:anue = DUMMY_ANUE
"""

models = dict()

models['SSM'] = [-0.6933333333e+00, -0.1000000000e+01, 0.3866666667e+00, 0.1000000000e+01, -0.8000000000e-01, -0.1000000000e+01, 0.1000000000e+01, 0.1000000000e+01] 
models['LRM'] = [-0.4717535801e+00, 0.3674234614e+00, 0.2630933427e+00, -0.3674234614e+00, -0.5443310540e-01, 0.3674234614e+00, 0.1564951780e+00, 0.1564951780e+00]  
models['PSI'] = [0.0000000000e+00, 0.5055250296e+00, 0.0000000000e+00, 0.5055250296e+00, 0.0000000000e+00, 0.5055250296e+00, 0.2527625148e+00, 0.2527625148e+00]     
models['CHI'] = [-0.7831560083e+00, 0.3915780041e+00, 0.0000000000e+00, -0.3915780041e+00, 0.7831560083e+00, 0.3915780041e+00, 0.5873670062e+00, 0.5873670062e+00]   
models['ETA'] = [0.4795831523e+00, 0.1598610508e+00, 0.0000000000e+00, 0.6394442031e+00, -0.4795831523e+00, 0.1598610508e+00, -0.1598610508e+00, -0.1598610508e+00]  
models['I']   = [-0.6191391874e+00, 0.6191391874e+00, 0.0000000000e+00, -0.3910519505e-12, 0.6191391874e+00, 0.6191391874e+00, 0.6191391874e+00, 0.6191391874e+00]   

for ecm in [27, 100]:

    if not os.path.exists(outdir_local[ecm]):
          os.makedirs(outdir_local[ecm])

    for mass in masses[ecm]:

        for name, values in models.iteritems():

        
            newcard = dummycard
            newcard = newcard.replace('DUMMYECM', str(ecm*1000))
            newcard = newcard.replace('DUMMYMASS', str(mass*1000))
            
            newcard = newcard.replace('DUMMYMODEL', name)
            newcard = newcard.replace('DUMMY_VD', str(values[0]))
            newcard = newcard.replace('DUMMY_AD', str(values[1]))
            newcard = newcard.replace('DUMMY_VU', str(values[2]))
            newcard = newcard.replace('DUMMY_AU', str(values[3]))
            newcard = newcard.replace('DUMMY_VE', str(values[4]))
            newcard = newcard.replace('DUMMY_AE', str(values[5]))
            newcard = newcard.replace('DUMMY_VNUE', str(values[6]))
            newcard = newcard.replace('DUMMY_ANUE', str(values[7]))

            cardloc = cardini+name+'_'+str(mass)+cardend
            card = outdir_local[ecm] + '/'+ cardloc

            with open(card, "w") as f:
              f.write(newcard)

            dest = outdir_eos[ecm]+ '/'+ cardloc
            cmd = 'eos cp --streams=1000 {} root://eospublic.cern.ch/{}'.format(card, dest)
            print cmd
	    #os.system(cmd)
