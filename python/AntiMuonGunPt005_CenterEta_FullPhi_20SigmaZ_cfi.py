import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_100_1_9ti.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_10_1_pNQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_11_1_hQW.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_12_1_pdZ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_13_1_rw6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_14_1_xji.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_15_1_NP8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_16_1_zps.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_17_1_QuF.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_18_1_1NE.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_19_1_X00.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_1_1_iMQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_20_1_Lud.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_21_1_gAn.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_22_1_LsU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_23_1_G2n.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_24_1_8TL.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_25_1_EDm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_26_1_T7G.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_27_1_3Kv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_28_1_s5W.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_29_1_WX5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_2_1_sNQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_30_1_n7N.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_31_1_4zB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_32_1_rpn.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_33_1_sF6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_34_1_mng.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_35_1_hhN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_36_1_uck.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_37_1_r5R.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_38_1_plT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_39_1_L0M.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_3_1_ZLv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_40_1_5xj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_41_1_fb6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_42_1_QOC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_43_1_GEQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_44_1_VKm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_45_1_fUi.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_46_1_snQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_47_1_wSR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_48_1_GHB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_49_1_ER9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_4_1_5uA.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_50_1_2XW.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_51_1_ezd.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_52_1_GLL.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_53_1_WwR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_54_1_IPN.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_55_1_p53.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_56_1_yQR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_57_1_147.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_58_1_ozk.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_59_1_yA9.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_5_1_y7M.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_60_1_wvw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_61_1_cfS.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_62_1_sus.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_63_1_cii.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_64_1_5ji.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_65_1_HCF.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_66_1_YrC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_67_1_7T7.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_68_1_6WT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_69_1_kPe.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_6_1_g3U.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_70_1_ZNC.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_71_1_WR6.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_72_1_Hs8.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_73_1_Fvs.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_74_1_Sfm.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_75_1_YMj.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_76_1_0BB.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_77_1_TAf.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_78_1_mT1.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_79_1_cb5.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_7_1_D2D.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_80_1_rMR.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_81_1_9S2.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_82_1_V51.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_83_1_YzU.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_84_1_yk3.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_85_1_Chv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_86_1_YVk.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_87_1_hme.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_88_1_pqw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_89_1_Etb.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_8_1_tEQ.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_90_1_Riw.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_91_1_asT.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_92_1_7AD.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_93_1_Tky.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_94_1_96O.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_95_1_hrv.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_96_1_y55.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_97_1_I30.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_98_1_JlK.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_99_1_VZg.root',
        '/store/user/skaplan/noreplica/AntiMuonGunPt005/CenterEta_FullPhi_20SigmaZ/MuonGunEvents_9_1_oIq.root',
    )

)
