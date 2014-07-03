import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring(
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_100_1_PyU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_101_1_icZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_102_1_YtI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_103_1_9bS.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_104_1_fgf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_105_1_r5d.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_106_1_HNU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_107_1_usM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_108_1_J7s.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_109_1_ZfM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_10_1_4qz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_110_1_OW0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_111_1_yGP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_112_1_e8J.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_113_1_iql.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_114_1_RE6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_115_1_m67.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_116_1_T8n.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_117_1_9WK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_118_1_hZz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_119_1_t97.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_11_1_rFx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_120_1_Euh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_121_1_Fhf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_122_1_b4R.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_123_1_1k8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_124_1_sdg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_125_1_elX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_126_1_fSD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_127_1_TJf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_128_1_zhf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_129_1_8uG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_12_1_LD1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_130_1_Ewd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_131_1_3pD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_132_1_Dif.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_133_1_0eu.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_134_1_kAz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_135_1_amD.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_136_1_LYW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_137_1_XWQ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_138_1_iw1.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_139_1_AUg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_13_1_Tsh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_140_1_FaX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_141_1_szC.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_142_1_AQl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_143_1_L7R.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_144_1_RFs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_145_1_rel.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_146_1_FU7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_147_1_JuY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_148_1_oYK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_149_1_1dN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_14_1_gUR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_150_1_uEL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_151_1_o11.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_152_1_jtk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_153_1_yhT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_154_1_3XX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_155_1_fgK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_156_1_PEB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_157_1_qJ2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_158_1_XND.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_159_1_qb5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_15_1_OBB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_160_1_FIR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_161_1_4PI.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_162_1_QNr.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_163_1_5sO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_164_1_mQv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_165_1_Y7M.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_166_1_oes.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_167_1_HgF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_168_1_Go9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_169_1_Ily.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_16_1_eYi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_170_1_9aj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_171_1_jjf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_172_1_6mY.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_173_1_naN.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_174_1_oeE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_175_1_3lp.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_176_1_zVs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_177_1_xxg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_178_1_5bO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_179_1_17L.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_17_1_o5T.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_180_1_vUA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_181_1_tjW.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_182_1_rdT.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_183_1_BLc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_184_1_kdf.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_185_1_urZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_186_1_2kl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_187_1_SyU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_188_1_4Pg.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_189_1_BrM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_18_1_Vxj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_190_1_MBo.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_191_1_O10.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_192_1_IOK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_193_1_1g7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_194_1_tHl.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_195_1_nQF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_196_1_mqZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_197_1_1mv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_198_1_xb5.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_199_1_bhz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_19_1_fzP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_1_1_ejM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_200_1_Szc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_20_1_lwH.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_21_1_klG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_22_1_Kd8.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_23_1_StR.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_24_1_Gfv.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_25_1_JSs.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_26_1_Pj2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_27_1_dl6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_28_1_gtX.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_29_1_5Wt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_2_1_chA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_30_1_b59.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_31_1_gaK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_32_1_3ju.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_33_1_n6N.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_34_1_guK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_35_1_EL0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_36_1_gtd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_37_1_0rU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_38_1_ZV0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_39_1_M9h.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_3_1_hYM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_40_1_Vxb.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_41_1_JHt.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_42_1_2h9.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_43_1_9XJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_44_1_c3w.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_45_1_vnj.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_46_1_7gn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_47_1_8kL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_48_1_xKm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_49_1_x4A.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_4_1_ezP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_50_1_bLL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_51_1_zSL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_52_1_8IP.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_53_1_2Qz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_54_1_J0U.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_55_1_bPb.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_56_1_W9z.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_57_1_GyK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_58_1_dkO.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_59_1_IYi.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_5_1_22I.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_60_1_cHc.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_61_1_0KJ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_62_1_XXM.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_63_1_9Oh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_64_1_9ya.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_65_1_QFh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_66_1_IeZ.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_67_1_FVm.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_68_1_Qvk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_69_1_hOx.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_6_1_oGh.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_70_1_S4z.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_71_1_Uk4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_72_1_gkG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_73_1_JOU.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_74_1_xg4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_75_1_km6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_76_1_wpK.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_77_1_bjk.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_78_1_Hw7.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_79_1_aPe.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_7_1_WpL.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_80_1_I2P.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_81_1_uVG.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_82_1_8gF.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_83_1_XrA.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_84_1_238.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_85_1_sb4.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_86_1_bW0.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_87_1_Fwd.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_88_1_AZE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_89_1_tWE.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_8_1_fub.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_90_1_wqB.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_91_1_zGV.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_92_1_869.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_93_1_Fuz.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_94_1_qT6.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_95_1_6ih.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_96_1_nZn.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_97_1_K8B.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_98_1_oVy.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_99_1_gf2.root',
		'/store/user/skaplan/noreplica/MinBiasBeamSpotPhi0R4_HISTATS/outfile14TeVSKIM_9_1_DHE.root',
	)

)
