indir ='/eos/fcc/hh/generation/mg5_amcatnlo/gridpacks/'
outdir='/eos/fcc/hh/generation/mg5_amcatnlo/lhe/'

version='v0_0'
outdir_delphes='/eos/fcc/hh/generation/DelphesEvents/%s/'%version


gridpacklist = {
'pp_tt012j_5f':['ttbar + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 10, qCut = 15'],
'pp_w012j_5f':['w + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 10, qCut = 15'],
'pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 10, qCut = 15'],
'pp_tt012j_5f_v2':['ttbar + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 60, qCut = 90'],
'pp_w012j_5f_v2':['w + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 30, qCut = 45'],
'pp_z012j_5f_v2':['z + 0,1,2 jets 5 flavor scheme','inclusive decays','xqcut = 30, qCut = 45'],
'pp_jj012j_5f':['dijet + 0,1,2 jets 5 flavor scheme','',''],
'pp_hh_bbaa':['gluon gluon fusion di-higgs','bbbar gammagamma',''],
'pp_jjaa01j_5f':['dijet diphoton + 0,1,2 jets 5 flavor scheme','','']
}

