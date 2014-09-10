import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_100_1_92z.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_10_1_I1O.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_11_1_I4F.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_12_1_ZOZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_13_1_2FS.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_14_1_mup.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_15_1_Hsj.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_16_1_Jfe.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_17_1_Oim.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_18_1_HnB.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_19_1_iWt.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_1_1_SgF.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_20_1_515.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_21_1_bIT.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_22_1_opM.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_23_1_Uwx.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_24_1_ymQ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_25_1_4Eu.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_26_1_OGD.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_27_1_Gct.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_28_1_0Ko.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_29_1_ZSK.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_2_1_KAD.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_30_1_fL4.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_31_1_sUu.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_32_1_sR7.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_33_1_OTh.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_34_1_eCd.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_35_1_xFP.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_36_1_9xB.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_37_1_3qz.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_38_1_Mk8.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_39_1_o7X.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_3_1_y5u.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_40_1_O7P.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_41_1_ioM.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_42_1_TBw.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_43_1_NGl.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_44_1_yj9.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_45_1_ir7.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_46_1_BqN.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_47_1_esd.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_48_1_HHy.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_49_1_4in.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_4_1_THP.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_50_1_f5W.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_51_1_gIP.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_52_1_ru9.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_53_1_84l.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_54_1_ru1.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_55_1_Iko.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_56_1_KVs.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_57_1_NJK.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_58_1_uuV.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_59_1_Qwh.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_5_1_Ulr.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_60_1_WF1.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_61_1_iZ7.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_62_1_myJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_63_1_pIf.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_64_1_zPJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_65_1_oFX.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_66_1_tK5.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_67_1_Yhl.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_68_1_33v.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_69_1_BV9.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_6_1_mFa.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_70_1_q9M.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_71_1_pXD.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_72_1_STy.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_73_1_vEI.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_74_1_v3a.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_75_1_R02.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_76_1_Tjw.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_77_1_wjf.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_78_1_xhm.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_79_1_Y4G.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_7_1_AVm.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_80_1_MPN.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_81_1_ZkM.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_82_1_RuD.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_83_1_uOd.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_84_1_ms6.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_85_1_MhK.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_86_1_7XV.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_87_1_OKZ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_88_1_V5n.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_89_1_otd.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_8_1_ZxI.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_90_1_GIv.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_91_1_7LE.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_92_1_5Xz.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_93_1_M9V.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_94_1_hdK.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_95_1_N4E.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_96_1_kQD.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_97_1_ADJ.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_98_1_lf2.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_99_1_hwM.root',
        '/store/user/skaplan/noreplica/MuonGunPt50/FullEta_FullPhi_20SigmaZ/MuonGunEvents_9_1_n6X.root',
    )

)
