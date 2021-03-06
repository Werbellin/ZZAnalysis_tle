
#LEPTON_SETUP = 2016
#ELECORRTYPE = "None" # "None" to switch off
#ELEREGRESSION = "None" # Not supported as of 2016
#APPLYMUCORR = False # Switch off muon scale corrections
#BUNCH_SPACING = 25
#FSRMODE = "RunII" # only Run II supported as of 2016
#KINREFIT = False  # control KinZFitter (very slow)
#PROCESS_CR = True # Uncomment to run CR paths and trees
#ADDLOOSEELE = True # Run paths for loose electrons
#APPLYTRIG = False  # must set to False for all MC samples except MINIAODv2-reHLT

PD = ""
MCFILTER = ""

#KEEPLOOSECOMB = True # Do not skip loose lepton ZZ combinations (for debugging

#For DATA: 
#IsMC = False
#PD = "DoubleEle"

# Get absolute path
import os
PyFilePath = os.environ['CMSSW_BASE'] + "/src/ZZAnalysis/AnalysisStep/test/"

### ----------------------------------------------------------------------
### Standard sequence
### ----------------------------------------------------------------------

execfile(PyFilePath + "analyzer.py")

process.source.inputCommands = cms.untracked.vstring("keep *", "drop LHERunInfoProduct_*_*_*", "drop LHEEventProduct_*_*_*")

### ----------------------------------------------------------------------
### Replace parameters
### ----------------------------------------------------------------------

process.source.fileNames = cms.untracked.vstring(

    ## Spring16 MiniAODv1 files for synchronization
#    '/store/mc/RunIISpring16MiniAODv1/VBF_HToZZTo4L_M190_13TeV_powheg2_JHUgenV6_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/00000/28ADE6D5-021F-E611-B1A4-00145E5521B9.root',
#    '/store/mc/RunIISpring16MiniAODv1/WminusH_HToZZTo4L_M150_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_v3-v1/00000/C6DF34D4-CF20-E611-A8EE-782BCB27B958.root'
    ## High-mass sync file
#    '/store/mc/RunIISpring16MiniAODv2/Graviton2PBToZZTo4L_width0p1_M-2000_13TeV-JHUgenV6-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/00000/EC1FA990-8A24-E611-9E70-0025905A48F2.root'


    ## reHLT miniAODv2 files for sync   
    '/store/mc/RunIISpring16MiniAODv2/VBF_HToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/9AEF77A8-4B3B-E611-97F0-44A842240F8D.root',
    '/store/mc/RunIISpring16MiniAODv2/WminusH_HToZZTo4L_M125_13TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/FE43CA0A-993A-E611-91FB-0242AC130002.root'

    ## High-mass reHLT sync file
#'/store/mc/RunIISpring16MiniAODv2/Graviton2PBToZZTo4L_width0p1_M-2000_13TeV-JHUgenV6-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/EC5DACC2-7539-E611-9499-001C23BED42C.root'

    )

process.calibratedPatElectrons.isSynchronization = cms.bool(True)
process.calibratedMuons.isSynchronization = cms.bool(True)

process.maxEvents.input = -1
#process.source.skipEvents = cms.untracked.uint32(5750)

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000


### ----------------------------------------------------------------------
### Analyzer for Plots
### ----------------------------------------------------------------------


#process.source.eventsToProcess = cms.untracked.VEventRange("1:8670")

# Debug
process.dumpUserData =  cms.EDAnalyzer("dumpUserData",
     dumpTrigger = cms.untracked.bool(True),
     muonSrcs = cms.PSet(
#       slimmedMuons = cms.InputTag("slimmedMuons"),
        muons = cms.InputTag("appendPhotons:muons"),
     ),
     electronSrcs = cms.PSet(
#       slimmedElectron = cms.InputTag("slimmedElectrons"),
        electrons = cms.InputTag("appendPhotons:electrons"),
#        RSE = cms.InputTag("appendPhotons:looseElectrons"),
#        TLE = cms.InputTag("appendPhotons:electronstle"), #These are actually photons, should add a photonSrcs section for them.
     ),
     candidateSrcs = cms.PSet(
        Z     = cms.InputTag("ZCand"),
#        ZRSE     = cms.InputTag("ZCandlooseEle"),
#        ZTLE     = cms.InputTag("ZCandtle"),
        ZZ  = cms.InputTag("ZZCand"),
#        ZZRSE     = cms.InputTag("ZZCandlooseEle"),
#        ZZTLE     = cms.InputTag("ZZCandtle"),
#        ZLL  = cms.InputTag("ZLLCand"),
#        ZL  = cms.InputTag("ZlCand"),
     ),
     jetSrc = cms.InputTag("cleanJets"),
)

# Create lepton sync file
#process.PlotsZZ.dumpForSync = True;
#process.p = cms.EndPath( process.PlotsZZ)

# Keep all events in the tree, even if no candidate is selected
#process.ZZTree.skipEmptyEvents = False

# replace the paths in analyzer.py
#process.trees = cms.EndPath(process.ZZTree)

#Dump reconstructed variables
#process.appendPhotons.debug = cms.untracked.bool(True)
#process.fsrPhotons.debug = cms.untracked.bool(True)
#process.dump = cms.Path(process.dumpUserData)

#Print MC history
#process.mch = cms.EndPath(process.printTree)


#Monitor memory usage
#process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",
#    ignoreTotal = cms.untracked.int32(1)
#)
