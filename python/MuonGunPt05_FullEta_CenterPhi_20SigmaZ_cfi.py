import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_100_1_kBh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_10_1_AMq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_11_1_Oxu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_12_1_d7C.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_13_1_2VL.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_14_1_IbZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_15_1_iUN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_16_1_jzK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_17_1_rl8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_18_1_vb3.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_19_1_8DZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_1_1_FBN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_20_1_GD3.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_21_1_Uqn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_22_1_RMT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_23_1_L3f.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_24_1_66o.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_25_1_FVr.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_26_1_7Da.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_27_1_cQM.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_28_1_Iom.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_29_1_VUO.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_2_1_Zlb.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_30_1_96S.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_31_1_5sv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_32_1_pwP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_33_1_6ru.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_34_1_785.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_35_1_ctQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_36_1_yWH.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_37_1_eLZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_38_1_p4e.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_39_1_30D.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_3_1_eNY.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_40_1_Qoo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_41_1_F6b.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_42_1_XCG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_43_1_n5Y.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_44_1_KB5.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_45_1_5ZK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_46_1_Hdn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_47_1_KOJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_48_1_xSI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_49_1_cDr.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_4_1_ouT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_50_1_eTK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_51_1_p0C.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_52_1_DNO.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_53_1_Cug.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_54_1_8gJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_55_1_RAu.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_56_1_hgR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_57_1_3bT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_58_1_q9r.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_59_1_SAn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_5_1_dwT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_60_1_YtU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_61_1_M6d.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_62_1_zCF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_63_1_q2n.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_64_1_KRS.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_65_1_X7Q.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_66_1_BPy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_67_1_0BZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_68_1_X94.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_69_1_X7r.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_6_1_WUz.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_70_1_f1j.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_71_1_p4O.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_72_1_aE8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_73_1_wbA.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_74_1_lpd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_75_1_pAN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_76_1_zDb.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_77_1_bx6.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_78_1_s9J.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_79_1_2vF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_7_1_VTG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_80_1_fPO.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_81_1_OMJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_82_1_GGe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_83_1_Iiq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_84_1_1R5.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_85_1_jyN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_86_1_hPi.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_87_1_MYC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_88_1_yxQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_89_1_wWy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_8_1_jih.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_90_1_9fd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_91_1_n1d.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_92_1_7Xq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_93_1_eao.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_94_1_yMJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_95_1_8qP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_96_1_qOt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_97_1_gNv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_98_1_efX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_99_1_yWx.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_9_1_VvV.root',
    )

)