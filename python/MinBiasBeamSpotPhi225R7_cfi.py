import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_100_1_KIc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_101_1_5hK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_102_1_zoZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_103_1_Wli.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_105_1_TwF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_106_1_nfB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_107_1_PBJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_108_1_WUW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_109_1_877.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_10_1_7Bk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_110_1_woR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_111_1_YyK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_112_1_qrX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_113_1_GXT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_114_1_R2s.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_115_1_xuJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_116_1_oEv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_117_1_yo2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_118_1_y77.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_119_1_HYh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_11_1_wuV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_120_1_56y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_121_1_Ysg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_122_1_uqL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_123_1_tsr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_124_1_aRe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_125_1_MXj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_126_1_Y08.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_127_1_WH1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_128_1_PCx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_129_1_rL3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_12_1_WN4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_130_1_9rM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_131_1_g8b.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_132_1_cLM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_133_1_xfh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_134_1_a1p.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_135_1_AZj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_136_1_ejj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_137_1_aEf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_138_1_SIE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_139_1_k2Q.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_13_1_cHN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_140_1_T8z.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_141_1_qRU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_142_1_jOR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_143_1_TnJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_144_1_ga7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_145_1_k6b.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_146_1_UIv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_147_1_1ur.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_148_1_Xdx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_149_1_r9b.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_14_1_5wi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_150_1_IRR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_151_1_bTB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_152_1_x1k.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_153_1_HeI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_154_1_4sl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_155_1_JVA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_156_1_gGh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_157_1_5SG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_158_1_pL3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_159_1_XMl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_15_1_L8y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_160_1_uLI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_161_1_sZM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_162_1_Rru.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_163_1_aT9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_164_1_0LF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_165_1_NOA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_166_1_cLR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_167_1_ti2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_168_1_KcK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_169_1_hPf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_16_1_OZF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_170_1_UfF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_171_1_9B3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_172_1_zHv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_173_1_E2E.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_174_1_LCD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_175_1_lX7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_176_1_PDi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_177_1_mO5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_178_1_B7p.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_179_1_qt0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_17_1_dAo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_180_1_pD7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_181_1_7fH.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_182_1_xJo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_183_1_sc6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_184_1_512.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_185_1_rSB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_186_1_acX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_187_1_bY6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_188_1_nsr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_189_1_wwq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_18_1_xIp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_190_1_gLv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_191_1_Fey.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_192_1_a6T.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_193_1_ugV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_194_1_oJe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_195_1_wiF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_196_1_J4W.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_197_1_DPf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_198_1_H3h.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_199_1_8c8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_19_1_LOl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_1_1_P52.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_200_1_5AG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_20_1_PeQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_21_1_cdA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_22_1_870.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_23_1_CVD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_24_1_w8y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_25_1_yh0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_26_1_fm6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_27_1_cc3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_28_1_mKY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_29_1_FW4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_2_1_v1l.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_30_1_rgG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_31_1_Gj4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_32_1_yG3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_33_1_YAh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_34_1_DaG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_35_1_qto.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_36_1_5GU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_37_1_OaU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_38_1_7WL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_39_1_vce.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_3_1_gMD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_40_1_x82.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_41_1_0qP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_42_1_VNu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_43_1_Zie.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_44_1_zsN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_45_1_Q47.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_46_1_Hzj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_47_1_IZF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_48_1_4lU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_49_1_myA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_4_1_3Dd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_50_1_1As.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_51_1_nXO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_52_1_3gU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_53_1_hne.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_54_1_WVX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_55_1_Sk6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_56_1_dEc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_57_1_j41.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_58_1_DPQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_59_1_7l9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_5_1_ZrY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_60_1_5A8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_61_1_s1D.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_62_1_BSf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_63_1_bli.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_64_1_p1L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_65_1_uJm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_66_1_Nas.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_67_1_C6j.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_68_1_v3L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_69_1_ppy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_6_1_lZO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_70_1_pwB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_71_1_xhu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_72_1_K90.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_73_1_5O4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_74_1_14D.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_75_1_gYN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_76_1_WEw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_77_1_nuq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_78_1_ly0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_79_1_ztl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_7_1_s7V.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_80_1_KiT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_81_1_u20.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_82_1_Bsc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_83_1_1WR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_84_1_Tu6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_85_1_xvJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_86_1_7Ew.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_87_1_klu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_88_1_O9d.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_89_1_60F.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_8_1_X5I.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_90_1_JtX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_91_1_DVC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_92_1_K1a.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_93_1_sxs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_94_1_mJl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_95_1_4lQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_96_1_x5W.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_97_1_Tlg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_98_1_7sc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_99_1_p1z.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi225R7_HISTATS/outfile14TeVSKIM_9_1_yzM.root',
	)

)
