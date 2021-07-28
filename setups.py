config = []
config.append ({"name" : "finviz_new_highs", "url":"https://finviz.com/screener.ashx?v=111&s=ta_newhigh&f=cap_smallover,fa_pe_profitable,sh_avgvol_o500,sh_price_o15&ft=3", "filename" : "dailyhighlist.txt"} )
config.append ({"name" : "finviz_ipos", "url" : "https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_changeopen_u,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa", "filename" : "ipolist.txt"}) 
config.append ({"name" : "finviz_high_5pct", "url" : "https://finviz.com/screener.ashx?v=111&f=cap_smallover,fa_epsqoq_pos,fa_salesqoq_pos,sh_avgvol_o750,sh_price_o15,ta_highlow52w_b0to5h,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=3", "filename" : "highlist5pct.txt"}) 


finviz_new_highs = "https://finviz.com/screener.ashx?v=111&s=ta_newhigh&f=cap_smallover,fa_pe_profitable,sh_avgvol_o500,sh_price_o15&ft=3" 
finviz_ipos = "https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_epsyoy1_o20,fa_salesqoq_o20,ind_stocksonly,ipodate_prev3yrs,sh_avgvol_o500,sh_price_o15,ta_changeopen_u,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa"
finviz_high_5pct = "https://finviz.com/screener.ashx?v=111&f=cap_smallover,fa_epsqoq_pos,fa_salesqoq_pos,sh_avgvol_o750,sh_price_o15,ta_highlow52w_b0to5h,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=3"
finviz_url = finviz_ipos
finviz_url = finviz_new_highs
finviz_url = finviz_high_5pct
output_filename = "ipolist.txt"
output_filename = "dailyhighlist.txt"
output_filename = "highlist5pct.txt"
