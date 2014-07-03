import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_100_1_PiG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_101_1_LBd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_102_1_rQ1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_103_1_5q7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_104_1_n4n.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_105_1_STU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_106_1_vdC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_107_1_rLu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_108_1_tK4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_109_1_kE6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_10_1_Enf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_110_1_MA8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_111_1_rCt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_112_1_GQd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_113_1_rk6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_114_1_Kuq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_115_1_ygW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_116_1_Kbe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_117_1_CcD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_118_1_AKI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_119_1_Ae2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_11_1_SUE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_120_1_lOQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_121_1_l6Q.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_122_1_AAV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_123_1_QFl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_124_1_pZL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_125_1_qy6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_126_1_BZQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_127_1_FJZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_128_1_HcJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_129_1_1ZX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_12_1_CIn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_130_1_Hvf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_131_1_Gqb.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_132_1_25F.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_133_1_Xoy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_134_1_kl4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_135_1_5U0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_136_1_025.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_137_1_1wQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_138_1_C3C.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_139_1_6Lu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_13_1_UZm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_140_1_Afo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_141_1_DE4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_142_1_EdV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_143_1_lIM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_144_1_PII.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_145_1_KAk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_146_1_Vd2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_147_1_64A.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_148_1_VCt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_149_1_UuG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_14_1_cnI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_150_1_ViJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_151_1_A6Y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_152_1_uz3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_153_1_PFe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_154_1_RYz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_155_1_Pzo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_156_1_Jry.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_157_1_qYm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_158_1_Em5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_159_1_cin.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_15_1_sgp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_160_1_ch3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_161_1_cUh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_162_1_sgI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_163_1_5L4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_164_1_ikU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_165_1_RWM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_166_1_wpQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_167_1_wNn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_168_1_Lio.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_169_1_h7M.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_16_1_IjB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_170_1_pfV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_171_1_ex0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_172_1_64H.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_173_1_Byl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_174_1_lF4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_175_1_3gp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_176_1_Y1J.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_177_1_Ivt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_178_1_EcR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_179_1_Jb0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_17_1_znS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_180_1_B0E.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_181_1_eT7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_182_1_P5I.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_183_1_HU8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_184_1_h2J.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_185_1_NyL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_186_1_QyU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_187_1_pyi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_188_1_d39.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_189_1_a4a.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_18_1_ziZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_190_1_uJv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_191_1_JTS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_192_1_pwK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_194_1_dXq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_195_1_YQ0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_196_1_vp0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_197_1_Led.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_198_1_pAW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_199_1_LTo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_19_1_Sqm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_1_1_B5Q.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_200_1_T8g.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_20_1_PKj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_21_1_Xqm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_22_1_hVc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_23_1_fq5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_24_1_VIz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_25_1_ne3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_26_1_wfs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_27_1_SIK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_28_1_ba1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_29_1_ZcU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_2_1_Pun.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_30_1_AQC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_31_1_eTT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_32_1_dVw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_33_1_TFR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_34_1_b4G.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_35_1_d5U.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_36_1_IW1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_37_1_SbK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_38_1_udf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_39_1_HR8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_3_1_9y2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_40_1_zCr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_41_1_oiz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_42_1_BSr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_43_1_87r.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_44_1_2Lq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_45_1_ZkE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_46_1_Ukq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_47_1_HTr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_48_1_cfg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_49_1_pIj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_4_1_Uv9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_50_1_l7L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_51_1_Xrl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_52_1_Fw1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_53_1_cFl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_54_1_JII.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_55_1_LM7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_56_1_6gJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_57_1_vz5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_58_1_b17.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_59_1_WDB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_5_1_58V.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_60_1_VDN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_61_1_6HE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_62_1_SbM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_63_1_XDV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_64_1_Vsm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_65_1_VFI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_66_1_qdw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_67_1_soe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_68_1_Qcy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_69_1_hUr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_6_1_Llo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_70_1_o4N.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_71_1_xkT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_72_1_ukj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_73_1_h7z.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_74_1_9wv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_75_1_2re.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_76_1_AxE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_77_1_l25.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_78_1_08D.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_79_1_x3i.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_7_1_Oq1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_80_1_j0e.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_81_1_U9Y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_82_1_Nxa.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_83_1_3G5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_84_1_egz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_85_1_fb4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_86_1_LUl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_87_1_bIG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_88_1_cLn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_89_1_zKD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_8_1_Loc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_90_1_ykE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_91_1_mis.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_92_1_4xw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_93_1_BQx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_94_1_ha1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_95_1_JgD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_96_1_CKu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_97_1_sdC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_98_1_WIJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_99_1_MzX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R2_HISTATS/outfile14TeVSKIM_9_1_ufO.root',
	)

)
