from pybaseball import batting_stats
from pybaseball import pitching_stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Collect all stats for 2025
bdata25 = batting_stats(2025, qual=1)
pdata25 = pitching_stats(2025, qual=1)

bdata25_WAR = bdata25[['Season','Name','Team', 'WAR']]
pdata25_WAR = pdata25[['Season','Name','Team', 'WAR']]

# Breakdown batter data by team
arib_25 = bdata25_WAR[bdata25_WAR['Team'] == 'ARI']
atlb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'ATL']
balb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'BAL']
bosb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'BOS']
chcb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'CHC']
chwb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'CHW']
cinb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'CIN']
cleb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'CLE']
colb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'COL']
detb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'DET']
houb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'HOU']
kcrb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'KCR']
laab_25 = bdata25_WAR[bdata25_WAR['Team'] == 'LAA']
ladb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'LAD']
miab_25 = bdata25_WAR[bdata25_WAR['Team'] == 'MIA']
milb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'MIL']
minb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'MIN']
nymb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'NYM']
nyyb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'NYY']
oakb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'OAK']
phib_25 = bdata25_WAR[bdata25_WAR['Team'] == 'PHI']
pitb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'PIT']
sdpb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'SDP']
sfgb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'SFG']
stlb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'STL']
seab_25 = bdata25_WAR[bdata25_WAR['Team'] == 'SEA']
tbrb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'TBR']
texb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'TEX']
torb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'TOR']
wasb_25 = bdata25_WAR[bdata25_WAR['Team'] == 'WAS']

# breakdown pitcher data by team
arip_25 = pdata25_WAR[pdata25_WAR['Team'] == 'ARI']
atlp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'ATL']
balp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'BAL']
bosp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'BOS']
chcp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'CHC']
chwp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'CHW']
cinp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'CIN']
clep_25 = pdata25_WAR[pdata25_WAR['Team'] == 'CLE']
colp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'COL']
detp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'DET']
houp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'HOU']
kcrp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'KCR']
laap_25 = pdata25_WAR[pdata25_WAR['Team'] == 'LAA']
ladp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'LAD']
miap_25 = pdata25_WAR[pdata25_WAR['Team'] == 'MIA']
milp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'MIL']
minp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'MIN']
nymp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'NYM']
nyyp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'NYY']
oakp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'ATH']
phip_25 = pdata25_WAR[pdata25_WAR['Team'] == 'PHI']
pitp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'PIT']
sdpp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'SDP']
sfgp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'SFG']
stlp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'STL']
seap_25 = pdata25_WAR[pdata25_WAR['Team'] == 'SEA']
tbrp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'TBR']
texp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'TEX']
torp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'TOR']
wasp_25 = pdata25_WAR[pdata25_WAR['Team'] == 'WAS']

# calculate batter fWAR per team
arib_25_war = arib_25['WAR'].sum()
atlb_25_war = atlb_25['WAR'].sum()
balb_25_war = balb_25['WAR'].sum()
bosb_25_war = bosb_25['WAR'].sum()
chcb_25_war = chcb_25['WAR'].sum()
chwb_25_war = chwb_25['WAR'].sum()
cinb_25_war = cinb_25['WAR'].sum()
cleb_25_war = cleb_25['WAR'].sum()
colb_25_war = colb_25['WAR'].sum()
detb_25_war = detb_25['WAR'].sum()
houb_25_war = houb_25['WAR'].sum()
kcrb_25_war = kcrb_25['WAR'].sum()
laab_25_war = laab_25['WAR'].sum()
ladb_25_war = ladb_25['WAR'].sum()
miab_25_war = miab_25['WAR'].sum()
milb_25_war = milb_25['WAR'].sum()
minb_25_war = minb_25['WAR'].sum()
nymb_25_war = nymb_25['WAR'].sum()
nyyb_25_war = nyyb_25['WAR'].sum()
oakb_25_war = oakb_25['WAR'].sum()
phib_25_war = phib_25['WAR'].sum()
pitb_25_war = pitb_25['WAR'].sum()
sdpb_25_war = sdpb_25['WAR'].sum()
sfgb_25_war = sfgb_25['WAR'].sum()
stlb_25_war = stlb_25['WAR'].sum()
seab_25_war = seab_25['WAR'].sum()
tbrb_25_war = tbrb_25['WAR'].sum()
texb_25_war = texb_25['WAR'].sum()
torb_25_war = torb_25['WAR'].sum()
wasb_25_war = wasb_25['WAR'].sum()

# calculate pitcher fWAR by team
arip_25_war = arip_25['WAR'].sum()
atlp_25_war = atlp_25['WAR'].sum()
balp_25_war = balp_25['WAR'].sum()
bosp_25_war = bosp_25['WAR'].sum()
chcp_25_war = chcp_25['WAR'].sum()
chwp_25_war = chwp_25['WAR'].sum()
cinp_25_war = cinp_25['WAR'].sum()
clep_25_war = clep_25['WAR'].sum()
colp_25_war = colp_25['WAR'].sum()
detp_25_war = detp_25['WAR'].sum()
houp_25_war = houp_25['WAR'].sum()
kcrp_25_war = kcrp_25['WAR'].sum()
laap_25_war = laap_25['WAR'].sum()
ladp_25_war = ladp_25['WAR'].sum()
miap_25_war = miap_25['WAR'].sum()
milp_25_war = milp_25['WAR'].sum()
minp_25_war = minp_25['WAR'].sum()
nymp_25_war = nymp_25['WAR'].sum()
nyyp_25_war = nyyp_25['WAR'].sum()
oakp_25_war = oakp_25['WAR'].sum()
phip_25_war = phip_25['WAR'].sum()
pitp_25_war = pitp_25['WAR'].sum()
sdpp_25_war = sdpp_25['WAR'].sum()
sfgp_25_war = sfgp_25['WAR'].sum()
stlp_25_war = stlp_25['WAR'].sum()
seap_25_war = seap_25['WAR'].sum()
tbrp_25_war = tbrp_25['WAR'].sum()
texp_25_war = texp_25['WAR'].sum()
torp_25_war = torp_25['WAR'].sum()
wasp_25_war = wasp_25['WAR'].sum()

# add pitcher and batter fWAR per team
ari_25_war = arib_25_war + arip_25_war
atl_25_war = atlb_25_war + atlp_25_war
bal_25_war = balb_25_war + balp_25_war
bos_25_war = bosb_25_war + bosp_25_war
chc_25_war = chcb_25_war + chcp_25_war
chw_25_war = chwb_25_war + chwp_25_war
cin_25_war = cinb_25_war + cinp_25_war
cle_25_war = cleb_25_war + clep_25_war
col_25_war = colb_25_war + colp_25_war
det_25_war = detb_25_war + detp_25_war
hou_25_war = houb_25_war + houp_25_war
kcr_25_war = kcrb_25_war + kcrp_25_war
laa_25_war = laab_25_war + laap_25_war
lad_25_war = ladb_25_war + ladp_25_war
mia_25_war = miab_25_war + miap_25_war
mil_25_war = milb_25_war + milp_25_war
min_25_war = minb_25_war + minp_25_war
nym_25_war = nymb_25_war + nymp_25_war
nyy_25_war = nyyb_25_war + nyyp_25_war
oak_25_war = oakb_25_war + oakp_25_war
phi_25_war = phib_25_war + phip_25_war
pit_25_war = pitb_25_war + pitp_25_war
sdp_25_war = sdpb_25_war + sdpp_25_war
sfg_25_war = sfgb_25_war + sfgp_25_war
stl_25_war = stlb_25_war + stlp_25_war
sea_25_war = seab_25_war + seap_25_war
tbr_25_war = tbrb_25_war + tbrp_25_war
tex_25_war = texb_25_war + texp_25_war
tor_25_war = torb_25_war + torp_25_war
was_25_war = wasb_25_war + wasp_25_war

# Add all teams & divide by 30 for the average
avg_team_war25 = (ari_25_war + atl_25_war + bal_25_war + bos_25_war + chc_25_war + chw_25_war + cin_25_war + cle_25_war + col_25_war  + det_25_war + hou_25_war + kcr_25_war + laa_25_war + lad_25_war + mia_25_war + mil_25_war + min_25_war + nym_25_war + nyy_25_war + oak_25_war + phi_25_war + pit_25_war + sdp_25_war + sfg_25_war + stl_25_war + sea_25_war + tbr_25_war  + tex_25_war + tor_25_war + was_25_war)/30

print(f'Team Average: {avg_team_war25}')
print(f'STL: {stl_25_war}')
print(f'MIL: {mil_25_war}')
print(f'PHI: {phi_25_war}')
print(f'TOR: {tor_25_war}')
print(f'NYY: {nyy_25_war}')
print(f'LAD: {lad_25_war}')
print(f'CLE: {cle_25_war}')

values = [stl_25_war, mil_25_war, phi_25_war, tor_25_war, nyy_25_war, lad_25_war]
teams = ['25 Cardinals', '25 Brewers', '25 Phillies', '25 Blue Jays', '25 Yankees', '25 Dodgers']
plt.bar(teams, values)
plt.axhline(y=avg_team_war25, color='r', linestyle='--', linewidth=2, label=f'Average Team WAR ({avg_team_war25})')
plt.xlabel('Teams')
plt.ylabel('2025 WAR')
plt.title('Teams vs Average WAR')
plt.show()

##  Collect all data for 2022
bdata22 = batting_stats(2022, qual=1)
pdata22 = pitching_stats(2022, qual=1)

bdata22_WAR = bdata22[['Season','Name','Team', 'WAR']]
pdata22_WAR = pdata22[['Season','Name','Team', 'WAR']]

all_war = pd.concat([bdata22_WAR, pdata22_WAR, bdata25_WAR, pdata25_WAR])

all_war.to_csv("all_war.csv")

# Breakdown batter data by team
arib_22 = bdata22_WAR[bdata22_WAR['Team'] == 'ARI']
atlb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'ATL']
balb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'BAL']
bosb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'BOS']
chcb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'CHC']
chwb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'CHW']
cinb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'CIN']
cleb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'CLE']
colb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'COL']
detb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'DET']
houb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'HOU']
kcrb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'KCR']
laab_22 = bdata22_WAR[bdata22_WAR['Team'] == 'LAA']
ladb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'LAD']
miab_22 = bdata22_WAR[bdata22_WAR['Team'] == 'MIA']
milb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'MIL']
minb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'MIN']
nymb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'NYM']
nyyb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'NYY']
oakb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'OAK']
phib_22 = bdata22_WAR[bdata22_WAR['Team'] == 'PHI']
pitb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'PIT']
sdpb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'SDP']
sfgb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'SFG']
stlb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'STL']
seab_22 = bdata22_WAR[bdata22_WAR['Team'] == 'SEA']
tbrb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'TBR']
texb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'TEX']
torb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'TOR']
wasb_22 = bdata22_WAR[bdata22_WAR['Team'] == 'WAS']

# breakdown pitcher data by team
arip_22 = pdata22_WAR[pdata22_WAR['Team'] == 'ARI']
atlp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'ATL']
balp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'BAL']
bosp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'BOS']
chcp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'CHC']
chwp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'CHW']
cinp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'CIN']
clep_22 = pdata22_WAR[pdata22_WAR['Team'] == 'CLE']
colp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'COL']
detp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'DET']
houp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'HOU']
kcrp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'KCR']
laap_22 = pdata22_WAR[pdata22_WAR['Team'] == 'LAA']
ladp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'LAD']
miap_22 = pdata22_WAR[pdata22_WAR['Team'] == 'MIA']
milp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'MIL']
minp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'MIN']
nymp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'NYM']
nyyp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'NYY']
oakp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'OAK']
phip_22 = pdata22_WAR[pdata22_WAR['Team'] == 'PHI']
pitp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'PIT']
sdpp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'SDP']
sfgp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'SFG']
stlp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'STL']
seap_22 = pdata22_WAR[pdata22_WAR['Team'] == 'SEA']
tbrp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'TBR']
texp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'TEX']
torp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'TOR']
wasp_22 = pdata22_WAR[pdata22_WAR['Team'] == 'WAS']

# calculate batter WAR per team
arib_22_war = arib_22['WAR'].sum()
atlb_22_war = atlb_22['WAR'].sum()
balb_22_war = balb_22['WAR'].sum()
bosb_22_war = bosb_22['WAR'].sum()
chcb_22_war = chcb_22['WAR'].sum()
chwb_22_war = chwb_22['WAR'].sum()
cinb_22_war = cinb_22['WAR'].sum()
cleb_22_war = cleb_22['WAR'].sum()
colb_22_war = colb_22['WAR'].sum()
detb_22_war = detb_22['WAR'].sum()
houb_22_war = houb_22['WAR'].sum()
kcrb_22_war = kcrb_22['WAR'].sum()
laab_22_war = laab_22['WAR'].sum()
ladb_22_war = ladb_22['WAR'].sum()
miab_22_war = miab_22['WAR'].sum()
milb_22_war = milb_22['WAR'].sum()
minb_22_war = minb_22['WAR'].sum()
nymb_22_war = nymb_22['WAR'].sum()
nyyb_22_war = nyyb_22['WAR'].sum()
oakb_22_war = oakb_22['WAR'].sum()
phib_22_war = phib_22['WAR'].sum()
pitb_22_war = pitb_22['WAR'].sum()
sdpb_22_war = sdpb_22['WAR'].sum()
sfgb_22_war = sfgb_22['WAR'].sum()
stlb_22_war = stlb_22['WAR'].sum()
seab_22_war = seab_22['WAR'].sum()
tbrb_22_war = tbrb_22['WAR'].sum()
texb_22_war = texb_22['WAR'].sum()
torb_22_war = torb_22['WAR'].sum()
wasb_22_war = wasb_22['WAR'].sum()

# calculate pitcher war by team
arip_22_war = arip_22['WAR'].sum()
atlp_22_war = atlp_22['WAR'].sum()
balp_22_war = balp_22['WAR'].sum()
bosp_22_war = bosp_22['WAR'].sum()
chcp_22_war = chcp_22['WAR'].sum()
chwp_22_war = chwp_22['WAR'].sum()
cinp_22_war = cinp_22['WAR'].sum()
clep_22_war = clep_22['WAR'].sum()
colp_22_war = colp_22['WAR'].sum()
detp_22_war = detp_22['WAR'].sum()
houp_22_war = houp_22['WAR'].sum()
kcrp_22_war = kcrp_22['WAR'].sum()
laap_22_war = laap_22['WAR'].sum()
ladp_22_war = ladp_22['WAR'].sum()
miap_22_war = miap_22['WAR'].sum()
milp_22_war = milp_22['WAR'].sum()
minp_22_war = minp_22['WAR'].sum()
nymp_22_war = nymp_22['WAR'].sum()
nyyp_22_war = nyyp_22['WAR'].sum()
oakp_22_war = oakp_22['WAR'].sum()
phip_22_war = phip_22['WAR'].sum()
pitp_22_war = pitp_22['WAR'].sum()
sdpp_22_war = sdpp_22['WAR'].sum()
sfgp_22_war = sfgp_22['WAR'].sum()
stlp_22_war = stlp_22['WAR'].sum()
seap_22_war = seap_22['WAR'].sum()
tbrp_22_war = tbrp_22['WAR'].sum()
texp_22_war = texp_22['WAR'].sum()
torp_22_war = torp_22['WAR'].sum()
wasp_22_war = wasp_22['WAR'].sum()

# add pitcher and batter war per team

ari_22_war = arib_22_war + arip_22_war
atl_22_war = atlb_22_war + atlp_22_war
bal_22_war = balb_22_war + balp_22_war
bos_22_war = bosb_22_war + bosp_22_war
chc_22_war = chcb_22_war + chcp_22_war
chw_22_war = chwb_22_war + chwp_22_war
cin_22_war = cinb_22_war + cinp_22_war
cle_22_war = cleb_22_war + clep_22_war
col_22_war = colb_22_war + colp_22_war
det_22_war = detb_22_war + detp_22_war
hou_22_war = houb_22_war + houp_22_war
kcr_22_war = kcrb_22_war + kcrp_22_war
laa_22_war = laab_22_war + laap_22_war
lad_22_war = ladb_22_war + ladp_22_war
mia_22_war = miab_22_war + miap_22_war
mil_22_war = milb_22_war + milp_22_war
min_22_war = minb_22_war + minp_22_war
nym_22_war = nymb_22_war + nymp_22_war
nyy_22_war = nyyb_22_war + nyyp_22_war
oak_22_war = oakb_22_war + oakp_22_war
phi_22_war = phib_22_war + phip_22_war
pit_22_war = pitb_22_war + pitp_22_war
sdp_22_war = sdpb_22_war + sdpp_22_war
sfg_22_war = sfgb_22_war + sfgp_22_war
stl_22_war = stlb_22_war + stlp_22_war
sea_22_war = seab_22_war + seap_22_war
tbr_22_war = tbrb_22_war + tbrp_22_war
tex_22_war = texb_22_war + texp_22_war
tor_22_war = torb_22_war + torp_22_war
was_22_war = wasb_22_war + wasp_22_war

# Add all teams & divide by 30 for the average
avg_team_war22 = (ari_22_war + atl_22_war + bal_22_war + bos_22_war + chc_22_war + chw_22_war + cin_22_war + cle_22_war + col_22_war  + det_22_war + hou_22_war + kcr_22_war + laa_22_war + lad_22_war + mia_22_war + mil_22_war + min_22_war + nym_22_war + nyy_22_war + oak_22_war + phi_22_war + pit_22_war + sdp_22_war + sfg_22_war + stl_22_war + sea_22_war + tbr_22_war  + tex_22_war + tor_22_war + was_22_war)/30

print(avg_team_war22)
print(stl_22_war)
print(mil_22_war)
print(phi_22_war)
print(tor_22_war)
print(nyy_22_war)
print(lad_22_war)

values = [stl_22_war, hou_22_war, atl_22_war, nym_22_war, nyy_22_war, lad_22_war]
teams = ['22 Cardinals', '22 Astros', '22 Braves', '22 Mets', '22 Yankees', '22 Dodgers']
plt.bar(teams, values)
plt.axhline(y=avg_team_war22, color='r', linestyle='--', linewidth=2, label=f'Average Team WAR ({avg_team_war22})')
plt.xlabel('Teams')
plt.ylabel('2022 WAR')
plt.title('Teams vs Average WAR')
plt.show()