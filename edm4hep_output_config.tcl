
module EDM4HepOutput EDM4HepOutput {
    add ReconstructedParticleCollections EFlowTrack EFlowPhoton EFlowNeutralHadron 
    add GenParticleCollections           Particle
    add JetCollections                   Jet JetNoIso
    add MuonCollections                  Muon MuonNoIso 
    add ElectronCollections              Electron ElectronNoIso 
    add PhotonCollections                Photon PhotonNoIso 
    add MissingETCollections             MissingET
    add ScalarHTCollections              ScalarHT
    set RecoParticleCollectionName       ReconstructedParticles
    set MCRecoAssociationCollectionName  MCRecoAssociations
}
