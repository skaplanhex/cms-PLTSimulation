import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_100_1_KFp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_101_1_L1L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_102_1_2k8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_103_1_ZgU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_104_1_ajY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_105_1_hT3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_106_1_C9y.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_107_1_Jz1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_108_1_ugF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_109_1_F5l.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_10_1_1FY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_110_1_3lM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_111_1_4LZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_112_1_cAX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_113_1_Jwm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_114_1_pex.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_115_1_lKK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_116_1_4xb.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_117_1_uON.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_118_1_jGo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_119_1_nQn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_11_1_49b.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_120_1_zBp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_121_1_KnV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_122_1_8KK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_123_1_mlP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_124_1_JnH.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_125_1_Psk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_126_1_wEJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_127_1_hHm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_128_1_qSS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_129_1_Xv3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_12_1_N49.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_130_1_6X4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_131_1_Kw2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_132_1_Z7A.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_133_1_Fjl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_134_1_NLs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_135_1_2t8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_136_1_jQY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_137_1_OYU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_138_1_9P4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_139_1_lQH.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_13_1_oGO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_140_1_V75.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_141_1_HoE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_142_1_yVp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_143_1_xyI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_144_1_jVA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_145_1_LSV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_146_1_2Pu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_147_1_8gg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_148_1_94a.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_149_1_9uA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_14_1_9n3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_150_1_wNM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_151_1_WHj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_152_1_xok.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_153_1_nkU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_154_1_GPr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_155_1_7Qb.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_156_1_ScE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_157_1_KVw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_158_1_AnK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_159_1_x9U.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_15_1_Gkj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_160_1_Voj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_161_1_JiI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_162_1_ABx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_163_1_eJ4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_164_1_Li5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_165_1_d1G.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_166_1_Tnq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_167_1_Gmr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_168_1_y1Q.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_169_1_QRP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_16_1_n7A.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_170_1_SYd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_171_1_fi9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_172_1_I5C.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_173_1_lho.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_174_1_sY6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_175_1_W5c.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_176_1_OMm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_177_1_Dif.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_178_1_JV6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_179_1_KZn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_17_1_sEy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_180_1_rn3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_181_1_cMc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_182_1_YYA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_183_1_5Qy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_184_1_fgC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_185_1_arl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_186_1_OEI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_187_1_8pB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_188_1_veJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_18_1_6wt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_190_1_tQL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_191_1_RLm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_192_1_m9t.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_193_1_7uo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_194_1_iEp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_195_1_JOa.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_196_1_ijr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_197_1_7Cp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_198_1_vif.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_199_1_q0h.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_19_1_aC1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_1_1_Eio.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_200_1_urv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_20_1_YFF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_21_1_Lf0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_22_1_IQe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_23_1_Ez1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_24_1_D62.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_25_1_jB3.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_26_1_oO7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_27_1_qOS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_28_1_hIe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_29_1_poo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_2_1_cTu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_30_1_zV5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_31_1_WTk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_32_1_Odi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_33_1_SNq.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_34_1_9QJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_35_1_Mtl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_36_1_J8S.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_37_1_qfw.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_38_1_JYu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_39_1_OUC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_3_1_OHz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_40_1_B5q.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_41_1_W2o.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_42_1_uql.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_43_1_K1E.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_44_1_suJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_45_1_ffD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_46_1_jTZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_47_1_8JV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_48_1_MfW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_49_1_XVZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_4_1_mts.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_50_1_Fcf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_51_1_vU5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_52_1_sqI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_53_1_c2P.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_54_1_Gci.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_55_1_kxt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_56_1_T5L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_57_1_P4m.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_58_1_6r4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_59_1_A4s.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_5_1_TtL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_60_1_DVs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_61_1_J6b.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_62_1_Aas.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_63_1_ekn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_64_1_lNt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_65_1_NLe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_66_1_3LV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_67_1_qW4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_68_1_sab.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_69_1_UJJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_6_1_OLE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_70_1_hF7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_71_1_GIr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_72_1_6b7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_73_1_IiS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_74_1_WOB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_75_1_c4A.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_76_1_n88.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_77_1_W8B.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_78_1_PNg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_79_1_Gvr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_7_1_zm1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_80_1_Dwy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_81_1_wV0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_82_1_9Oh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_83_1_zeB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_84_1_5c2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_85_1_FtD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_86_1_o00.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_87_1_qWY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_88_1_v4W.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_89_1_xk9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_8_1_Xns.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_90_1_Fmz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_91_1_toE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_92_1_KlP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_93_1_J4h.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_94_1_LaY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_95_1_134.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_96_1_GMA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_97_1_3ds.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_98_1_eNG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_99_1_Ab5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R2_HISTATS/outfile14TeVSKIM_9_1_MLv.root',
	)

)
