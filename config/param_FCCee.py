#module
module_name='config/param_FCCee.py'
#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#directories
webbasedir="/eos/experiment/fcc/www/data/FCCee/"
pubbasedir="/afs/cern.ch/work/f/fccsw/public/FCCDicts/"
eosbaseinputdir="/eos/experiment/fcc/ee/generation/"
eosbaseoutputdir="/eos/experiment/fcc/ee/generation/"

#stat
lhe_stat = webbasedir + "statlhe.html"
delphes_stat = webbasedir + "statdelphesVERSION_DETECTOR.html"
stdhep_stat = webbasedir + "stat_stdhep_VERSION.html"

#web
lhe_web = webbasedir + "LHEevents.txt"
delphes_web = webbasedir + "Delphesevents_VERSION_DETECTOR.txt"
stdhep_web = webbasedir + "STDHEP_events_VERSION.txt"

#yaml directory
yamldir      = pubbasedir+"yaml/FCCee/"

#proc lists
procList     = [pubbasedir+"FCCee_procDict_VERSION_DETECTOR.json",
                webbasedir+"FCCee_procDict_VERSION_DETECTOR.json"]

##eos directory for MG5@MCatNLO gridpacks
gp_dir       = eosbaseinputdir+"gridpacks/"

##eos directory for lhe files
lhe_dir      = eosbaseoutputdir+"lhe/"

##extension
lhe_ext      = ".lhe.gz"

##eos directory for stdhep files
stdhep_dir   = eosbaseoutputdir+"/stdhep/"

##extension
stdhep_ext   = ".stdhep.gz"

##FCC-ee production version and corresponding SW tag
prodTag = {
    'spring2021':'/cvmfs/sw.hsf.org/spackages2/key4hep-stack/2021-05-12/x86_64-centos7-gcc8.3.0-opt/iyafnfo5muwvpbxcoa4ygwoxi2smkkwa/setup.sh',
    'spring2021_training':'/cvmfs/sw.hsf.org/spackages2/key4hep-stack/2021-05-12/x86_64-centos7-gcc8.3.0-opt/iyafnfo5muwvpbxcoa4ygwoxi2smkkwa/setup.sh',
    'dev':'/cvmfs/sw.hsf.org/key4hep/setup.sh' ,
    'pre_fall2022':'/cvmfs/fcc.cern.ch/sw/latest/setup.sh',
    'pre_fall2022_training':'/cvmfs/fcc.cern.ch/sw/latest/setup.sh',
    'winter2023':'/cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh',
    'winter2023_training':'/cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh',
}

defaultstack='/cvmfs/fcc.cern.ch/sw/latest/setup.sh'


##eos directory for FCCSW pythia delphes files
delphes_dir  = eosbaseoutputdir+"DelphesEvents/"
##extension
delphes_ext  = ".root"
##name of the ttree
treename     = "events"


##where the delphes cards are stored
delphescards_dir = eosbaseinputdir+"FCC-config/_VERSION_/FCCee/Delphes/"
##where the pythia cards are stored
pythiacards_dir  = eosbaseinputdir+"FCC-config/_VERSION_/FCCee/Generator/Pythia8/"
##where the EVTGEN card are stored
evtgencards_dir  = eosbaseinputdir+"FCC-config/_VERSION_/FCCee/Generator/EvtGen/"
##where the WHIZARD cards are stored
whizardcards_dir = eosbaseinputdir+"FCC-config/_VERSION_/FCCee/Generator/Whizard/"
##where the KKMC cards are stored
kkmccards_dir = eosbaseinputdir+"FCC-config/_VERSION_/FCCee/Generator/KKMC/"
# /cvmfs/fcc.cern.ch/sw/latest/setup.sh 
##delphes base card detector
#detectors = ['IDEA', 'IDEA_3T', 'IDEA_FullSilicon']
detectors = ['IDEA', 'IDEA_3T', 'IDEA_SiTracking']


#list of processes only with Pythia, meaning no LHE
pythialist={
    'dummy':['<p style=\"background-color:Tomato;\">NOT REGISTERED IN param_FCCee</p>','<p style=\"background-color:Tomato;\">NOT REGISTERED IN param_FCCee</p>','','-9999','-9999','-9999'],

    'p8_ee_ZH_Znunu_Hgg_ecm240':['ZH ecm=240GeV','Z->nunu, H->gg','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Hbb_ecm240':['ZH ecm=240GeV','Z->nunu, H->bb','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Hcc_ecm240':['ZH ecm=240GeV','Z->nunu, H->cc','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Hss_ecm240':['ZH ecm=240GeV','Z->nunu, H->ss','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Hdd_ecm240':['ZH ecm=240GeV','Z->nunu, H->dd','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Huu_ecm240':['ZH ecm=240GeV','Z->nunu, H->uu','','0.201868','1.0','1.0'],             #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZH_Znunu_Htautau_ecm240':['ZH ecm=240GeV','Z->nunu, H->tautau','','0.201868','1.0','1.0'],     #    Pythia 8.303, noBES (Used 0.201037 before)

    'p8_ee_ZH_ecm240':['ZH ecm=240GeV','inclusive decays','','0.201868','1.0','1.0'],       #    Pythia 8.303, noBES (Used 0.201037 before)
    'p8_ee_ZZ_ecm240':['ZZ ecm=240GeV','inclusive decays','','1.35899','1.0','1.0'],
    'p8_ee_WW_ecm240':['WW ecm=240GeV','inclusive decays','','16.4385','1.0','1.0'],
    'p8_ee_Zqq_ecm240':['Z/Gamma* ecm=240GeV','hadronic decays','','52.6539','1.0','1.0'],  # Pythia 8.303, noBES (was 53.188 before spring2021)
    'p8_ee_Zll_ecm240':['Z/Gamma* ecm=240GeV','leptonic decays (e/mu/tau)','','13.7787','1.0','1.0'],  # Pythia 8.303, noBES 

    'p8_ee_ZH_mH-higher-100MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.201316','1.0','1.0'],  	# Pythia 8.303, noBES
    'p8_ee_ZH_mH-higher-50MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.201673','1.0','1.0'],		# Pythia 8.303, noBES
    'p8_ee_ZH_mH-lower-50MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.202169','1.0','1.0'],		# Pythia 8.303, noBES
    'p8_ee_ZH_mH-lower-100MeV_ecm240':['ZH ecm=240GeV, vary mH','inclusive decays','','0.20253','1.0','1.0'],		# Pythia 8.303, noBES

    'p8_ee_ZZ_Zll_ecm240':['ZZ ecm=240GeV','Z to e, mu, tau','','0.027','1.0','1.0'], 

    'p8_ee_WW_mumu_ecm240':['WW ecm=240GeV','W->mu and W ->tau->mu','','0.25792','1.0','1.0'],
    'p8_noBES_ee_WW_mumu_ecm240':['WW ecm=240GeV','W->mu and W ->tau->mu','','0.25792','1.0','1.0'],

    'p8_ee_WW_ee_ecm240':['WW ecm=240GeV','W->e and W ->tau->e','','0.25792','1.0','1.0'],

    'p8_noBES_ee_ZH_ecm240':['ZH ecm=240GeV, no BES','inclusive decays','','0.201037','1.0','1.0'],
    'p8_noBES_ee_ZZ_ecm240':['ZZ ecm=240GeV, no BES','inclusive decays','','1.35899','1.0','1.0'],
    'p8_noBES_ee_WW_ecm240':['WW ecm=240GeV, no BES','inclusive decays','','16.4385','1.0','1.0'],

    'p8_ee_ZH_ecm365':['ZH ecm=365GeV','inclusive decays','','0.1173','1.0','1.0'],
    'p8_ee_ZZ_ecm365':['ZZ ecm=365GeV','inclusive decays','','0.6428','1.0','1.0'],
    'p8_ee_WW_ecm365':['WW ecm=365GeV','inclusive decays','','10.7165','1.0','1.0'],
    'p8_ee_tt_ecm365':['tt ecm=365GeV','inclusive decays','','0.800','1.0','1.0'],

    'p8_ee_WW_mumu_ecm365':['WW ecm=365GeV','W->mu and W ->tau->mu','','0.1785','1.0','1.0'],
    'p8_ee_Zqq_ecm365':['Z/Gamma* ecm=365GeV','hadronic decays','','21.4149','1.0','1.0'],  

    'p8_ee_tt_fullhad_ecm365':['tt ecm=365GeV','hadronic decays','','0.363528','1.0','1.0'],
    'p8_ee_ZZ_fullhad_ecm365':['ZZ ecm=365GeV','hadronic decays','','0.31417','1.0','1.0'],
    'p8_ee_WW_fullhad_ecm365':['WW ecm=365GeV','hadronic decays','','4.86969','1.0','1.0'],

    'p8_ee_ZH2_mH2-200GeV_ecm365':['Z BSM Higgs ecm=365GeV', 'inclusive decays', '', '1.0', '1.0', '1.0'],

    'p8_ee_H_Hbb_ecm125':['H ecm=125GeV','Higgs to bb','','0.000164','1.0','1.0'],
    'p8_ee_H_Hgg_ecm125':['H ecm=125GeV','Higgs to gluon','','0.000023','1.0','1.0'],
    'p8_ee_H_Hcc_ecm125':['H ecm=125GeV','Higgs to cc','','0.000008','1.0','1.0'],
    'p8_ee_H_Htautau_ecm125':['H ecm=125GeV','Higgs to tau','','0.0000065','1.0','1.0'],
    'p8_noBES_ee_H_Hbb_ecm125':['H ecm=125GeV','Higgs to bb','','0.000164','1.0','1.0'],
    'p8_noBES_ee_H_Hgg_ecm125':['H ecm=125GeV','Higgs to gluon','','0.000023','1.0','1.0'],
    'p8_noBES_ee_H_Hcc_ecm125':['H ecm=125GeV','Higgs to cc','','0.000008','1.0','1.0'],
    'p8_noBES_ee_H_Htautau_ecm125':['H ecm=125GeV','Higgs to tau','','0.0000065','1.0','1.0'],
    
    'p8_ee_Z_Zbb_ecm125':['bb ecm=125GeV','bb','','81.','1.0','1.0'],
    'p8_ee_Z_Zcc_ecm125':['cc ecm=125GeV','cc','','73.','1.0','1.0'],
    'p8_ee_Z_Zqq_ecm125':['qq ecm=125GeV','qq','','237.','1.0','1.0'],
    'p8_ee_Z_Ztautau_ecm125':['tautau ecm=125GeV','tautau','','26.','1.0','1.0'],
    'p8_ee_ZZ_ecm125':['ZZ ecm=125GeV','inclusive','','1.','0.','1.0'],
    'p8_ee_WW_ecm125':['WW ecm=125GeV','inclusive','','0.0558','1.0','1.0'],

    # ttbar threshold scan
    'p8_ee_WW_ecm340':['WW ecm=340GeV','inclusive decays','','12.056','1.0','1.0'],
    'p8_ee_WW_ecm345':['WW ecm=345GeV','inclusive decays','','11.899','1.0','1.0'],
    'p8_ee_WW_ecm350':['WW ecm=350GeV','inclusive decays','','11.715','1.0','1.0'],
    'p8_ee_WW_ecm355':['WW ecm=355GeV','inclusive decays','','11.527','1.0','1.0'],


#once we have Z -> bb
#we need a factor of 7.9e-5 for Bc production
#then a factor 0.0236 for Bc -> tau nu BF
#then 0.098 for tau -> 3π nu

    
    'p8_ee_Zbb_ecm91':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays','','6645.46','1.0','1.0'],     # win2023: 6600.53
    'p8_ee_Zbb_DIRAC_ecm91':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays','','6645.46','1.0','1.0'],     # win2023: 6600.53
    'p8_ee_Zcc_ecm91':['Z/Gamma* ecm=91.188GeV to cc','inclusive decays','','5215.46','1.0','1.0'],     # win2023: 5184.19
    'p8_ee_Zuds_ecm91':['Z/Gamma* ecm=91.188GeV to uds','inclusive decays','','18616.5','1.0','1.0'],
    'p8_ee_Zss_ecm91':['Z/Gamma* ecm=91.188GeV to ss','','','5215.46','1.0','1.0'],
    'p8_ee_Zud_ecm91':['Z/Gamma* ecm=91.188GeV to uu and dd','','','11870.5','1.0','1.0'],

    'p8_ee_Zbb_noFSR_ecm91':['Z/Gamma* ecm=91.188GeV to bb','for test, no gluon radiation','','6645.46','1.0','1.0'],     # win2023: 6600.53

    'p8_ee_Ztautau_ecm91':['Z/Gamma* ecm=91.188GeV to tautau','inclusive decays','','1476.58','1.0','1.0'],    
    'p8_ee_Zee_ecm91':['Z/Gamma* ecm=91.188GeV','Z decays to ee','','1462.09','1.0','1.0'],
    'p8_ee_Zmumu_ecm91':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],
    'p8_ee_Zmumu_ecm88':['Z/Gamma* ecm=87.8 GeV','Z decays to mumu','','197.0','1.0','1.0'],
    'p8_ee_Zmumu_ecm94':['Z/Gamma* ecm=94.3 GeV','Z decays to mumu','','386.0','1.0','1.0'],


    'p8_ee_Zbb_ecm91_EvtGen':['Z/Gamma* ecm=91.188GeV to bb','inclusive decays using EvtGen','','6645.46','1.0','1.0'],
    
    'p8_ee_Zcc_ecm91_EvtGen_Dd2K3Pi':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Dd2TauNu':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Dd2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Ds2EtapRho':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Ds2TauNu':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Ds2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Lc2LENu':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Lc2LMuNu':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Lc2LRhoPi':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_Lc2Sigma2Pi':['Z/Gamma* ecm=91.188GeV to cc','EvtGen to be filled','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2DENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0ENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0ENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstENu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstMuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsMuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2EE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2MuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2NuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiMuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2KEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2KMuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2KTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LMuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen to be filled','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0Pi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+/- -> D0(KPi)Pi','','1.3290920','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstTauTauTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) tau+ tau-, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2D0PiPi':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> D0 p+ p-','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2MuMu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> mu mu','','3.029000668e-07','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D*- -> (D0b -> K+ pi-) pi-) tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D*- -> (D0b -> K+ pi-) pi-) tau+ nu, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D- -> K+ pi- pi-) tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (D- -> K+ pi- pi-) tau+ nu, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstEE':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) e+ e-','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_BdKstNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (K*0 -> K- pi+) nu nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsPi0':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B0 -> (Ks0 -> pi pi) pi0','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiGamma':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> (phi -> K+ K-) gamma','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2TauTau':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> tau+ tau-, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2TauTauTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs0 -> tau+ tau-, tau -> 3pi nu TAUHADNU model','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi nu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi nu TAUHADNU model','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTau23PiPi0NuTAUOLA':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> 3pi pi0 nu TAUOLA model','','0.01','1.0','1.0'],#0.0931 for the tau decay, it is 0.0462
    'p8_ee_Zbb_ecm91_EvtGen_Bc2MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> mu+ nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931                                         
    'p8_ee_Zbb_ecm91_EvtGen_Bc2TauNuTau2MuNuNuPHOTOSTAULNUNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bc+ -> tau+ nu, tau -> mu nu nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931   
    'p8_ee_Zbb_ecm91_EvtGen_Bu2MuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> mu+ nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931                                         
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTau2MuNuNuPHOTOSTAULNUNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> tau+ nu, tau -> mu nu nu','','0.011680911114880002','1.0','1.0'],#6645.46*2*0.0004*0.0236*0.0931   


    #'p8_ee_Zbb_ecm91_EvtGen_Bs2DsK':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs+ -> D*K','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTAUHADNU':['Z/Gamma* ecm=91.188GeV to bb','EvtGen B+ -> tau+ nu, tau -> 3pi nu TAUHADNU model','','0.05799621863924','1.0','1.0'],#6645.46*2*0.43*0.000109*0.0931
    'p8_ee_Zbb_ecm91_EvtGen_Bu2TauNuTau23PiPi0NuTAUOLA':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu+ -> tau+ nu, tau -> 3pi pi0 nu TAUOLA model','','0.01','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_BuCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bu cocktail','','877.26717','1.0','1.0'],#6645.46*0.13201
    'p8_ee_Zbb_ecm91_EvtGen_BdCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bd cocktail','','691.52657','1.0','1.0'],#6645.46*0.10406
    'p8_ee_Zbb_ecm91_EvtGen_BsCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Bs cocktail','','155.02529','1.0','1.0'],#6645.46*0.023328
    'p8_ee_Zbb_ecm91_EvtGen_LbCocktail':['Z/Gamma* ecm=91.188GeV to bb','Bc2TaNu Lb cocktail','','75.485780','1.0','1.0'],#6645.46*0.011359


    'p8_ee_Zbb_ecm91_EvtGen_Bd2Kstee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Kstee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsteeBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KsteeBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2Kstmm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Kstmm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstmmBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KstmmBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2Rhomm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Rhomm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Rhoee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2Rhoee','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Kstee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2Kstee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2KsteeBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2KsteeBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Kstmm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2Kstmm','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2KstmmBTOSLLBALL':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2KstmmBTOSLLBALL','','1.0','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bu2Piee':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2Piee','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Pimm':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2Pimm','','1.0','1.0','1.0'],


    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bd2KstNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bs2PhiNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2KNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Bu2KNuNu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LNuNu':['Z/Gamma* ecm=91.188GeV to bb','EvtGen Lb2LNuNu','','1.0','1.0','1.0'],
    
    'p8_ee_Zbb_ecm91_EvtGen_Bd2D3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bd2D3Pi','','17.1452868','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DDs'     :['Z/Gamma* ecm=91.188GeV to bb','Bd2DDs','','20.57434416','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bd2DTauNu','','30.861516240000004','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Dst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bd2Dst3Pi','','20.602919638','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Bd2DstDs','','22.8603824','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Bd2DstDsst','','50.57859606','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Bd2DstTauNu','','44.86350046','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2Ds3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bs2Ds3Pi','','3.891581376','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsDs'     :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsDs','','2.8070423040000003','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsTauNu','','15.502529088000001','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bs2Dsst3Pi','','4.5997215936','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstD','','8.867701824','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstDsst','','9.186683904','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Bs2DsstTauNu','','10.335019392','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bu2D03Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Bu2D03Pi','','16.00226768','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0Ds'     :['Z/Gamma* ecm=91.188GeV to bb','Bu2D0Ds','','25.717930199999998','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2D0TauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Bu2D0TauNu','','22.003118060000002','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst03Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Bu2Dsst3Pi','','29.43274234','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0Ds'   :['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstD','','21.71736328','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0Dsst' :['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstDsst','','48.86406738','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bu2Dst0TauNu':['Z/Gamma* ecm=91.188GeV to bb','Bu2DsstTauNu','','53.721898640000006','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Lb2Lc3Pi'    :['Z/Gamma* ecm=91.188GeV to bb','Lb2Ds3Pi','','1.893291554','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcDs'     :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsDs','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcTauNu'  :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsTauNu','','8.040342054','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Lcst3Pi'  :['Z/Gamma* ecm=91.188GeV to bb','Lb2Dsst3Pi','','1.893291554','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstDs'   :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstD','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstDsst' :['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstDsst','','2.7047022199999997','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2LcstTauNu':['Z/Gamma* ecm=91.188GeV to bb','Lb2DsstTauNu','','8.040342054','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bs2JpsiPhi':['Z/Gamma* ecm=91.188GeV to bb','Bs to JPsi(mumu) Phi(KK)','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2KstarTauTau':['Z/Gamma* ecm=91.188GeV to bb','B to K* tautau decay, with  taus decaying into 3 pions','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> (Ds+ ->  pi+  pi+  pi-  pi0) (Ds- -> pi-  pi-  pi+  pi0) (K*0 -> K+ pi-)','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2Taunu':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0v2':['Z/Gamma* ecm=91.188GeV to bb','B0 -> (Ds+ -> (eta0 ->  pi+  pi-  pi0 / omega0 -> pi+  pi-  pi0) pi+) (Ds+ -> (eta0 ->  pi-  pi+  pi0 / omega0 -> pi-  pi+  pi0) pi-) (K*0 -> K+ pi-)','','1','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu or 3pi1pi0','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0pi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to pipipipipi0','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2pipipipi0pi0v2':['Z/Gamma* ecm=91.188GeV to bb','B0 -> (Ds+ ->  (eta0 / omega0 -> pi+ pi- pi0) pi+ pi0) (Ds- -> (eta0 / omega0 -> pi+ pi- pi0)  pi- pi0) (K*0 -> K+ pi-)','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsKstarTauNuDs2TauNu':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds K*0 tau nu, K*0 forced to K+ pi-, Ds forced to tau nu','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0v2':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds Ds K*0, K*0 forced to K+ pi-, Ds+ forced to tau nu, Ds- forced to omega/eta pi-','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0v2ChargeConjugation':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds Ds K*0, K*0 forced to K+ pi-, Ds- forced to tau nu, Ds+ forced to omega/eta pi+','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsstarDsKstarDs2TaunuDsstar2Dsgamma':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds*+ Ds- K*0, K*0 forced to K+ pi-, Ds forced to tau nu, D*s+ forced in Ds gamma','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0pi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds+ forced to tau nu, Ds- forced to multi pions','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsDsKstarDs2TaunuDs2pipipipi0pi0ChargeConjugation':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds+ Ds- K*0, K*0 forced to K+ pi-, Ds- forced to tau nu, Ds+ forced to multi pions','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsstarDsKstarDs2PiPiPiPi0Pi0Dsstar2Dsgamma':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds*+ Ds- K*0, K*0 forced to K+ pi-, Ds*+ forced to Ds+ and gamma, and both Ds+ and Ds- forced to multi pions','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsstarKstarTauNuDs2pipipipi0pi0':['Z/Gamma* ecm=91.188GeV to bb','B0 -> Ds*+ tau- K*0, K*0 forced to K+ pi-, Ds* forced to Ds gamma, and Ds forced to multi pions','','1','1.0','1.0'],
#Bu = 0.307 * 0.43 = 0.13201
#Bd = 0.242 * 0.43 = 0.10406
#Bs = 0.243 * 0.096 = 0.023328
#Lb = 0.307 * 0.037 = 0.011359
    'p8_ee_Zbb_ecm91_EvtGen_Bd2DsK':['Z/Gamma* ecm=91.188GeV to bb','B0 to Ds K, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2Dsstarpi':['Z/Gamma* ecm=91.188GeV to bb','B0 to Ds* pi, Ds* to gamma Phi pi or gamma Phi rho','','4.52e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsK':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds K, Ds to Phi pi or Phi rho','','13.23e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsKtest':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds K, Ds to Phi pi or Phi rho','','13.23e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsKstar':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds K*, Ds to Phi pi or Phi rho, K* to K pi0','','6.52e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dspi':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds pi, Ds to Phi pi or Phi rho','','176e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsrho':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds rho, Ds to Phi pi','','200e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2DsstarK':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds* K, Ds* to gamma Phi pi or gamma Phi rho','','8.248e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2Dsstarpi':['Z/Gamma* ecm=91.188GeV to bb','Bs to Ds* pi, Ds* to gamma Phi pi or gamma Phi rho','','105e-3','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Dsp':['Z/Gamma* ecm=91.188GeV to bb','Lambda0 to Ds p, Ds to Phi pi or Phi rho','','1','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Lb2Dsstarp':['Z/Gamma* ecm=91.188GeV to bb','Lambda0 to Ds* p, Ds* to gamma Phi pi or gamma Phi rho','','1','1.0','1.0'],

    'p8_ee_Ztautau_ecm91_EvtGen_Tau2MuMuMu':['Z/Gamma* ecm=91.188GeV to tautau','EvtGen tau -> 3mu','','1.0','1.0','1.0'],    
    'p8_ee_Ztautau_ecm91_EvtGen_Tau2MuGamma':['Z/Gamma* ecm=91.188GeV to tautau','EvtGen tau -> mu gamma','','1.0','1.0','1.0'],
    'p8_ee_Zcc_ecm91_EvtGen_D2PiPi0':['Z/Gamma* ecm=91.188GeV to cc','EvtGen D+ -> pi+ pi0','','1.0','1.0','1.0'],


    'p8_noBES_ee_Ztautau_ecm91_EvtGen_TauMinus2MuMuMu':['Z/Gamma* ecm=91.188GeV to tautau', 'tau- -> 3mu, sig for BR=2e-8','','29.5e-6','1.0','1.0'],
    'p8_noBES_ee_Ztautau_ecm91_EvtGen_TauMinus2PiPiPinu':['Z/Gamma* ecm=91.188GeV to tautau', 'tau- -> 3pi nu','','137.3','1.0','1.0'],

    'p8_ee_Zbb_ecm91_EvtGen_Bd2KsNuNu':['Z/Gamma* ecm=91.188GeV to bb', 'Bd to Ks nunu','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiKs':['Z/Gamma* ecm=91.188GeV to bb','Bs to Phi(KK) Ks(pi+pi-)','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2PhiKs':['Z/Gamma* ecm=91.188GeV to bb','Bd to Phi(KK) Ks(pi+pi-)','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2PhiPhi':['Z/Gamma* ecm=91.188GeV to bb','Bs to Phi(KK) Phi(KK)','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bs2KstarKstar':['Z/Gamma* ecm=91.188GeV to bb','Bs to Kstar(Kpi) Kstar(Kpi)','','1.0','1.0','1.0'],
    'p8_ee_Zbb_ecm91_EvtGen_Bd2rhoKstar':['Z/Gamma* ecm=91.188GeV to bb','Bd to rho(pipi) Kstar(Kpi)','','1.0','1.0','1.0'],


}



##list of possible decays of LHE files
decaylist = {

}

##list of decays branching ratios 
# from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR 
# and Particle data Group
branching_ratios = {
'hmumu':2.176E-04,
'haa':2.270E-03,
'hlla':1.533E-03*(3.363E-02 + 3.366E-02),
'hllll':1.240E-04,
'hlvlv':1.055E-02,
'hbb':5.824E-01,
'htautau':6.272E-02,
'zll':0.307,
'ztautau':0.03367,
'zbb':0.152,
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
'wzlllv':0.03333,


}


##Gridpack list
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
    'dummy': ['<span style="background-color:tomato;">NOT REGISTERED IN param_FCCee</span>',
              '<span style="background-color:tomato;">NOT REGISTERED IN param_FCCee</span>', '',
              '-9999', '-9999', '-9999'],
    'mg_ee_tt_ecm350':['tt','tt inclusive','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tH_ecm365':['tt','tt inclusive','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tcz_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tua_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tua_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tuz_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tuz_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tca_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tca_ecm365':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tbw_FCNC_tcz_ecm240':['single top FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tca_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tua_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tuz_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    'mg_ee_tt_FCNC_tcz_ecm365':['ttbar FCNC','to be added','','1.0','1.0','1.0'],
    # added on March 16, 2023 :
    'mg_ee_tq_fullhad_FCNC_tuz_ecm240':['single top FCNC','full hadronic','','1.0','1.0','1.0'],
    'mg_ee_tq_fullhad_FCNC_tua_ecm240':['single top FCNC','full hadronic','','1.0','1.0','1.0'],
    'mg_ee_tq_fullhad_FCNC_tua_ecm365':['single top FCNC','full hadronic','','1.0','1.0','1.0'],
    'mg_ee_tq_fullhad_FCNC_tuz_ecm365':['single top FCNC','full hadronic','','1.0','1.0','1.0'],

    'mg_ee_zhh_ecm365':['e+e- -> ZHH', 'LO', '', '2.0e-5', '1.0', '1.0'],
    'mg_ee_zh_ecm240':['e+e- -> ZH', '', '', '1.0', '1.0', '1.0'],
    'mg_ee_bb_ecm90':['e+e- -> bb', '', '', '1.0', '1.0', '1.0'],
    'mg_ee_cc_ecm90':['e+e- -> cc', '', '', '1.0', '1.0', '1.0'],
    'mg_ee_qq_ecm90':['e+e- -> qq', '', '', '1.0', '1.0', '1.0'],
    'mg_ee_ss_ecm90':['e+e- -> ss', '', '', '1.0', '1.0', '1.0'],

    'wzp6_ee_mumuH_ecm240':['mumuH ecm=240 GeV','inclusive Higgs decays','','6.7643e-3','1.0','1.0'],
    'wzp6_ee_mumuH_noISR_ecm240':['mumuH ecm=240 GeV, no ISR','inclusive Higgs decays','','7.9757e-3','1.0','1.0'],
    'wzp6_ee_mumuH_ISRnoRecoil_ecm240':['mumuH ecm=240 GeV, ISR  pT=0','inclusive Higgs decays','','6.7223e-3','1.0','1.0'],
    'wzp6_noBES_ee_mumuH_ecm240':['mumuH ecm=240 GeV','inclusive Higgs decays','','6.7626e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-higher-100MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7393e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-higher-50MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7488e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-lower-50MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7738e-3','1.0','1.0'],
    'wzp6_ee_mumuH_mH-lower-100MeV_ecm240':['mumuH ecm=240 GeV, vary mH','inclusive Higgs decays','','6.7849e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-6pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76052e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-6pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76602e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-1pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76140e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-1pc_ecm240':['mumuH ecm=240 GeV, vary BES','inclusive Higgs decays','','6.76093e-3','1.0','1.0'],
    'wzp6_ee_mumuH_noFSR_ecm240':['mumuH ecm=240 GeV, no FSR','inclusive Higgs decays','','6.7602e-3','1.0','1.0'],


    'wzp6_ee_tautauH_ecm240':['tautauH ecm=240 GeV','inclusive Higgs decays','','6.7518e-3','1.0','1.0'],
    'wzp6_ee_eeH_ecm240':['eeH ecm=240 GeV','inclusive Higgs decays','','7.1611e-3','1.0','1.0'],
    'wzp6_ee_eeH_mH-higher-100MeV_ecm240':['eeH ecm=240 GeV, vary mH','inclusive Higgs decays','','7.137e-3','1.0','1.0'],
    'wzp6_ee_eeH_mH-higher-50MeV_ecm240':['eeH ecm=240 GeV, vary mH','inclusive Higgs decays','','7.152e-3','1.0','1.0'],
    'wzp6_ee_eeH_mH-lower-50MeV_ecm240':['eeH ecm=240 GeV, vary mH','inclusive Higgs decays','','7.169e-3','1.0','1.0'],
    'wzp6_ee_eeH_mH-lower-100MeV_ecm240':['eeH ecm=240 GeV, vary mH','inclusive Higgs decays','','7.188e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-higher-1pc_ecm240':['eeH ecm=240 GeV, vary BES','inclusive Higgs decays','','7.159e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-lower-1pc_ecm240':['eeH ecm=240 GeV, vary BES','inclusive Higgs decays','','7.169e-3','1.0','1.0'],

    'wzp6_ee_nunuH_ecm240':['nunuH ecm=240 GeV (all nu flavours)','inclusive Higgs decays','','46.191e-3','1.0','1.0'],
    'wzp6_ee_qqH_ecm240':['qqH ecm=240 GeV, q = u,d,s,c,b','inclusive Higgs decays','','136.35e-3','1.0','1.0'],

    'wzp6_egamma_eZ_Zee_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to ee','','5.198e-2','1.0','1.0'],
    'wzp6_gammae_eZ_Zee_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to ee','','5.198e-2','1.0','1.0'],
    'wzp6_egamma_eZ_Zmumu_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to mumu','','103.68e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zmumu_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to mumu','','103.68e-3','1.0','1.0'],
    'wzp6_egamma_eZ_Zbb_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to bb','','455.7e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zbb_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to bb','','455.7e-3','1.0','1.0'],
    'wzp6_egamma_eZ_Zqq_ecm240':['e(e)Z EPA, e- gamma, ecm=240 GeV','Z to qq, q=udsc','','1.6369','1.0','1.0'],
    'wzp6_gammae_eZ_Zqq_ecm240':['e(e)Z EPA, e+ gamma, ecm=240 GeV','Z to qq, q=udsc','','1.6369','1.0','1.0'],
    'wzp6_egamma_tbnu_ecm240':['nu_e t b (e) EPA, e- gamma, ecm=240 GeV','inc. top decays','','1.0753e-5','1.0','1.0'],
    'wzp6_gammae_tbnu_ecm240':['nu_e t b (e) EPA, e+ gamma, ecm=240 GeV','inc. top decays','','1.0753e-5','1.0','1.0'],


    'wzp6_gaga_ee_60_ecm240':['gammagamma to ee, M(ee) > 60 GeV,  ecm=240 GeV','','','8.730e-1','1.0','1.0'],
    'wzp6_gaga_mumu_60_ecm240':['gammagamma to mumu, M(mumu) > 60 GeV,  ecm=240 GeV','','','1.5523','1.0','1.0'],
    'wzp6_gaga_tautau_60_ecm240':['gammagamma to tautau, M(tautau) > 60 GeV,  ecm=240 GeV','','','0.836','1.0','1.0'],
   
    'wzp6_ee_mumu_ecm240':['Z/gamma* to mumu, ecm=240 GeV','full phase space','','5.288','1.0','1.0'],
    'wzp6_ee_mumu_noFSR_ecm240':['Z/gamma* to mumu, ecm=240 GeV, no FSR','full phase space','','5.301','1.0','1.0'],

    'wzp6_ee_tautau_ecm240':['Z/gamma* to tautau, ecm=240 GeV','full phase space','','4.668','1.0','1.0'],
    'wzp6_ee_ee_Mee_30_150_ecm240':['ee (s and t), ecm=240 GeV','30 < Mee < 150 GeV, 15 < theta < 165 deg','','8.305','1.0','1.0'],

    'kkmc_ee_mumu_ecm240':['Z/gamma* to mumu, ecm=240 GeV','full phase space','','5.24619','1.0','1.0'],
    'kkmc_ee_mumu_noFSR_ecm240':['Z/gamma* to mumu, ecm=240 GeV, no FSR','full phase space','','5.77305','1.0','1.0'],

    'wzp6_ee_gammagamma_ecm91':['diphoton production','|cos(theta)| < 0.95 for the two leading photons','','45.454','1.0','1.0'],

    'wzp6_ee_ZZ_test_ecm240':['ZZ ecm=240 GeV','inclusive Z decays by Pythia','','1.11','1.0','1.0'],

    'wzp6_ee_nuenueZ_ecm240':['Z nue nuebar, W-exchange only','inclusive Z decays by Pythia','','3.3274e-2','1.0','1.0'],

# for Higgs, sqrts = 365 GeV:
    'wzp6_ee_mumuH_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-10pc_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-10pc_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-higher-1pc_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_mumuH_BES-lower-1pc_ecm365':['mumuH ecm=365 GeV','inclusive Higgs decays','','4.185e-3','1.0','1.0'],
    'wzp6_ee_tautauH_ecm365':['tautauH ecm=365 GeV','inclusive Higgs decays','','4.172e-3','1.0','1.0'],
    'wzp6_ee_eeH_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-higher-10pc_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-lower-10pc_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-higher-1pc_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_eeH_BES-lower-1pc_ecm365':['eeH ecm=365 GeV','inclusive Higgs decays','','7.390e-3','1.0','1.0'],
    'wzp6_ee_nunuH_ecm365':['nunuH ecm=365 GeV (all nu flavours)','inclusive Higgs decays','','53.94e-3','1.0','1.0'],
    'wzp6_ee_qqH_ecm365':['qqH ecm=365 GeV, q = u,d,s,c,b','inclusive Higgs decays','','84.307e-3','1.0','1.0'],

    'wzp6_egamma_eZ_Zmumu_ecm365':['e(e)Z EPA, e- gamma, ecm=365 GeV','Z to mumu','','140.0e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zmumu_ecm365':['e(e)Z EPA, e+ gamma, ecm=365 GeV','Z to mumu','','140.0e-3','1.0','1.0'],

    'wzp6_gaga_mumu_60_ecm365':['gammagamma to mumu, M(mumu) > 60 GeV,  ecm=365 GeV','','','2.843','1.0','1.0'],
    'wzp6_gaga_tautau_60_ecm365':['gammagamma to tautau, M(tautau) > 60 GeV,  ecm=365 GeV','','','1.537','1.0','1.0'],

    'wzp6_ee_mumu_ecm365':['Z/gamma* to mumu, ecm=365 GeV','full phase space','','2.287','1.0','1.0'],
    'wzp6_ee_tautau_ecm365':['Z/gamma* to tautau, ecm=365 GeV','full phase space','','2.017','1.0','1.0'],
    'wzp6_ee_ee_Mee_30_150_ecm365':['ee (s and t), ecm=365 GeV','30 < Mee < 150 GeV, 15 < theta < 165 deg','','1.53','1.0','1.0'],


    # xxH exclusive samples, sqrts = 240 GeV
    # branching ratios taken from LHCHXSWG/PDG unless explicitely stated
    #     'mumu'   : 2.176e-4
    #     'ee'     : 5.090e-9 -> BR(H->mumu)*(M_e/M_mu)^2
    #     'aa'     : 2.270e-3
    #     'Za'     : 1.533e-3
    #     'ZZ'     : 2.641e-2
    #     'WW'     : 2.152e-1
    #     'bb'     : 5.824e-1
    #     'cc'     : 2.891e-2
    #     'ss'     : 2.400e-4
    #     'uudd'   : 3.000e-7 -> BR(H->ss)*(M_ud/M_s)^2
    #     'dd'     : 70% of 'uudd'
    #     'uu'     : 30% of 'uudd'
    #     'gg'     : 8.187e-2
    #     'tautau' : 6.272e-2
    #
    # xsec from corresponding xxH H->bb generated events
    #     'mumuH'   : 6.7643e-3
    #     'eeH'     : 7.1611e-3
    #     'tautauH' : 6.7518e-3
    #     'nunuH'   : 46.191e-3
    #     'bbH'     : 29.970e-3
    #     'ccH'     : 23.339e-3
    #     'ssH'     : 29.958e-3
    #     'qqH'     : 53.343e-3
    'wzp6_ee_nunuH_Hbb_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to bb','','2.690e-02','1.0','1.0'],
    'wzp6_ee_nunuH_Hcc_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to cc','','1.335e-03','1.0','1.0'],
    'wzp6_ee_nunuH_Hss_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to ss','','1.109e-05','1.0','1.0'],
    'wzp6_ee_nunuH_Hgg_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to gg','','3.782e-03','1.0','1.0'],
    'wzp6_ee_nunuH_Hqq_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to uu,dd','','1.386e-08','1.0','1.0'],
    'wzp6_ee_nunuH_Hdd_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to dd','','9.702e-09','1.0','1.0'],
    'wzp6_ee_nunuH_Huu_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to uu','','4.158e-09','1.0','1.0'],
    'wzp6_ee_nunuH_Htautau_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to tautau','','2.897e-03','1.0','1.0'],
    'wzp6_ee_nunuH_Hmumu_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to mumu','','1.005e-05','1.0','1.0'],
    'wzp6_ee_nunuH_HWW_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to WW','','9.940e-03','1.0','1.0'],
    'wzp6_ee_nunuH_HZZ_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to ZZ','','1.220e-03','1.0','1.0'],
    'wzp6_ee_nunuH_HZa_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to Za','','7.081e-05','1.0','1.0'],
    'wzp6_ee_nunuH_Haa_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to aa','','1.049e-04','1.0','1.0'],

    # nunuH with QFV Higgs decays
    'wzp6_ee_nunuH_Hbd_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hbs_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hcu_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hsd_ecm240':['ee -> Z(nu nu) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],



    'wzp6_ee_eeH_Hbb_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to bb','','4.171e-03','1.0','1.0'],
    'wzp6_ee_eeH_Hcc_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to cc','','2.070e-04','1.0','1.0'],
    'wzp6_ee_eeH_Hss_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to ss','','1.718e-06','1.0','1.0'],
    'wzp6_ee_eeH_Hgg_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to gg','','5.863e-04','1.0','1.0'],
    'wzp6_ee_eeH_Htautau_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to tautau','','4.491e-04','1.0','1.0'],
    'wzp6_ee_eeH_Hmumu_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to mumu','','1.558e-06','1.0','1.0'],
    'wzp6_ee_eeH_HWW_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to WW','','1.541e-03','1.0','1.0'],
    'wzp6_ee_eeH_HZZ_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to ZZ','','1.891e-04','1.0','1.0'],
    'wzp6_ee_eeH_HZa_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to Za','','1.098e-05','1.0','1.0'],
    'wzp6_ee_eeH_Haa_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to aa','','1.626e-05','1.0','1.0'],
    
    # eeH with QFV Higgs decays
    'wzp6_ee_eeH_Hbd_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hbs_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hcu_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hsd_ecm240':['ee -> Z(e e) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_mumuH_Hbb_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to bb','','3.940e-03','1.0','1.0'],
    'wzp6_ee_mumuH_Hcc_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to cc','','1.956e-04','1.0','1.0'],
    'wzp6_ee_mumuH_Hss_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to ss','','1.624e-06','1.0','1.0'],
    'wzp6_ee_mumuH_Hgg_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to gg','','5.538e-04','1.0','1.0'],
    'wzp6_ee_mumuH_Htautau_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to tautau','','4.243e-04','1.0','1.0'],
    'wzp6_ee_mumuH_Hmumu_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to mumu','','1.472e-06','1.0','1.0'],
    'wzp6_ee_mumuH_HWW_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to WW','','1.456e-03','1.0','1.0'],
    'wzp6_ee_mumuH_HZZ_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to ZZ','','1.786e-04','1.0','1.0'],
    'wzp6_ee_mumuH_HZa_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to Za','','1.037e-05','1.0','1.0'],
    'wzp6_ee_mumuH_Haa_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to aa','','1.535e-05','1.0','1.0'],

    # mumuH with QFV Higgs decays
    'wzp6_ee_mumuH_Hbd_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hbs_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hcu_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hsd_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_mumuH_Hbs_W4p1MeV_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to bs, Higgs width set to SM','','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hbb_W4p1MeV_ecm240':['ee -> Z(mu mu) H,  ecm=240 GeV','H to bb, Higgs width set to SM','','1.0','1.0','1.0'],


    'wzp6_ee_tautauH_Hbb_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to bb','','3.932e-03','1.0','1.0'],
    'wzp6_ee_tautauH_Hcc_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to cc','','1.952e-04','1.0','1.0'],
    'wzp6_ee_tautauH_Hss_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to ss','','1.6200e-06','1.0','1.0'],
    'wzp6_ee_tautauH_Hgg_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to gg','','5.528e-04','1.0','1.0'],
    'wzp6_ee_tautauH_Htautau_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to tautau','','4.235e-04','1.0','1.0'],
    'wzp6_ee_tautauH_Hmumu_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to mumu','','1.469e-06','1.0','1.0'],
    'wzp6_ee_tautauH_HWW_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to WW','','1.453e-03','1.0','1.0'],
    'wzp6_ee_tautauH_HZZ_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to ZZ','','1.783e-04','1.0','1.0'],
    'wzp6_ee_tautauH_HZa_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to Za','','1.035e-05','1.0','1.0'],
    'wzp6_ee_tautauH_Haa_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to aa','','1.533e-05','1.0','1.0'],
    
    # tautauH with QFV Higgs decays
    'wzp6_ee_tautauH_Hbd_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hbs_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hcu_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hsd_ecm240':['ee -> Z(tau tau) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_bbH_Hbb_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to bb','','1.745e-02','1.0','1.0'],
    'wzp6_ee_bbH_Hcc_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to cc','','8.664e-04','1.0','1.0'],
    'wzp6_ee_bbH_Hss_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to ss','','7.193e-06','1.0','1.0'],
    'wzp6_ee_bbH_Hgg_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to gg','','2.454e-03','1.0','1.0'],
    'wzp6_ee_bbH_Htautau_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to tautau','','1.880e-03','1.0','1.0'],
    'wzp6_ee_bbH_Hmumu_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to mumu','','6.521e-06','1.0','1.0'],
    'wzp6_ee_bbH_HWW_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to WW','','6.450e-03','1.0','1.0'],
    'wzp6_ee_bbH_HZZ_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to ZZ','','7.915e-04','1.0','1.0'],
    'wzp6_ee_bbH_HZa_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to Za','','4.594e-05','1.0','1.0'],
    'wzp6_ee_bbH_Haa_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to aa','','6.803e-05','1.0','1.0'],
    
    # bbH with QFV Higgs decays
    'wzp6_ee_bbH_Hbd_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hbs_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hcu_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hsd_ecm240':['ee -> Z(b b) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_ccH_Hbb_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to bb','','1.359e-02','1.0','1.0'],
    'wzp6_ee_ccH_Hcc_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to cc','','6.747e-04','1.0','1.0'],
    'wzp6_ee_ccH_Hss_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to ss','','5.607e-06','1.0','1.0'],
    'wzp6_ee_ccH_Hgg_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to gg','','1.911e-03','1.0','1.0'],
    'wzp6_ee_ccH_Htautau_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to tautau','','1.464e-03','1.0','1.0'],
    'wzp6_ee_ccH_Hmumu_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to mumu','','5.079e-06','1.0','1.0'],
    'wzp6_ee_ccH_HWW_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to WW','','5.023e-03','1.0','1.0'],
    'wzp6_ee_ccH_HZZ_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to ZZ','','6.164e-04','1.0','1.0'],
    'wzp6_ee_ccH_HZa_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to Za','','3.578e-05','1.0','1.0'],
    'wzp6_ee_ccH_Haa_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to aa','','5.298e-05','1.0','1.0'],
    
    # ccH with QFV Higgs decays
    'wzp6_ee_ccH_Hbd_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hbs_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hcu_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hsd_ecm240':['ee -> Z(c c) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_ssH_Hbb_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to bb','','1.745e-02','1.0','1.0'],
    'wzp6_ee_ssH_Hcc_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to cc','','8.661e-04','1.0','1.0'],
    'wzp6_ee_ssH_Hss_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to ss','','7.190e-06','1.0','1.0'],
    'wzp6_ee_ssH_Hgg_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to gg','','2.453e-03','1.0','1.0'],
    'wzp6_ee_ssH_Htautau_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to tautau','','1.879e-03','1.0','1.0'],
    'wzp6_ee_ssH_Hmumu_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to mumu','','6.519e-06','1.0','1.0'],
    'wzp6_ee_ssH_HWW_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to WW','','6.447e-03','1.0','1.0'],
    'wzp6_ee_ssH_HZZ_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to ZZ','','7.912e-04','1.0','1.0'],
    'wzp6_ee_ssH_HZa_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to Za','','4.593e-05','1.0','1.0'],
    'wzp6_ee_ssH_Haa_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to aa','','6.800e-05','1.0','1.0'],
    
    # ssH with QFV Higgs decays
    'wzp6_ee_ssH_Hbd_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hbs_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hcu_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hsd_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    'wzp6_ee_qqH_Hbb_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to bb','','3.107e-02','1.0','1.0'],
    'wzp6_ee_qqH_Hcc_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to cc','','1.542e-03','1.0','1.0'],
    'wzp6_ee_qqH_Hss_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to ss','','1.280e-05','1.0','1.0'],
    'wzp6_ee_qqH_Hgg_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to gg','','4.367e-03','1.0','1.0'],
    'wzp6_ee_qqH_Htautau_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to tautau','','3.346e-03','1.0','1.0'],
    'wzp6_ee_qqH_Hmumu_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to mumu','','1.161e-05','1.0','1.0'],
    'wzp6_ee_qqH_HWW_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to WW','','1.148e-02','1.0','1.0'],
    'wzp6_ee_qqH_HZZ_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to ZZ','','1.409e-03','1.0','1.0'],
    'wzp6_ee_qqH_HZZ_qqqq_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to ZZ* to 4q (q=udscb)','','1.0','1.0','1.0'],
    'wzp6_ee_qqH_HZZ_qqnunu_ecm240':['ee -> Z(u u/ d d ) H,  ecm=240 GeV','H to ZZ* to 2nu2q (q=udscb)','','1.0','1.0','1.0'],
    'wzp6_ee_qqH_HZa_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to Za','','8.177e-05','1.0','1.0'],
    'wzp6_ee_qqH_Haa_ecm240':['ee -> Z(u u / d d) H,  ecm=240 GeV','H to aa','','1.211e-04','1.0','1.0'],
    
    # qqH with QFV Higgs decays
    'wzp6_ee_qqH_Hbd_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to bd','','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hbs_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to bs','','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hcu_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to cu','','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hsd_ecm240':['ee -> Z(s s) H,  ecm=240 GeV','H to sd','','1.0','1.0','1.0'],

    
# for top FCNC, ecm = 365 GeV:
    'wzp6_egamma_tbnu_ecm365':['nu_e t b (e) EPA, e- gamma, ecm=365 GeV','inc. top decays','','2.276e-4','1.0','1.0'],
    'wzp6_gammae_tbnu_ecm365':['nu_e t b (e) EPA, e+ gamma, ecm=365 GeV','inc. top decays','','2.276e-4','1.0','1.0'],
    'wzp6_ee_tbjj_singleTop_ecm365':['t B jj (+cc), j=udcs, tB pair from a W, ecm=365 GeV','inc. top decays','','5.989e-3','1.0','1.0'],
    'wzp6_egamma_eZ_Zbb_ecm365':['e(e)Z EPA, e- gamma, ecm=365 GeV','Z to bb','','615.2e-3','1.0','1.0'],
    'wzp6_gammae_eZ_Zbb_ecm365':['e(e)Z EPA, e+ gamma, ecm=365 GeV','Z to bb','','615.2e-3','1.0','1.0'],

# for polarized t tbar, ecm = 365 GeV:
    'wzp6_ee_SM_tt_tWsTWb_tlepTall_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W s -> lep, anti-top -> W b',     '','0.01','1.0','1.0'],
    'wzp6_ee_SM_tt_tWsTWb_tlightTall_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W s -> light q, anti-top -> W b', '','0.01','1.0','1.0'],
    'wzp6_ee_SM_tt_tWsTWb_theavyTall_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W s -> heavy q, anti-top -> W b', '','0.01','1.0','1.0'],
    'wzp6_ee_SM_tt_tWbTWs_tallTlep_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W b, anti-top -> W s -> lep',     '','0.01','1.0','1.0'],
    'wzp6_ee_SM_tt_tWbTWs_tallTlight_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W b, anti-top -> W s -> light q', '','0.01','1.0','1.0'],
    'wzp6_ee_SM_tt_tWbTWs_tallTheavy_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top -> W b, anti-top -> W s -> heavy q', '','0.01','1.0','1.0'],

    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],

    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_ta_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_ta_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_ta_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_ta_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_ta_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_ta_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_ta_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_ta_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],

    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_tv_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_tv_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_tv_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_tv_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_tv_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_tv_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_tv_ttAup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_tv_ttAdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
 
    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_vr_ttZup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepTlep_noCKMmix_keepPolInfo_vr_ttZdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully leptonic decays','','0.106','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_vr_ttZup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_thadThad_noCKMmix_keepPolInfo_vr_ttZdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top fully hadronic decays','','0.454','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_vr_ttZup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_tlepThad_noCKMmix_keepPolInfo_vr_ttZdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_vr_ttZup_ecm365':   ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],
    'wzp6_ee_SM_tt_thadTlep_noCKMmix_keepPolInfo_vr_ttZdown_ecm365': ['ee -> Z*/A* -> tt, ecm=365GeV','top mixed lep+had decays', '','0.220','1.0','1.0'],

# ttbar threshold scan
    'wzp6_ee_WbWb_ecm340': ['ee -> WbWb, ecm=340GeV','W inclusive', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_ecm345': ['ee -> WbWb, ecm=345GeV','W inclusive', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_ecm350': ['ee -> WbWb, ecm=350GeV','W inclusive', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_ecm355': ['ee -> WbWb, ecm=355GeV','W inclusive', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_ecm365': ['ee -> WbWb, ecm=365GeV','W inclusive', '','1.0','1.0','1.0'],

    'wzp6_ee_WbWb_had_ecm340': ['ee -> WbWb, ecm=340GeV','Whad Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_had_ecm345': ['ee -> WbWb, ecm=345GeV','Whad Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_had_ecm350': ['ee -> WbWb, ecm=350GeV','Whad Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_had_ecm355': ['ee -> WbWb, ecm=355GeV','Whad Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_had_ecm365': ['ee -> WbWb, ecm=365GeV','Whad Whad', '','1.0','1.0','1.0'],

    'wzp6_ee_WbWb_lep_ecm340': ['ee -> WbWb, ecm=340GeV','Wlep Wlep', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_lep_ecm345': ['ee -> WbWb, ecm=345GeV','Wlep Wlep', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_lep_ecm350': ['ee -> WbWb, ecm=350GeV','Wlep Wlep', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_lep_ecm355': ['ee -> WbWb, ecm=355GeV','Wlep Wlep', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_lep_ecm365': ['ee -> WbWb, ecm=365GeV','Wlep Wlep', '','1.0','1.0','1.0'],

    'wzp6_ee_WbWb_semihad_ecm340': ['ee -> WbWb, ecm=340GeV','Wlep Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_semihad_ecm345': ['ee -> WbWb, ecm=345GeV','Wlep Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_semihad_ecm350': ['ee -> WbWb, ecm=350GeV','Wlep Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_semihad_ecm355': ['ee -> WbWb, ecm=355GeV','Wlep Whad', '','1.0','1.0','1.0'],
    'wzp6_ee_WbWb_semihad_ecm365': ['ee -> WbWb, ecm=365GeV','Wlep Whad', '','1.0','1.0','1.0'],


# ee->H + background, ecm = 125 GeV:
    'wzp6_ee_l1l2nunu_ecm125':['ee -> l1l2nunu (l1!=l2, no H) ecm=125GeV','','','5.799e-03','1.0','1.0'],
    'wzp6_ee_eenunu_ecm125':['ee -> eenunu (no H) ecm=125GeV','','','3.364e-01','1.0','1.0'],
    'wzp6_ee_mumununu_ecm125':['ee -> mumununu (no H) ecm=125GeV','','','2.202e-01','1.0','1.0'],
    'wzp6_ee_tautaununu_ecm125':['ee -> tautaununu (no H) ecm=125GeV','','','4.265e-02','1.0','1.0'],

    'wzp6_ee_enueqq_ecm125':['ee -> enuqq (no H) ecm=125GeV','','','1.382e-02','1.0','1.0'],
    'wzp6_ee_munumuqq_ecm125':['ee -> munuqq (no H) ecm=125GeV','','','6.711e-03','1.0','1.0'],
    'wzp6_ee_taunutauqq_ecm125':['ee -> taunuqq (no H) ecm=125GeV','','','6.761e-03','1.0','1.0'],
    'wzp6_ee_qq_ecm125':['ee -> qq, ecm=125GeV','','','3.631E+02','1.0','1.0'],

    'wzp6_ee_Hllnunu_ecm125':['ee -> H-> WW ecm=125GeV','H->WW*->llnunu','','3.187e-05','1.0','1.0'],
    'wzp6_ee_Hlnuqq_ecm125':['ee -> H ecm=125GeV','H->WW*->lnuqq','','4.584e-05','1.0','1.0'],
    'wzp6_ee_Hqqlnu_ecm125':['ee -> H-> WW ecm=125GeV','H->WW*->qqlnu','','3.187e-05','1.0','1.0'],
    'wzp6_ee_Hgg_ecm125':['ee -> H-> gg, ecm=125GeV','','','7.384e-05','1.0','1.0'],

    # xxH, ecm = 365 GeV (sample info & cross sections to be updated!)
    'wzp6_ee_bbH_ecm365':['ee->bbH, ecm=365 GeV','H->incl.', '','1.8389e-02','1.0','1.0'],
    'wzp6_ee_ccH_ecm365':['ee->ccH, ecm=365 GeV','H->incl.', '','1.4436e-02','1.0','1.0'],
    'wzp6_ee_ssH_ecm365':['ee->ssH, ecm=365 GeV','H->incl.', '','1.8538e-02','1.0','1.0'],
    'wzp6_ee_qqH_ecm365':['ee->qqH (q=u,d), ecm=365 GeV','H->incl.', '','3.2997e-02','1.0','1.0'],

    'wzp6_ee_bbH_HWW_ecm365':['ee->bbH, ecm=365 GeV','H->WW', '','3.957e-03','1.0','1.0'],
    'wzp6_ee_bbH_HZZ_ecm365':['ee->bbH, ecm=365 GeV','H->ZZ', '','4.857e-04','1.0','1.0'],
    'wzp6_ee_bbH_HZa_ecm365':['ee->bbH, ecm=365 GeV','H->Za', '','2.819e-05','1.0','1.0'],
    'wzp6_ee_bbH_Haa_ecm365':['ee->bbH, ecm=365 GeV','H->aa', '','4.174e-05','1.0','1.0'],
    'wzp6_ee_bbH_Hbb_ecm365':['ee->bbH, ecm=365 GeV','H->bb', '','1.071e-02','1.0','1.0'],
    'wzp6_ee_bbH_Hcc_ecm365':['ee->bbH, ecm=365 GeV','H->cc', '','5.316e-04','1.0','1.0'],
    'wzp6_ee_bbH_Hgg_ecm365':['ee->bbH, ecm=365 GeV','H->gg', '','1.506e-03','1.0','1.0'],
    'wzp6_ee_bbH_Hss_ecm365':['ee->bbH, ecm=365 GeV','H->ss', '','3.678e-06','1.0','1.0'],
    'wzp6_ee_bbH_Htautau_ecm365':['ee->bbH, ecm=365 GeV','H->tautau', '','1.153e-03','1.0','1.0'],

    'wzp6_ee_ccH_HWW_ecm365':['ee->ccH, ecm=365 GeV','H->WW', '','3.107e-03','1.0','1.0'],
    'wzp6_ee_ccH_HZZ_ecm365':['ee->ccH, ecm=365 GeV','H->ZZ', '','3.813e-04','1.0','1.0'],
    'wzp6_ee_ccH_HZa_ecm365':['ee->ccH, ecm=365 GeV','H->Za', '','2.213e-05','1.0','1.0'],
    'wzp6_ee_ccH_Haa_ecm365':['ee->ccH, ecm=365 GeV','H->aa', '','3.277e-05','1.0','1.0'],
    'wzp6_ee_ccH_Hbb_ecm365':['ee->ccH, ecm=365 GeV','H->bb', '','8.407e-03','1.0','1.0'],
    'wzp6_ee_ccH_Hcc_ecm365':['ee->ccH, ecm=365 GeV','H->cc', '','4.173e-04','1.0','1.0'],
    'wzp6_ee_ccH_Hgg_ecm365':['ee->ccH, ecm=365 GeV','H->gg', '','1.182e-03','1.0','1.0'],
    'wzp6_ee_ccH_Hss_ecm365':['ee->ccH, ecm=365 GeV','H->ss', '','2.887e-06','1.0','1.0'],
    'wzp6_ee_ccH_Htautau_ecm365':['ee->ccH, ecm=365 GeV','H->tautau', '','9.054e-04','1.0','1.0'],

    'wzp6_ee_eeH_HWW_ecm365':['ee->eeH, ecm=365 GeV','H->WW', '','1.590e-03','1.0','1.0'],
    'wzp6_ee_eeH_HZZ_ecm365':['ee->eeH, ecm=365 GeV','H->ZZ', '','1.951e-04','1.0','1.0'],
    'wzp6_ee_eeH_HZa_ecm365':['ee->eeH, ecm=365 GeV','H->Za', '','1.133e-05','1.0','1.0'],
    'wzp6_ee_eeH_Haa_ecm365':['ee->eeH, ecm=365 GeV','H->aa', '','1.677e-05','1.0','1.0'],
    'wzp6_ee_eeH_Hbb_ecm365':['ee->eeH, ecm=365 GeV','H->bb', '','4.303e-03','1.0','1.0'],
    'wzp6_ee_eeH_Hcc_ecm365':['ee->eeH, ecm=365 GeV','H->cc', '','2.136e-04','1.0','1.0'],
    'wzp6_ee_eeH_Hgg_ecm365':['ee->eeH, ecm=365 GeV','H->gg', '','6.049e-04','1.0','1.0'],
    'wzp6_ee_eeH_Hss_ecm365':['ee->eeH, ecm=365 GeV','H->ss', '','1.478e-06','1.0','1.0'],
    'wzp6_ee_eeH_Htautau_ecm365':['ee->eeH, ecm=365 GeV','H->tautau', '','4.634e-04','1.0','1.0'],

    'wzp6_ee_mumuH_HWW_ecm365':['ee->mumuH, ecm=365 GeV','H->WW', '','9.007e-04','1.0','1.0'],
    'wzp6_ee_mumuH_HZZ_ecm365':['ee->mumuH, ecm=365 GeV','H->ZZ', '','1.105e-04','1.0','1.0'],
    'wzp6_ee_mumuH_HZa_ecm365':['ee->mumuH, ecm=365 GeV','H->Za', '','6.416e-06','1.0','1.0'],
    'wzp6_ee_mumuH_Haa_ecm365':['ee->mumuH, ecm=365 GeV','H->aa', '','9.501e-06','1.0','1.0'],
    'wzp6_ee_mumuH_Hbb_ecm365':['ee->mumuH, ecm=365 GeV','H->bb', '','2.438e-03','1.0','1.0'],
    'wzp6_ee_mumuH_Hcc_ecm365':['ee->mumuH, ecm=365 GeV','H->cc', '','1.210e-04','1.0','1.0'],
    'wzp6_ee_mumuH_Hgg_ecm365':['ee->mumuH, ecm=365 GeV','H->gg', '','3.426e-04','1.0','1.0'],
    'wzp6_ee_mumuH_Hss_ecm365':['ee->mumuH, ecm=365 GeV','H->ss', '','8.371e-07','1.0','1.0'],
    'wzp6_ee_mumuH_Htautau_ecm365':['ee->mumuH, ecm=365 GeV','H->tautau', '','2.625e-04','1.0','1.0'],

    'wzp6_ee_nunuH_HWW_ecm365':['ee->nunuH, ecm=365 GeV','H->WW', '','1.161e-02','1.0','1.0'],
    'wzp6_ee_nunuH_HZZ_ecm365':['ee->nunuH, ecm=365 GeV','H->ZZ', '','1.425e-03','1.0','1.0'],
    'wzp6_ee_nunuH_HZa_ecm365':['ee->nunuH, ecm=365 GeV','H->Za', '','8.273e-05','1.0','1.0'],
    'wzp6_ee_nunuH_Haa_ecm365':['ee->nunuH, ecm=365 GeV','H->aa', '','1.225e-04','1.0','1.0'],
    'wzp6_ee_nunuH_Hbb_ecm365':['ee->nunuH, ecm=365 GeV','H->bb', '','3.143e-02','1.0','1.0'],
    'wzp6_ee_nunuH_Hcc_ecm365':['ee->nunuH, ecm=365 GeV','H->cc', '','1.560e-03','1.0','1.0'],
    'wzp6_ee_nunuH_Hgg_ecm365':['ee->nunuH, ecm=365 GeV','H->gg', '','4.418e-03','1.0','1.0'],
    'wzp6_ee_nunuH_Hss_ecm365':['ee->nunuH, ecm=365 GeV','H->ss', '','1.079e-05','1.0','1.0'],
    'wzp6_ee_nunuH_Htautau_ecm365':['ee->nunuH, ecm=365 GeV','H->tautau', '','3.385e-03','1.0','1.0'],

    'wzp6_ee_qqH_HWW_ecm365':['ee->qqH, ecm=365 GeV','H->WW', '','7.101e-03','1.0','1.0'],
    'wzp6_ee_qqH_HZZ_ecm365':['ee->qqH, ecm=365 GeV','H->ZZ', '','8.715e-04','1.0','1.0'],
    'wzp6_ee_qqH_HZa_ecm365':['ee->qqH, ecm=365 GeV','H->Za', '','5.058e-05','1.0','1.0'],
    'wzp6_ee_qqH_Haa_ecm365':['ee->qqH, ecm=365 GeV','H->aa', '','7.490e-05','1.0','1.0'],
    'wzp6_ee_qqH_Hbb_ecm365':['ee->qqH, ecm=365 GeV','H->bb', '','1.922e-02','1.0','1.0'],
    'wzp6_ee_qqH_Hcc_ecm365':['ee->qqH, ecm=365 GeV','H->cc', '','9.540e-04','1.0','1.0'],
    'wzp6_ee_qqH_Hgg_ecm365':['ee->qqH, ecm=365 GeV','H->gg', '','2.701e-03','1.0','1.0'],
    'wzp6_ee_qqH_Hss_ecm365':['ee->qqH, ecm=365 GeV','H->ss', '','6.599e-06','1.0','1.0'],
    'wzp6_ee_qqH_Htautau_ecm365':['ee->qqH, ecm=365 GeV','H->tautau', '','2.070e-03','1.0','1.0'],

    'wzp6_ee_ssH_HWW_ecm365':['ee->ssH, ecm=365 GeV','H->WW', '','3.989e-03','1.0','1.0'],
    'wzp6_ee_ssH_HZZ_ecm365':['ee->ssH, ecm=365 GeV','H->ZZ', '','4.896e-04','1.0','1.0'],
    'wzp6_ee_ssH_HZa_ecm365':['ee->ssH, ecm=365 GeV','H->Za', '','2.842e-05','1.0','1.0'],
    'wzp6_ee_ssH_Haa_ecm365':['ee->ssH, ecm=365 GeV','H->aa', '','4.208e-05','1.0','1.0'],
    'wzp6_ee_ssH_Hbb_ecm365':['ee->ssH, ecm=365 GeV','H->bb', '','1.080e-02','1.0','1.0'],
    'wzp6_ee_ssH_Hcc_ecm365':['ee->ssH, ecm=365 GeV','H->cc', '','5.359e-04','1.0','1.0'],
    'wzp6_ee_ssH_Hgg_ecm365':['ee->ssH, ecm=365 GeV','H->gg', '','1.518e-03','1.0','1.0'],
    'wzp6_ee_ssH_Hss_ecm365':['ee->ssH, ecm=365 GeV','H->ss', '','3.708e-06','1.0','1.0'],
    'wzp6_ee_ssH_Htautau_ecm365':['ee->ssH, ecm=365 GeV','H->tautau', '','1.163e-03','1.0','1.0'],

    'wzp6_ee_tautauH_HWW_ecm365':['ee->tautauH, ecm=365 GeV','H->WW', '','8.979e-04','1.0','1.0'],
    'wzp6_ee_tautauH_HZZ_ecm365':['ee->tautauH, ecm=365 GeV','H->ZZ', '','1.102e-04','1.0','1.0'],
    'wzp6_ee_tautauH_HZa_ecm365':['ee->tautauH, ecm=365 GeV','H->Za', '','6.396e-06','1.0','1.0'],
    'wzp6_ee_tautauH_Haa_ecm365':['ee->tautauH, ecm=365 GeV','H->aa', '','9.471e-06','1.0','1.0'],
    'wzp6_ee_tautauH_Hbb_ecm365':['ee->tautauH, ecm=365 GeV','H->bb', '','2.430e-03','1.0','1.0'],
    'wzp6_ee_tautauH_Hcc_ecm365':['ee->tautauH, ecm=365 GeV','H->cc', '','1.206e-04','1.0','1.0'],
    'wzp6_ee_tautauH_Hgg_ecm365':['ee->tautauH, ecm=365 GeV','H->gg', '','3.416e-04','1.0','1.0'],
    'wzp6_ee_tautauH_Hss_ecm365':['ee->tautauH, ecm=365 GeV','H->ss', '','8.345e-07','1.0','1.0'],
    'wzp6_ee_tautauH_Htautau_ecm365':['ee->tautauH, ecm=365 GeV','H->tautau', '','2.617e-04','1.0','1.0'],

    'wzp6_ee_bbH_Hbd_ecm365':['ee->mumuH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hbs_ecm365':['ee->mumuH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hcu_ecm365':['ee->mumuH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_bbH_Hsd_ecm365':['ee->mumuH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hbd_ecm365':['ee->ccH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hbs_ecm365':['ee->ccH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hcu_ecm365':['ee->ccH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_ccH_Hsd_ecm365':['ee->ccH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hbd_ecm365':['ee->eeH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hbs_ecm365':['ee->eeH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hcu_ecm365':['ee->eeH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_eeH_Hsd_ecm365':['ee->eeH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hbd_ecm365':['ee->mumuH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hbs_ecm365':['ee->mumuH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hcu_ecm365':['ee->mumuH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_mumuH_Hsd_ecm365':['ee->mumuH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hbd_ecm365':['ee->nunuH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hbs_ecm365':['ee->nunuH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hcu_ecm365':['ee->nunuH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_nunuH_Hsd_ecm365':['ee->nunuH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hbd_ecm365':['ee->qqH (q=u,d), ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hbs_ecm365':['ee->qqH (q=u,d), ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hcu_ecm365':['ee->qqH (q=u,d), ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_qqH_Hsd_ecm365':['ee->qqH (q=u,d), ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hbd_ecm365':['ee->ssH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hbs_ecm365':['ee->ssH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hcu_ecm365':['ee->ssH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_ssH_Hsd_ecm365':['ee->ssH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hbd_ecm365':['ee->tautauH, ecm=365 GeV','H->bd', '','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hbs_ecm365':['ee->tautauH, ecm=365 GeV','H->bs', '','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hcu_ecm365':['ee->tautauH, ecm=365 GeV','H->cu', '','1.0','1.0','1.0'],
    'wzp6_ee_tautauH_Hsd_ecm365':['ee->tautauH, ecm=365 GeV','H->sd', '','1.0','1.0','1.0'],


    'wzp6_ee_qqH_HZZ_qqqq_ecm365':['ee -> Z(u u / d d) H, ecm=365 GeV','H to ZZ* to 4q (q=udscb)', '','3.6231e-03','1.0','1.0'],
    'wzp6_ee_qqH_HZZ_qqnunu_ecm365':['ee->Z(u u / d d) H, ecm=365 GeV','H to ZZ* to 2nu2q (q=udscb)', '','2.43815e-04','1.0','1.0'],

    'wzp6_ee_tautau_ecm365': ['Z/gamma* to tautau, ecm=365 GeV','full phase space', '','2.01656','1.0','1.0'],
    'wzp6_ee_mumu_ecm365':['Z/gamma* to mumu, ecm=365 GeV','full phase space', '','2.28580','1.0','1.0'],
    'wzp6_ee_ee_Mee_30_150_ecm365':['ee (s and t), ecm=365 GeV','30 < Mee < 150 GeV, 15 < theta < 165 deg', '','1.5270','1.0','1.0'],

    'wzp6_ee_qq_ecm340':['ee -> qq, ecm=340GeV','','','9.4775','1.0','1.0'],
    'wzp6_ee_qq_ecm345':['ee -> qq, ecm=345GeV','','','9.4775','1.0','1.0'],
    'wzp6_ee_qq_ecm350':['ee -> qq, ecm=350GeV','','','9.4775','1.0','1.0'],
    'wzp6_ee_qq_ecm355':['ee -> qq, ecm=355GeV','','','9.4775','1.0','1.0'],
    'wzp6_ee_qq_ecm365':['ee -> qq, ecm=365GeV','','','9.4775','1.0','1.0'],

    'wzp6_egamma_eZ_Zmumu_ecm365':['e(e)Z EPA, e- gamma, ecm=365 GeV', 'Z->mumu','1.40104e-01','1.0','1.0'],
    'wzp6_gammae_eZ_Zmumu_ecm365':['e(e)Z EPA, e+ gamma, ecm=365 GeV','Z->mumu', '','1.3992e-01','1.0','1.0'],
    'wzp6_egamma_eZ_Zee_ecm365':['e(e)Z EPA, e- gamma, ecm=365 GeV','Z->ee', '','6.9932e-02','1.0','1.0'],
    'wzp6_gammae_eZ_Zee_ecm365':['e(e)Z EPA, e+ gamma, ecm=365 GeV','Z->ee', '','7.00717e-02','1.0','1.0'],

    'wzp6_gaga_mumu_60_ecm365':['gammagamma to mumu, M(mumu) > 60 GeV, ecm=365 GeV','', '','2.8431','1.0','1.0'],
    'wzp6_gaga_ee_60_ecm365':['gammagamma to ee, M(ee) > 60 GeV,  ecm=365 GeV','', '','2.0063','1.0','1.0'],
    'wzp6_gaga_tautau_60_ecm365':['gammagamma to tautau, M(tautau) > 60 GeV, ecm=365 GeV','', '','1.5395','1.0','1.0'],

    'wzp6_ee_nuenueZ_ecm365':['Z nue nuebar, W- exchange only','Z inclusive', '','1.2624e-01','1.0','1.0'],

    'wzp6_ee_mumu_ecm91p188':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],
    'wzp6_ee_mumu_ecm91p1879':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],
    'wzp6_ee_mumu_ecm91p1881':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],
    'wzp6_ee_mumu_ecm91p18795':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],
    'wzp6_ee_mumu_ecm91p18805':['Z/Gamma* ecm=91.188GeV','Z decays to mumu','','1462.08','1.0','1.0'],




}

