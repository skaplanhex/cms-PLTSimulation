import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_100_1_AyW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_10_1_jrC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_11_1_9AC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_12_1_4hr.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_13_1_HH0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_14_1_WeM.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_15_1_SL8.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_16_1_QwG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_17_1_nfo.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_18_1_D1B.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_19_1_gvZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_1_1_zOR.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_20_1_jVe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_21_1_zSL.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_22_1_YRq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_23_1_dJC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_24_1_ePU.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_25_1_Axa.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_26_1_izk.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_27_1_XAp.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_28_1_uAK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_29_1_SSb.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_2_1_6YY.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_30_1_OcZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_31_1_leT.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_32_1_L8J.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_33_1_G7G.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_34_1_8Zq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_35_1_WpL.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_36_1_k5N.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_37_1_LT2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_38_1_tVt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_39_1_Qw1.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_3_1_pak.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_40_1_OiN.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_41_1_2FW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_42_1_QQw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_43_1_Pae.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_44_1_lXj.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_45_1_YGs.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_46_1_SWw.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_47_1_41t.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_48_1_Miq.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_49_1_jAh.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_4_1_x6T.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_50_1_G9C.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_51_1_oV6.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_52_1_frs.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_53_1_Z2C.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_54_1_R9Z.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_55_1_QPt.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_56_1_19b.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_57_1_Ws2.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_58_1_JHJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_59_1_wyj.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_5_1_9z3.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_60_1_cps.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_61_1_TKd.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_62_1_X1q.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_63_1_IE5.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_64_1_See.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_65_1_nlx.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_66_1_orJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_67_1_Wi1.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_68_1_BuC.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_69_1_nYe.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_6_1_eUZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_70_1_ykB.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_71_1_hCS.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_72_1_z4x.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_73_1_Msn.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_74_1_srb.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_75_1_U6x.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_76_1_3wD.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_77_1_iw4.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_78_1_T0z.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_79_1_GTG.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_7_1_l8u.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_80_1_5Ow.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_81_1_X0g.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_82_1_LFI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_83_1_EO0.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_84_1_al9.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_85_1_sYv.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_86_1_sHK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_87_1_j4p.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_88_1_xQ7.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_89_1_vnD.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_8_1_HhQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_90_1_rZI.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_91_1_xw1.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_92_1_zHW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_93_1_egZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_94_1_B44.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_95_1_ttW.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_96_1_xiE.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_97_1_89t.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_98_1_oI7.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_99_1_xKK.root',
        '/store/user/skaplan/noreplica/MuonGunPt05/FullEta_FullPhi_LargeSigmaZ/MuonGunEvents_9_1_93Z.root',
    )

)
