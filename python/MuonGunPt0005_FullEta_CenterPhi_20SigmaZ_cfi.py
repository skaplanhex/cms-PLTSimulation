import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_100_1_hz9.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_10_1_6A7.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_11_1_2OL.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_12_1_75I.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_13_1_6Dc.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_14_1_yb9.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_15_1_Dmm.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_16_1_QQe.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_17_1_0zl.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_18_1_DL3.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_19_1_ezL.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_1_1_67h.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_20_1_0W2.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_21_1_za0.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_22_1_AUi.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_23_1_vNR.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_24_1_gTw.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_25_1_3TB.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_26_1_U4C.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_27_1_TSt.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_28_1_jdg.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_29_1_nKk.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_2_1_NXG.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_30_1_HOX.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_31_1_Ls3.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_32_1_Igp.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_33_1_8Mg.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_34_1_663.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_35_1_Ldc.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_36_1_wUh.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_37_1_ngV.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_38_1_IHW.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_39_1_XBq.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_3_1_mzl.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_40_1_rUj.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_41_1_wGm.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_42_1_6L5.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_43_1_BZ8.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_44_1_jPU.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_45_1_px1.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_46_1_RWc.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_47_1_C0k.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_48_1_uyN.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_49_1_Qgp.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_4_1_KYA.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_50_1_EUs.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_51_1_DEX.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_52_1_rbr.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_53_1_iEH.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_54_1_tzr.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_55_1_nHj.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_56_1_1Ff.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_57_1_3Pr.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_58_1_WZ5.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_59_1_RHN.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_5_1_HfH.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_60_1_Bap.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_61_1_CXH.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_62_1_Nki.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_63_1_AQu.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_64_1_qOE.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_65_1_5HW.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_66_1_hvu.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_67_1_BPv.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_68_1_Cbn.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_69_1_Z57.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_6_1_Gx1.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_70_1_B68.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_71_1_fg8.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_72_1_7ic.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_73_1_qK3.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_74_1_GmX.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_75_1_NuJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_76_1_8Z2.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_77_1_ld3.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_78_1_mjI.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_79_1_sJa.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_7_1_EEo.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_80_1_ZPE.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_81_1_yVQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_82_1_oMG.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_83_1_pJd.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_84_1_Rv4.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_85_1_IIv.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_86_1_hhu.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_87_1_JKV.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_88_1_2N2.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_89_1_nMX.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_8_1_nTs.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_90_1_w3s.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_91_1_76s.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_92_1_hLN.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_93_1_Ffz.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_94_1_aiR.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_95_1_phE.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_96_1_cjq.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_97_1_SdQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_98_1_CBa.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_99_1_MPH.root',
        '/store/user/skaplan/noreplica/MuonGunPt0005/FullEta_CenterPhi_20SigmaZ/MuonGunEvents_9_1_epB.root',
    )

)