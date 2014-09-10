import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_100_1_xot.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_10_1_3kq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_11_1_YNV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_12_1_j0r.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_13_1_qfZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_14_1_1y9.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_15_1_pwj.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_16_1_VSN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_17_1_RdL.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_18_1_BMP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_19_1_hWK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_1_1_Wzj.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_20_1_jaF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_21_1_tOy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_22_1_KMn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_23_1_WTT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_24_1_sOe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_25_1_O5t.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_26_1_4Nk.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_27_1_0tn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_28_1_Fhd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_29_1_KcV.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_2_1_fP0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_30_1_wmF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_31_1_RRh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_32_1_NCn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_33_1_0pC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_34_1_G68.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_35_1_l1H.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_36_1_RJR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_37_1_T6U.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_38_1_8FB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_39_1_sUk.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_3_1_oCc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_40_1_4sf.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_41_1_nlP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_42_1_skP.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_43_1_7Sw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_44_1_VFX.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_45_1_AIk.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_46_1_fjp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_47_1_edp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_48_1_Old.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_49_1_HUl.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_4_1_YmF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_50_1_ama.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_51_1_m0F.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_52_1_IQz.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_53_1_No2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_54_1_Q5x.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_55_1_FEE.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_56_1_o28.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_57_1_Y5i.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_58_1_wof.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_59_1_QVf.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_5_1_IF7.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_60_1_dJy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_61_1_L70.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_62_1_NfM.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_63_1_FXB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_64_1_iY0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_65_1_BOy.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_66_1_zbT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_67_1_RWU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_68_1_x8n.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_69_1_IrH.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_6_1_rcF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_70_1_DIe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_71_1_yXJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_72_1_nX7.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_73_1_kIl.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_74_1_Yms.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_75_1_7wU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_76_1_fgF.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_77_1_bPr.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_78_1_fD0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_79_1_MBY.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_7_1_qFI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_80_1_eHD.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_81_1_9b2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_82_1_Sxc.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_83_1_2Nd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_84_1_Wq9.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_85_1_zh1.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_86_1_d9B.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_87_1_eu8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_88_1_aFW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_89_1_AvQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_8_1_uGw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_90_1_u4A.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_91_1_2Fo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_92_1_ZKE.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_93_1_ZYt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_94_1_R2l.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_95_1_rg5.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_96_1_BmT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_97_1_DNS.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_98_1_fha.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_99_1_Fxf.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/CenterEta_CenterPhi_20SigmaZ/MuonGunEvents_9_1_AXS.root',
    )

)
