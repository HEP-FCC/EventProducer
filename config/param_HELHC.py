#module
module_name='config/param_HELHC.py'

#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#stat
lhe_stat="/afs/cern.ch/user/h/helsens/www/data/statlhe_HELHC.html"
delphes_stat="/afs/cern.ch/user/h/helsens/www/data/statdelphesVERSION_HELHC.html"

#web
lhe_web="/afs/cern.ch/user/h/helsens/www/data/LHEevents_helhc.txt"
delphes_web="/afs/cern.ch/user/h/helsens/www/data/Delphesevents_VERSION.txt"

#yaml directory
yamldir='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/HELHC/'

#heppy and proc lists
heppyList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/HELHC_heppySampleList_VERSION.py'
procList = '/afs/cern.ch/work/h/helsens/public/FCCDicts/HELHC_procDict_VERSION.json'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/helhc/generation/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/helhc/generation/lhe/'
##extension
lhe_ext     ='.lhe.gz'

##FCC versions
fcc_versions=['helhc_v01']

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/helhc/generation/DelphesEvents/'
##extension
delphes_ext='.root'
##name of the ttree
treename='events'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/helhc/utils/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/helhc/utils/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/helhc/utils/config/'

##muom momentum delphes resolution card
delphescard_mmr='muonMomentumResolutionVsP.tcl'
##momentum resolution delphes card
delphescard_mr='momentumResolutionVsP.tcl'
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v02.py'

##base dir of FCCSW
fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
##init script for FCCSW
stack=fccsw_dir+'init_fcc_stack.sh'
##FCCSW dir
fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
'dummy':['','','','','',''],
'p8_pp_ExcitedQ_2TeV_qq':['2TeV Excited quark Lambda 2TeV','','','186.46','1.0','1.0'],
'p8_pp_ExcitedQ_4TeV_qq':['4TeV Excited quark Lambda 4TeV','','','5.30825','1.0','1.0'],
'p8_pp_ExcitedQ_6TeV_qq':['6TeV Excited quark Lambda 6TeV','','','0.412825','1.0','1.0'],
'p8_pp_ExcitedQ_8TeV_qq':['8TeV Excited quark Lambda 8TeV','','','0.0447138','1.0','1.0'],
'p8_pp_ExcitedQ_10TeV_qq':['10TeV Excited quark Lambda 10TeV','','','0.00558454','1.0','1.0'],
'p8_pp_ExcitedQ_12TeV_qq':['12TeV Excited quark Lambda 12TeV','','','0.000728121','1.0','1.0'],
'p8_pp_ExcitedQ_14TeV_qq':['14TeV Excited quark Lambda 14TeV','','','9.70582e-05','1.0','1.0'],
'p8_pp_ExcitedQ_16TeV_qq':['16TeV Excited quark Lambda 16TeV','','','1.44959e-05','1.0','1.0'],
'p8_pp_ExcitedQ_18TeV_qq':['18TeV Excited quark Lambda 18TeV','','','3.10421e-06','1.0','1.0'],


'p8_pp_ZprimePSI_1TeV_ll':['1TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','1.26327','1.0','1.0'],
'p8_pp_ZprimePSI_2TeV_ll':['2TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','0.085362','1.0','1.0'],
'p8_pp_ZprimePSI_4TeV_ll':['4TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','0.00336506','1.0','1.0'],
'p8_pp_ZprimePSI_6TeV_ll':['6TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','0.000319221','1.0','1.0'],
'p8_pp_ZprimePSI_8TeV_ll':['8TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','4.16344e-05','1.0','1.0'],
'p8_pp_ZprimePSI_10TeV_ll':['10TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','6.47563e-06','1.0','1.0'],
'p8_pp_ZprimePSI_12TeV_ll':['12TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','1.39881e-06','1.0','1.0'],
'p8_pp_ZprimePSI_14TeV_ll':['14TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','4.60545e-07','1.0','1.0'],
'p8_pp_ZprimePSI_16TeV_ll':['16TeV Z\'(PSI) -> ll (l=e,mu,tau)','','','2.25108e-07','1.0','1.0'],

'p8_pp_ZprimeI_1TeV_ll':['1TeV Z\'(I) -> ll (l=e,mu,tau)','','','2.30174','1.0','1.0'],
'p8_pp_ZprimeI_2TeV_ll':['2TeV Z\'(I) -> ll (l=e,mu,tau)','','','0.153677','1.0','1.0'],
'p8_pp_ZprimeI_4TeV_ll':['4TeV Z\'(I) -> ll (l=e,mu,tau)','','','0.00582704','1.0','1.0'],
'p8_pp_ZprimeI_6TeV_ll':['6TeV Z\'(I) -> ll (l=e,mu,tau)','','','0.000515749','1.0','1.0'],
'p8_pp_ZprimeI_8TeV_ll':['8TeV Z\'(I) -> ll (l=e,mu,tau)','','','6.57607e-05','1.0','1.0'],
'p8_pp_ZprimeI_10TeV_ll':['10TeV Z\'(I) -> ll (l=e,mu,tau)','','','1.17107e-05','1.0','1.0'],
'p8_pp_ZprimeI_12TeV_ll':['12TeV Z\'(I) -> ll (l=e,mu,tau)','','','3.37889e-06','1.0','1.0'],
'p8_pp_ZprimeI_14TeV_ll':['14TeV Z\'(I) -> ll (l=e,mu,tau)','','','1.46041e-06','1.0','1.0'],
'p8_pp_ZprimeI_16TeV_ll':['16TeV Z\'(I) -> ll (l=e,mu,tau)','','','7.89383e-07','1.0','1.0'],

'p8_pp_ZprimeCHI_1TeV_ll':['1TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','2.72389','1.0','1.0'],
'p8_pp_ZprimeCHI_2TeV_ll':['2TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','0.181617','1.0','1.0'],
'p8_pp_ZprimeCHI_4TeV_ll':['4TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','0.00703298','1.0','1.0'],
'p8_pp_ZprimeCHI_6TeV_ll':['6TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','0.000658995','1.0','1.0'],
'p8_pp_ZprimeCHI_8TeV_ll':['8TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','8.70986e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_10TeV_ll':['10TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','1.57176e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_12TeV_ll':['12TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','4.46175e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_14TeV_ll':['14TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','1.89368e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_16TeV_ll':['16TeV Z\'(CHI) -> ll (l=e,mu,tau)','','','1.02383e-06','1.0','1.0'],

'p8_pp_ZprimeLRM_1TeV_ll':['1TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','2.87617','1.0','1.0'],
'p8_pp_ZprimeLRM_2TeV_ll':['2TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','0.193013','1.0','1.0'],
'p8_pp_ZprimeLRM_4TeV_ll':['4TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','0.00797759','1.0','1.0'],
'p8_pp_ZprimeLRM_6TeV_ll':['6TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','0.000787521','1.0','1.0'],
'p8_pp_ZprimeLRM_8TeV_ll':['8TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','0.000115722','1.0','1.0'],
'p8_pp_ZprimeLRM_10TeV_ll':['10TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','2.45152e-05','1.0','1.0'],
'p8_pp_ZprimeLRM_12TeV_ll':['12TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','7.68388e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_14TeV_ll':['14TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','3.48641e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_16TeV_ll':['16TeV Z\'(LRM) -> ll (l=e,mu,tau)','','','1.91233e-06','1.0','1.0'],

'p8_pp_ZprimeSSM_1TeV_ll':['1TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.43703','1.0','1.0'],
'p8_pp_ZprimeSSM_2TeV_ll':['2TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','0.299201','1.0','1.0'],
'p8_pp_ZprimeSSM_4TeV_ll':['4TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','0.0125426','1.0','1.0'],
'p8_pp_ZprimeSSM_6TeV_ll':['6TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','0.00127705','1.0','1.0'],
'p8_pp_ZprimeSSM_8TeV_ll':['8TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','0.000204715','1.0','1.0'],
'p8_pp_ZprimeSSM_10TeV_ll':['10TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.76451e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_12TeV_ll':['12TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.6009e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_14TeV_ll':['14TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','7.50234e-06','1.0','1.0'],
'p8_pp_ZprimeSSM_16TeV_ll':['16TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.1616e-06','1.0','1.0'],

'p8_pp_ZprimeETA_1TeV_ll':['1TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','1.43422','1.0','1.0'],
'p8_pp_ZprimeETA_2TeV_ll':['2TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','0.0975244','1.0','1.0'],
'p8_pp_ZprimeETA_4TeV_ll':['4TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','0.0038843','1.0','1.0'],
'p8_pp_ZprimeETA_6TeV_ll':['6TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','0.000373203','1.0','1.0'],
'p8_pp_ZprimeETA_8TeV_ll':['8TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','4.90595e-05','1.0','1.0'],
'p8_pp_ZprimeETA_10TeV_ll':['10TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','8.00358e-06','1.0','1.0'],
'p8_pp_ZprimeETA_12TeV_ll':['12TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','1.80172e-06','1.0','1.0'],
'p8_pp_ZprimeETA_14TeV_ll':['14TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','6.12268e-07','1.0','1.0'],
'p8_pp_ZprimeETA_16TeV_ll':['16TeV Z\'(ETA) -> ll (l=e,mu,tau)','','','3.03296e-07','1.0','1.0'],

'p8_pp_ZprimePSI_1TeV_ll_PDF19':['1TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','1.4744','1.0','1.0'],
'p8_pp_ZprimePSI_2TeV_ll_PDF19':['2TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.101514','1.0','1.0'],
'p8_pp_ZprimePSI_4TeV_ll_PDF19':['4TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00392017','1.0','1.0'],
'p8_pp_ZprimePSI_6TeV_ll_PDF19':['6TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000336398','1.0','1.0'],
'p8_pp_ZprimePSI_8TeV_ll_PDF19':['8TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','3.94839e-05','1.0','1.0'],
'p8_pp_ZprimePSI_10TeV_ll_PDF19':['10TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','6.10682e-06','1.0','1.0'],
'p8_pp_ZprimePSI_12TeV_ll_PDF19':['12TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','1.40828e-06','1.0','1.0'],
'p8_pp_ZprimePSI_14TeV_ll_PDF19':['14TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','5.04701e-07','1.0','1.0'],
'p8_pp_ZprimePSI_16TeV_ll_PDF19':['16TeV Z\'(PSI) -> ll (l=e,mu,tau) NNPDF3.0','','','2.53195e-07','1.0','1.0'],
'p8_pp_ZprimeI_1TeV_ll_PDF19':['1TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','2.6997','1.0','1.0'],
'p8_pp_ZprimeI_2TeV_ll_PDF19':['2TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','0.178875','1.0','1.0'],
'p8_pp_ZprimeI_4TeV_ll_PDF19':['4TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00640409','1.0','1.0'],
'p8_pp_ZprimeI_6TeV_ll_PDF19':['6TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000519332','1.0','1.0'],
'p8_pp_ZprimeI_8TeV_ll_PDF19':['8TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','6.66165e-05','1.0','1.0'],
'p8_pp_ZprimeI_10TeV_ll_PDF19':['10TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','1.47512e-05','1.0','1.0'],
'p8_pp_ZprimeI_12TeV_ll_PDF19':['12TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','4.64312e-06','1.0','1.0'],
'p8_pp_ZprimeI_14TeV_ll_PDF19':['14TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','1.89327e-06','1.0','1.0'],
'p8_pp_ZprimeI_16TeV_ll_PDF19':['16TeV Z\'(I) -> ll (l=e,mu,tau) NNPDF3.0','','','9.54216e-07','1.0','1.0'],
'p8_pp_ZprimeCHI_1TeV_ll_PDF19':['1TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','3.22179','1.0','1.0'],
'p8_pp_ZprimeCHI_2TeV_ll_PDF19':['2TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.212271','1.0','1.0'],
'p8_pp_ZprimeCHI_4TeV_ll_PDF19':['4TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00791412','1.0','1.0'],
'p8_pp_ZprimeCHI_6TeV_ll_PDF19':['6TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000676058','1.0','1.0'],
'p8_pp_ZprimeCHI_8TeV_ll_PDF19':['8TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','8.69071e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_10TeV_ll_PDF19':['10TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','1.77016e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_12TeV_ll_PDF19':['12TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','5.55227e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_14TeV_ll_PDF19':['14TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','2.30074e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_16TeV_ll_PDF19':['16TeV Z\'(CHI) -> ll (l=e,mu,tau) NNPDF3.0','','','1.20053e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_1TeV_ll_PDF19':['1TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','3.37247','1.0','1.0'],
'p8_pp_ZprimeLRM_2TeV_ll_PDF19':['2TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.227451','1.0','1.0'],
'p8_pp_ZprimeLRM_4TeV_ll_PDF19':['4TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00912529','1.0','1.0'],
'p8_pp_ZprimeLRM_6TeV_ll_PDF19':['6TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000828187','1.0','1.0'],
'p8_pp_ZprimeLRM_8TeV_ll_PDF19':['8TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000117093','1.0','1.0'],
'p8_pp_ZprimeLRM_10TeV_ll_PDF19':['10TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','2.58827e-05','1.0','1.0'],
'p8_pp_ZprimeLRM_12TeV_ll_PDF19':['12TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','8.69422e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_14TeV_ll_PDF19':['14TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','4.0263e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_16TeV_ll_PDF19':['16TeV Z\'(LRM) -> ll (l=e,mu,tau) NNPDF3.0','','','2.20753e-06','1.0','1.0'],
'p8_pp_ZprimeSSM_1TeV_ll_PDF19':['1TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','5.12833','1.0','1.0'],
'p8_pp_ZprimeSSM_2TeV_ll_PDF19':['2TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.35421','1.0','1.0'],
'p8_pp_ZprimeSSM_4TeV_ll_PDF19':['4TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.0145604','1.0','1.0'],
'p8_pp_ZprimeSSM_6TeV_ll_PDF19':['6TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00136389','1.0','1.0'],
'p8_pp_ZprimeSSM_8TeV_ll_PDF19':['8TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000207047','1.0','1.0'],
'p8_pp_ZprimeSSM_10TeV_ll_PDF19':['10TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','4.95649e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_12TeV_ll_PDF19':['12TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','1.78606e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_14TeV_ll_PDF19':['14TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','8.61274e-06','1.0','1.0'],
'p8_pp_ZprimeSSM_16TeV_ll_PDF19':['16TeV Z\'(SSM) -> ll (l=e,mu,tau) NNPDF3.0','','','4.83197e-06','1.0','1.0'],
'p8_pp_ZprimeETA_1TeV_ll_PDF19':['1TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','1.64617','1.0','1.0'],
'p8_pp_ZprimeETA_2TeV_ll_PDF19':['2TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','0.115515','1.0','1.0'],
'p8_pp_ZprimeETA_4TeV_ll_PDF19':['4TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','0.00457997','1.0','1.0'],
'p8_pp_ZprimeETA_6TeV_ll_PDF19':['6TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','0.000397324','1.0','1.0'],
'p8_pp_ZprimeETA_8TeV_ll_PDF19':['8TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','4.70821e-05','1.0','1.0'],
'p8_pp_ZprimeETA_10TeV_ll_PDF19':['10TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','7.32045e-06','1.0','1.0'],
'p8_pp_ZprimeETA_12TeV_ll_PDF19':['12TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','1.68533e-06','1.0','1.0'],
'p8_pp_ZprimeETA_14TeV_ll_PDF19':['14TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','6.45198e-07','1.0','1.0'],
'p8_pp_ZprimeETA_16TeV_ll_PDF19':['16TeV Z\'(ETA) -> ll (l=e,mu,tau) NNPDF3.0','','','3.37497e-07','1.0','1.0'],



'p8_pp_ZprimeSSM_Interf_6TeV_ll':['6TeV Z\'(SSM) -> ll (l=e,mu,tau) full interference','','','0.00127705','1.0','1.0'],
'p8_pp_ZprimeCHI_Interf_6TeV_ll':['6TeV Z\'(CHI) -> ll (l=e,mu,tau) full interference','','','0.000658995','1.0','1.0'],
'p8_pp_ZprimePSI_Interf_6TeV_ll':['6TeV Z\'(PSI) -> ll (l=e,mu,tau) full interference','','','0.000319221','1.0','1.0'],
'p8_pp_ZprimeETA_Interf_6TeV_ll':['6TeV Z\'(ETA) -> ll (l=e,mu,tau) full interference','','','0.000373203','1.0','1.0'],
'p8_pp_ZprimeLRM_Interf_6TeV_ll':['6TeV Z\'(LRM) -> ll (l=e,mu,tau) full interference','','','0.000787521','1.0','1.0'],
'p8_pp_ZprimeI_Interf_6TeV_ll':['6TeV Z\'(I) -> ll (l=e,mu,tau) full interference','','','0.000515749','1.0','1.0'],


'p8_pp_ZprimeSSM_Interf_6TeV_ll_PDF19':['6TeV Z\'(SSM) -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00155311','1.0','1.0'],
'p8_pp_ZprimeCHI_Interf_6TeV_ll_PDF19':['6TeV Z\'(CHI) -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00134517','1.0','1.0'],
'p8_pp_ZprimePSI_Interf_6TeV_ll_PDF19':['6TeV Z\'(PSI) -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00105053','1.0','1.0'],
'p8_pp_ZprimeETA_Interf_6TeV_ll_PDF19':['6TeV Z\'(ETA) -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00111821','1.0','1.0'],
'p8_pp_ZprimeLRM_Interf_6TeV_ll_PDF19':['6TeV Z\'(LRM) -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00134586','1.0','1.0'],
'p8_pp_ZprimeI_Interf_6TeV_ll_PDF19':  ['6TeV Z\'(I)   -> ll (l=e,mu,tau) full interference NNPDF3.0','','','0.00119849','1.0','1.0'],


'p8_pp_ZprimePSI_1TeV_jj'    :['1TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','7.59214','1.0','1.0'],
'p8_pp_ZprimePSI_2TeV_jj'    :['2TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','0.520618','1.0','1.0'],
'p8_pp_ZprimePSI_4TeV_jj'    :['4TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','0.0205405','1.0','1.0'],
'p8_pp_ZprimePSI_6TeV_jj'    :['6TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','0.0019434','1.0','1.0'],
'p8_pp_ZprimePSI_8TeV_jj'    :['8TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','0.000258114','1.0','1.0'],
'p8_pp_ZprimePSI_10TeV_jj'   :['10TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','3.96924e-05','1.0','1.0'],
'p8_pp_ZprimePSI_12TeV_jj'   :['12TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','8.47528e-06','1.0','1.0'],
'p8_pp_ZprimePSI_14TeV_jj'   :['14TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','2.75877e-06','1.0','1.0'],
'p8_pp_ZprimePSI_16TeV_jj'   :['16TeV Z\'(PSI) -> jj (j=u,d,s,c,b,t)','','','1.3206e-06','1.0','1.0'],
'p8_pp_ZprimeI_1TeV_jj'      :['1TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','7.20851','1.0','1.0'],
'p8_pp_ZprimeI_2TeV_jj'      :['2TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','0.463603','1.0','1.0'],
'p8_pp_ZprimeI_4TeV_jj'      :['4TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','0.0179226','1.0','1.0'],
'p8_pp_ZprimeI_6TeV_jj'      :['6TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','0.00160164','1.0','1.0'],
'p8_pp_ZprimeI_8TeV_jj'      :['8TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','0.000202025','1.0','1.0'],
'p8_pp_ZprimeI_10TeV_jj'     :['10TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','3.62837e-05','1.0','1.0'],
'p8_pp_ZprimeI_12TeV_jj'     :['12TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','1.03258e-05','1.0','1.0'],
'p8_pp_ZprimeI_14TeV_jj'     :['14TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','4.45916e-06','1.0','1.0'],
'p8_pp_ZprimeI_16TeV_jj'     :['16TeV Z\'(I) -> jj (j=u,d,s,c,b,t)','','','2.42305e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_1TeV_jj'    :['1TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','9.91395','1.0','1.0'],
'p8_pp_ZprimeCHI_2TeV_jj'    :['2TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','0.666581','1.0','1.0'],
'p8_pp_ZprimeCHI_4TeV_jj'    :['4TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','0.0261613','1.0','1.0'],
'p8_pp_ZprimeCHI_6TeV_jj'    :['6TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','0.00241642','1.0','1.0'],
'p8_pp_ZprimeCHI_8TeV_jj'    :['8TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','0.000318149','1.0','1.0'],
'p8_pp_ZprimeCHI_10TeV_jj'   :['10TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','5.73496e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_12TeV_jj'   :['12TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','1.618e-05','1.0','1.0'],
'p8_pp_ZprimeCHI_14TeV_jj'   :['14TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','6.84006e-06','1.0','1.0'],
'p8_pp_ZprimeCHI_16TeV_jj'   :['16TeV Z\'(CHI) -> jj (j=u,d,s,c,b,t)','','','3.66079e-06','1.0','1.0'],
'p8_pp_ZprimeLRM_1TeV_jj'    :['1TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','35.8386','1.0','1.0'],
'p8_pp_ZprimeLRM_2TeV_jj'    :['2TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','2.46358','1.0','1.0'],
'p8_pp_ZprimeLRM_4TeV_jj'    :['4TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','0.101062','1.0','1.0'],
'p8_pp_ZprimeLRM_6TeV_jj'    :['6TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','0.00981409','1.0','1.0'],
'p8_pp_ZprimeLRM_8TeV_jj'    :['8TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','0.0014444','1.0','1.0'],
'p8_pp_ZprimeLRM_10TeV_jj'   :['10TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','0.000300157','1.0','1.0'],
'p8_pp_ZprimeLRM_12TeV_jj'   :['12TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','9.49054e-05','1.0','1.0'],
'p8_pp_ZprimeLRM_14TeV_jj'   :['14TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','4.27867e-05','1.0','1.0'],
'p8_pp_ZprimeLRM_16TeV_jj'   :['16TeV Z\'(LRM) -> jj (j=u,d,s,c,b,t)','','','2.33348e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_1TeV_jj'    :['1TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','34.7115','1.0','1.0'],
'p8_pp_ZprimeSSM_2TeV_jj'    :['2TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','2.40375','1.0','1.0'],
'p8_pp_ZprimeSSM_4TeV_jj'    :['4TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','0.0996266','1.0','1.0'],
'p8_pp_ZprimeSSM_6TeV_jj'    :['6TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','0.0102918','1.0','1.0'],
'p8_pp_ZprimeSSM_8TeV_jj'    :['8TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','0.00162104','1.0','1.0'],
'p8_pp_ZprimeSSM_10TeV_jj'   :['10TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','0.000369505','1.0','1.0'],
'p8_pp_ZprimeSSM_12TeV_jj'   :['12TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','0.000126317','1.0','1.0'],
'p8_pp_ZprimeSSM_14TeV_jj'   :['14TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','5.78862e-05','1.0','1.0'],
'p8_pp_ZprimeSSM_16TeV_jj'   :['16TeV Z\'(SSM) -> jj (j=u,d,s,c,b,t)','','','3.23801e-05','1.0','1.0'],
'p8_pp_ZprimeETA_1TeV_jj'    :['1TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','11.0678','1.0','1.0'],
'p8_pp_ZprimeETA_2TeV_jj'    :['2TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','0.768449','1.0','1.0'],
'p8_pp_ZprimeETA_4TeV_jj'    :['4TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','0.0309143','1.0','1.0'],
'p8_pp_ZprimeETA_6TeV_jj'    :['6TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','0.00297326','1.0','1.0'],
'p8_pp_ZprimeETA_8TeV_jj'    :['8TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','0.000401193','1.0','1.0'],
'p8_pp_ZprimeETA_10TeV_jj'   :['10TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','6.40747e-05','1.0','1.0'],
'p8_pp_ZprimeETA_12TeV_jj'   :['12TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','1.39607e-05','1.0','1.0'],
'p8_pp_ZprimeETA_14TeV_jj'   :['14TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','4.73693e-06','1.0','1.0'],
'p8_pp_ZprimeETA_16TeV_jj'   :['16TeV Z\'(ETA) -> jj (j=u,d,s,c,b,t)','','','2.28996e-06','1.0','1.0'],

'p8_pp_Zprime_2TeV_ttbar':['2TeV Z\' -> ttbar','','','0.940036996838','1.0','1.0'],
'p8_pp_Zprime_4TeV_ttbar':['4TeV Z\' -> ttbar','','','0.0405111026035','1.0','1.0'],
'p8_pp_Zprime_5TeV_ttbar':['5TeV Z\' -> ttbar','','','0.0121043519574','1.0','1.0'],
'p8_pp_Zprime_6TeV_ttbar':['6TeV Z\' -> ttbar','','','0.00406482067516','1.0','1.0'],
'p8_pp_Zprime_8TeV_ttbar':['8TeV Z\' -> ttbar','','','0.000566211496682','1.0','1.0'],
'p8_pp_Zprime_10TeV_ttbar':['10TeV Z\' -> ttbar','','','9.75505387797e-05','1.0','1.0'],
'p8_pp_Zprime_12TeV_ttbar':['12TeV Z\' -> ttbar','','','2.28573182133e-05','1.0','1.0'],
'p8_pp_Zprime_14TeV_ttbar':['14TeV Z\' -> ttbar','','','8.25206433493e-06','1.0','1.0'],
'p8_pp_Zprime_15TeV_ttbar':['15TeV Z\' -> ttbar','','','5.68242987936e-06','1.0','1.0'],

'p8_pp_RSGraviton_2TeV_ww':['2TeV RSG -> WW','','','0.65107','1.0','1.0'],
'p8_pp_RSGraviton_4TeV_ww':['4TeV RSG -> WW','','','0.0132603','1.0','1.0'],
'p8_pp_RSGraviton_5TeV_ww':['5TeV RSG -> WW','','','0.00314907','1.0','1.0'],
'p8_pp_RSGraviton_6TeV_ww':['6TeV RSG -> WW','','','0.00085372','1.0','1.0'],
'p8_pp_RSGraviton_8TeV_ww':['8TeV RSG -> WW','','','8.14397e-05','1.0','1.0'],
'p8_pp_RSGraviton_10TeV_ww':['10TeV RSG -> WW','','','9.31719e-06','1.0','1.0'],
'p8_pp_RSGraviton_12TeV_ww':['12TeV RSG -> WW','','','1.17012e-06','1.0','1.0'],
'p8_pp_RSGraviton_14TeV_ww':['14TeV RSG -> WW','','','1.60987e-07','1.0','1.0'],
'p8_pp_RSGraviton_15TeV_ww':['15TeV RSG -> WW','','','6.30267e-08','1.0','1.0'],

}


##list of possible decays of LHE files

decaylist = {
'mg_pp_h012j_5f_HT_0_27000':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_hh01j_5f':['hhaabb'],
'mg_pp_vbf_h01j_5f_HT_0_27000':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau', 'hnunununu'],
'mg_pp_tth01j_5f_HT_0_27000':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_bbh_4f':['haa'],
'mg_pp_vh012j_5f_HT_0_27000':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_v0123j_5f':['znunu'],
'mg_pp_z0123j_4f':['zll'],
'mg_pp_w0123j_4f':['wlv'],
'mg_pp_ttz_5f':['znunu'],
'mg_pp_hh_5f_kl_0500_5f':['haa'],
'mg_pp_hh_5f_kl_0750_5f':['haa'],
'mg_pp_hh_5f_kl_0800_5f':['haa'],
'mg_pp_hh_5f_kl_0850_5f':['haa'],
'mg_pp_hh_5f_kl_0875_5f':['haa'],
'mg_pp_hh_5f_kl_0900_5f':['haa'],
'mg_pp_hh_5f_kl_0925_5f':['haa'],
'mg_pp_hh_5f_kl_0950_5f':['haa'],
'mg_pp_hh_5f_kl_0975_5f':['haa'],
'mg_pp_hh_5f_kl_1000_5f':['haa'],
'mg_pp_hh_5f_kl_1025_5f':['haa'],
'mg_pp_hh_5f_kl_1050_5f':['haa'],
'mg_pp_hh_5f_kl_1075_5f':['haa'],
'mg_pp_hh_5f_kl_1100_5f':['haa'],
'mg_pp_hh_5f_kl_1125_5f':['haa'],
'mg_pp_hh_5f_kl_1150_5f':['haa'],
'mg_pp_hh_5f_kl_1200_5f':['haa'],
'mg_pp_hh_5f_kl_1250_5f':['haa'],
'mg_pp_hh_5f_kl_1500_5f':['haa'],

'mg_pp_tth0123j_5f':['hbb'],
'mg_pp_ttx0_cosa_-01_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-02_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-03_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-04_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-05_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-06_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-07_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-08_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-09_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_-10_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_00_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_01_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_02_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_03_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_04_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_05_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_06_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_07_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_08_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_09_0123j_5f':['x0bb'],
'mg_pp_ttx0_cosa_10_0123j_5f':['x0bb'],

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
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
}


##Gridpack list for MG5@MC@NLO
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'dummy':['','','','','',''],
'mg_pp_ee_lo':['di-electron','pT(e)>1TeV','','0.000621','1.0','1.0'],
'mg_pp_ee_5f_HT_500_1000':['ee','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_ee_5f_HT_1000_2000':['ee','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_ee_5f_HT_2000_5000':['ee','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_ee_5f_HT_5000_10000':['ee','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_ee_5f_HT_10000_27000':['ee','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_mumu_lo':['di-muon','pT(mu)>1TeV','','0.000621','1.0','1.0'],
'mg_pp_mumu_5f_HT_500_1000':['mumu','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_mumu_5f_HT_1000_2000':['mumu','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_mumu_5f_HT_2000_5000':['mumu','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_mumu_5f_HT_5000_10000':['mumu','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_mumu_5f_HT_10000_27000':['mumu','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_tautau_5f_HT_500_1000':['tautau','500 < HT < 1000','no matching','0.1267','2.00','1.0'],
'mg_pp_tautau_5f_HT_1000_2000':['tautau','1000 < HT < 2000','no matching','0.01034','2.00','1.0'],
'mg_pp_tautau_5f_HT_2000_5000':['tautau','2000 < HT < 5000','no matching','0.0006172','2.00','1.0'],
'mg_pp_tautau_5f_HT_5000_10000':['tautau','5000 < HT < 10000','no matching','2.603e-06','2.00','1.0'],
'mg_pp_tautau_5f_HT_10000_27000':['tautau','10000 < HT < 27000','no matching','6.65e-09','2.00','1.0'],

'mg_pp_tt_lo':['top pair','pT(t)>0.5TeV','','11.09','1.0','1.0'],
'mg_pp_tt_5f_HT_500_1000':['di top','500 < HT < 1000','no matching','164.4','2.00','1.0'],
'mg_pp_tt_5f_HT_1000_2000':['di top','1000 < HT < 2000','no matching','10.72','2.00','1.0'],
'mg_pp_tt_5f_HT_2000_5000':['di top','2000 < HT < 5000','no matching','0.3235','2.00','1.0'],
'mg_pp_tt_5f_HT_5000_10000':['di top','5000 < HT < 10000','no matching','0.0008756','2.00','1.0'],
'mg_pp_tt_5f_HT_10000_27000':['di top','10000 < HT < 27000','no matching','1.214e-06','2.00','1.0'],

'mg_pp_jj_lo':['di-jet','pT(j)>0.5TeV','','3871','1.0','1.0'],
'mg_pp_jj_5f_HT_500_1000':['di jet 5f','500 < HT < 1000','no matching','9.202e+04','2.00','1.0'],
'mg_pp_jj_5f_HT_1000_2000':['di jet 5f','1000 < HT < 2000','no matching','3966','2.00','1.0'],
'mg_pp_jj_5f_HT_2000_5000':['di jet 5f','2000 < HT < 5000','no matching','118','2.00','1.0'],
'mg_pp_jj_5f_HT_5000_10000':['di jet 5f','5000 < HT < 10000','no matching','0.3968','2.00','1.0'],
'mg_pp_jj_5f_HT_10000_27000':['di jet 5f','10000 < HT < 27000','no matching','0.0008586','2.00','1.0'],


'mg_pp_tth01j_5f':['higgs associated with top pair + 0/1 jets','inclusive','xqcut = 80, qCut = 120','3.274','1.22','0.612'],
'mg_pp_jjaa_5f':['dijet diphoton','','','5.941','1.2','1.0'],
'mg_pp_jjja_5f':['photon +jets','','','1.125e+04','1.2','1.0'],


# xsec is given by 2*xsec*BR(H->bb), xsec = 139.9 fb (K-factor already included below)
'mg_pp_hh_5f_kl_0500':['HH, H->bb, H undec., kl = 0.500','inclusive','','0.23823473436','1.0','1.0'],
'mg_pp_hh_5f_kl_0750':['HH, H->bb, H undec., kl = 0.750','inclusive','','0.197409636361','1.0','1.0'],
'mg_pp_hh_5f_kl_0800':['HH, H->bb, H undec., kl = 0.800','inclusive','','0.189928552157','1.0','1.0'],
'mg_pp_hh_5f_kl_0850':['HH, H->bb, H undec., kl = 0.850','inclusive','','0.18267544642','1.0','1.0'],
'mg_pp_hh_5f_kl_0875':['HH, H->bb, H undec., kl = 0.875','inclusive','','0.179134385475','1.0','1.0'],
'mg_pp_hh_5f_kl_0900':['HH, H->bb, H undec., kl = 0.900','inclusive','','0.175650319148','1.0','1.0'],
'mg_pp_hh_5f_kl_0925':['HH, H->bb, H undec., kl = 0.925','inclusive','','0.172223247436','1.0','1.0'],
'mg_pp_hh_5f_kl_0950':['HH, H->bb, H undec., kl = 0.950','inclusive','','0.168853170341','1.0','1.0'],
'mg_pp_hh_5f_kl_0975':['HH, H->bb, H undec., kl = 0.975','inclusive','','0.165540087862','1.0','1.0'],
'mg_pp_hh_5f_kl_1000':['HH, H->bb, H undec., kl = 1.000','inclusive','','0.162284','1.0','1.0'],
'mg_pp_hh_5f_kl_1025':['HH, H->bb, H undec., kl = 1.025','inclusive','','0.159084906754','1.0','1.0'],
'mg_pp_hh_5f_kl_1050':['HH, H->bb, H undec., kl = 1.050','inclusive','','0.155942808125','1.0','1.0'],
'mg_pp_hh_5f_kl_1075':['HH, H->bb, H undec., kl = 1.075','inclusive','','0.152857704111','1.0','1.0'],
'mg_pp_hh_5f_kl_1100':['HH, H->bb, H undec., kl = 1.100','inclusive','','0.149829594715','1.0','1.0'],
'mg_pp_hh_5f_kl_1125':['HH, H->bb, H undec., kl = 1.125','inclusive','','0.146858479934','1.0','1.0'],
'mg_pp_hh_5f_kl_1150':['HH, H->bb, H undec., kl = 1.150','inclusive','','0.14394435977','1.0','1.0'],
'mg_pp_hh_5f_kl_1200':['HH, H->bb, H undec., kl = 1.200','inclusive','','0.138287103291','1.0','1.0'],
'mg_pp_hh_5f_kl_1250':['HH, H->bb, H undec., kl = 1.250','inclusive','','0.132857825278','1.0','1.0'],
'mg_pp_hh_5f_kl_1500':['HH, H->bb, H undec., kl = 1.500','inclusive','','0.109131112195','1.0','1.0'],

'mg_pp_bbh_4f':['bbar plus higgs','100 < mbb < 150','','0.29200332','3.2','1.0'],
'mg_pp_vh012j_5f':['higgsstrahlung + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','7.255','1.32','1.0'],

'mg_pp_vj_lo':['boson+1jet','pT(v,j)>0.5TeV','','18.54','1.0','1.0'],
'mg_pp_vv_lo':['di-boson','pT(v)>0.5TeV','','0.1562','1.0','1.0'],
'mg_pp_vv_5f_HT_500_1000':['di boson','500 < HT < 1000','no matching','1.74','2.00','1.0'],
'mg_pp_vv_5f_HT_1000_2000':['di boson','1000 < HT < 2000','no matching','0.1483','2.00','1.0'],
'mg_pp_vv_5f_HT_2000_5000':['di boson','2000 < HT < 5000','no matching','0.008341','2.00','1.0'],
'mg_pp_vv_5f_HT_5000_10000':['di boson','5000 < HT < 10000','no matching','4.367e-05','2.00','1.0'],
'mg_pp_vv_5f_HT_10000_27000':['di boson','10000 < HT < 27000','no matching','7.496e-08','2.00','1.0'],

'mg_pp_vj_5f_HT_500_1000':['v+jet 5f','500 < HT < 1000','no matching','277.3','2.00','1.0'],
'mg_pp_vj_5f_HT_1000_2000':['v+jet 5f','1000 < HT < 2000','no matching','18.03','2.00','1.0'],
'mg_pp_vj_5f_HT_2000_5000':['v+jet 5f','2000 < HT < 5000','no matching','0.7608','2.00','1.0'],
'mg_pp_vj_5f_HT_5000_10000':['v+jet 5f','5000 < HT < 10000','no matching','0.003244','2.00','1.0'],
'mg_pp_vj_5f_HT_10000_27000':['v+jet 5f','10000 < HT < 27000','no matching','4.769e-06','2.00','1.0'],


'mg_pp_Zprime_mumu_5f_Mzp_1TeV':['1TeV Z\' mumu Flavour anomaly','inclusive','','0.0006583','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_2TeV':['2TeV Z\' mumu Flavour anomaly','inclusive','','0.0001026','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_3TeV':['3TeV Z\' mumu Flavour anomaly','inclusive','','2.514e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_4TeV':['4TeV Z\' mumu Flavour anomaly','inclusive','','8.007e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_5TeV':['5TeV Z\' mumu Flavour anomaly','inclusive','','3.289e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_6TeV':['6TeV Z\' mumu Flavour anomaly','inclusive','','1.692e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_7TeV':['7TeV Z\' mumu Flavour anomaly','inclusive','','1.073e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_8TeV':['8TeV Z\' mumu Flavour anomaly','inclusive','','8.325e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_9TeV':['9TeV Z\' mumu Flavour anomaly','inclusive','','7.295e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_10TeV':['10TeV Z\' mumu Flavour anomaly','inclusive','','6.766e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_11TeV':['11TeV Z\' mumu Flavour anomaly','inclusive','','6.549e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_12TeV':['12TeV Z\' mumu Flavour anomaly','inclusive','','6.393e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_13TeV':['13TeV Z\' mumu Flavour anomaly','inclusive','','6.313e-07','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_14TeV':['14TeV Z\' mumu Flavour anomaly','inclusive','','6.22e-07','1.0','1.0'],

'mg_pp_tvj_5f':['single top W-t','inclusive','','237.3','1.0','1.0'],
'mg_pp_tj_5f':['single top s and t channels','inclusive','','788','1.0','1.0'],

'mg_pp_llaj_mhcut_5f_HT_20_100':['l+ l- a + 1 jet' ,'20 < HT < 100','','1.842','1.5','1.0'],
'mg_pp_llaj_mhcut_5f_HT_100_400':['l+ l- a + 1 jet','100 < HT < 400','','2.0','1.5','1.0'],
# xsec to be determined
'mg_pp_llaj_mhcut_5f_HT_400_27000':['l+ l- a + 1 jet','400 < HT < 27000','','0.03989990374','1.5','1.0'],

'mg_pp_llllj_mhcut_5f_HT_20_100':['4l + 1 jet','20 < HT < 100','','0.00226','1.6','1.0'],
'mg_pp_llllj_mhcut_5f_HT_100_400':['4l + 1 jet','100 < HT < 400','','0.0004216','1.6','1.0'],
'mg_pp_llllj_mhcut_5f_HT_400_27000':['4l + 1 jet','400 < HT < 27000','','1.996e-06','1.6','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_20_100':['mu+ mu- + 1 jet','20 < HT < 100','','27.15','1.2','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_100_400':['mu+ mu- + 1 jet','100 < HT < 400','','2.34','1.2','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_400_27000':['mu+ mu- + 1 jet','400 < HT < 27000','','0.0285','1.2','1.0'],
'mg_pp_aa012j_5f_HT_0_200':['di-photon + 0/1/2 jets','0 < HT < 200','xqcut = 20, qCut = 30','1729','2.0','0.296'],
'mg_pp_aa012j_5f_HT_200_600':['di-photon + 0/1/2 jets','200 < HT < 600','xqcut = 20, qCut = 30','157.4','2.0','0.575'],
'mg_pp_aa012j_5f_HT_600_27000':['di-photon + 0/1/2 jets','600 < HT < 27000','xqcut = 20, qCut = 30','8.566','2.0','0.67'],
'mg_gg_aa01j_5f_HT_0_200':['gluon fusion di-photon + 0/1 jets','0 < HT < 200','xqcut = 20, qCut = 30','179.6','2.0','0.642'],
'mg_gg_aa01j_5f_HT_200_600':['gluon fusion di-photon + 0/1 jets','200 < HT < 600','xqcut = 20, qCut = 30','1.275','2.0','0.501'],
'mg_gg_aa01j_5f_HT_600_27000':['gluon fusion di-photon + 0/1 jets','600 < HT < 27000','xqcut = 20, qCut = 30','0.02109','2.0','0.395'],

'mg_pp_vh012j_5f_HT_0_27000':['higgsstrahlung + 0/1/2 jets','0 < HT < 27000','xqcut = 40, qCut = 60','7.255','1.32','0.64'],
'mg_pp_vbf_h01j_5f_HT_0_27000':['vbf higgs + 0/1 jets','0 < HT < 27000','xqcut = 40, qCut = 60','13.89','1.20','0.181'],
'mg_pp_h012j_5f_HT_0_27000':['gluon fusion higgs (finite mt) + 0/1/2 jets','0 < HT < 27000','xqcut = 30, qCut = 45','88.8','3.5','0.445'],
'mg_pp_tth01j_5f_HT_0_27000':['higgs associated with top pair + 0/1 jets','0 < HT < 27000','xqcut = 80, qCut = 120','3.274','1.22','0.68'],


'mg_pp_lla01j_mhcut_5f':['l+ l- a + 0/1 jet','','','5.2983058','1.5','0.848'],
'mg_pp_llaj_mhcut_5f':['l+ l- a  1 jet','','','3.62','1.5','1.0'],
'mg_pp_llll01j_mhcut_5f':['llll + 0/1 jet','','','1.999','1.5','1.0'],
'mg_pp_mumu01j_mhcut_5f':['mumu + 0/1 jet','','','1.999','1.5','1.0'],

'mg_pp_tt_nlo':['','','','6.793e-02','',''],
'mg_pp_tt012j_5f':['','','','3806','',''],
'mg_pp_tt0123j_4f':['','','','3935','',''],
'mg_pp_t123j_5f':['single top (s,t channels) + 1/2/3 jets','inclusive','','1134','',''],
'mg_pp_ttbb_4f':['tt + bbin4f','','','36.69','',''],
'mg_pp_ttw_5f':['ttW','inclusive','','1.128','',''],
'mg_pp_ttww_4f':['ttWW (4FS)','inclusive','','0.05022','',''],
'mg_pp_ttwz_5f':['ttWZ','inclusive','','0.01045','',''],
'mg_pp_ttz_5f':['ttZ','inclusive','','3.07','',''],
'mg_pp_ttzz_5f':['ttZZ','inclusive','','0.008556','',''],
'mg_pp_tv012j_5f':['top pair off-shell t* -> Wj + 0/1/2 jets','inclusive','','411','',''],
'mg_pp_vv012j_5f':['di-vector boson + 0/1/2 jets','inclusive','','1.01e+04','',''],
'mg_pp_w0123j_4f':['w + 0/1/2/3 jets','inclusive','','4.184e+05','',''],
'mg_pp_z0123j_4f':['z + 0/1/2/3 jets','inclusive','','1.292e+05','',''],
'mg_pp_jj_lo_PT_30_inf':['','pT > 30GeV','','1.933e+08','',''],
'mg_pp_jjj_5f':['tri-jet','pT(leading) > 500GeV','','1.006e+04','',''],
'mg_pp_tth0123j_5f':['','','','3.916','',''],
'mg_pp_tth0123j_hbb_5f':['','','','3.916','',''],

'mg_pp_ttx0_cosa_-01_0123j_5f':['','','','1.928','',''],
'mg_pp_ttx0_cosa_-02_0123j_5f':['','','','1.992','',''],
'mg_pp_ttx0_cosa_-03_0123j_5f':['','','','2.086','',''],
'mg_pp_ttx0_cosa_-04_0123j_5f':['','','','2.245','',''],
'mg_pp_ttx0_cosa_-05_0123j_5f':['','','','2.418','',''],
'mg_pp_ttx0_cosa_-06_0123j_5f':['','','','2.651','',''],
'mg_pp_ttx0_cosa_-07_0123j_5f':['','','','2.922','',''],
'mg_pp_ttx0_cosa_-08_0123j_5f':['','','','3.234','',''],
'mg_pp_ttx0_cosa_-09_0123j_5f':['','','','3.589','',''],
'mg_pp_ttx0_cosa_-10_0123j_5f':['','','','3.996','',''],
'mg_pp_ttx0_cosa_00_0123j_5f':['','','','1.908','',''],
'mg_pp_ttx0_cosa_01_0123j_5f':['','','','1.929','',''],
'mg_pp_ttx0_cosa_02_0123j_5f':['','','','1.992','',''],
'mg_pp_ttx0_cosa_04_0123j_5f':['','','','2.244','',''],
'mg_pp_ttx0_cosa_05_0123j_5f':['','','','2.419','',''],
'mg_pp_ttx0_cosa_06_0123j_5f':['','','','2.65','',''],
'mg_pp_ttx0_cosa_07_0123j_5f':['','','','2.923','',''],
'mg_pp_ttx0_cosa_08_0123j_5f':['','','','3.235','',''],
'mg_pp_ttx0_cosa_09_0123j_5f':['','','','3.587','',''],
'mg_pp_ttx0_cosa_10_0123j_5f':['','','','3.996','',''],

'mg_pp_ttx0_cosa_-01_0123j_x0bb_5f':['','','','1.928','',''],
'mg_pp_ttx0_cosa_-02_0123j_x0bb_5f':['','','','1.992','',''],
'mg_pp_ttx0_cosa_-03_0123j_x0bb_5f':['','','','2.086','',''],
'mg_pp_ttx0_cosa_-04_0123j_x0bb_5f':['','','','2.245','',''],
'mg_pp_ttx0_cosa_-05_0123j_x0bb_5f':['','','','2.418','',''],
'mg_pp_ttx0_cosa_-06_0123j_x0bb_5f':['','','','2.651','',''],
'mg_pp_ttx0_cosa_-07_0123j_x0bb_5f':['','','','2.922','',''],
'mg_pp_ttx0_cosa_-08_0123j_x0bb_5f':['','','','3.234','',''],
'mg_pp_ttx0_cosa_-09_0123j_x0bb_5f':['','','','3.589','',''],
'mg_pp_ttx0_cosa_-10_0123j_x0bb_5f':['','','','3.996','',''],
'mg_pp_ttx0_cosa_00_0123j_x0bb_5f':['','','','1.908','',''],
'mg_pp_ttx0_cosa_01_0123j_x0bb_5f':['','','','1.929','',''],
'mg_pp_ttx0_cosa_02_0123j_x0bb_5f':['','','','1.992','',''],
'mg_pp_ttx0_cosa_04_0123j_x0bb_5f':['','','','2.244','',''],
'mg_pp_ttx0_cosa_05_0123j_x0bb_5f':['','','','2.419','',''],
'mg_pp_ttx0_cosa_06_0123j_x0bb_5f':['','','','2.65','',''],
'mg_pp_ttx0_cosa_07_0123j_x0bb_5f':['','','','2.923','',''],
'mg_pp_ttx0_cosa_08_0123j_x0bb_5f':['','','','3.235','',''],
'mg_pp_ttx0_cosa_09_0123j_x0bb_5f':['','','','3.587','',''],
'mg_pp_ttx0_cosa_10_0123j_x0bb_5f':['','','','3.996','',''],

}


