import pandas as pd
import nfl_data_py as nfl

'''
You are to use the Python nfl_daya_py package to analyze NFL data from this year's Super Bowl Teams: 

    identify at least 2 strengths/weakness of this years Super Bowl Teams
    compare data from 2022 to data from 2024 for at least 2 statistics
    collect data/visualizations into a word document and provide comments

Submit your PYHON file AND Word document to canvas.  
'''

data = nfl.import_pbp_data([2024])
players = nfl.import_seasonal_rosters([2024])
teams = nfl.import_team_desc()

#fields = data.columns.tolist()

small_data = data [[
    "season_type",
    "week",
    "play_type",
    "complete_pass",
    "posteam",
    "third_down_converted",
    "third_down_failed",
    "rusher_player_id",
    "rusher_player_name",
    "rushing_yards",
    "receiver_player_id",
    "receiver_player_name",
    "receiving_yards",
    "passer_player_id",
    "passer_player_name",
    "passing_yards"
]]

#J.Hurts passing data
passing_data = small_data[(small_data["complete_pass"] == 1.0) & (small_data["posteam"] == "PHI") & (small_data["passer_player_name"] == "J.Hurts")]
passing_data_agg = passing_data.groupby(["passer_player_name"], as_index = False).agg({"passing_yards": "sum"})
#print(passing_data_agg["passing_yards"] / 20)


#Receiving data - season totals for chiefs receivers
receiving_data = small_data[(small_data["play_type"] == "pass") & (small_data["posteam"] == "KC") & (small_data["complete_pass"] == 1.0)]
receiving_data_agg = receiving_data.groupby(["receiver_player_name"], as_index = False).agg({"receiving_yards": "sum"})
#print(receiving_data_agg)

#Grab eagles rushing data where Saquan was the rusher
rushing_data = small_data[(small_data["play_type"] == "run") & (small_data["posteam"] == "PHI") & (small_data["rusher_player_name"] == "S.Barkley")]
rushing_agg = rushing_data.agg({"rushing_yards": "sum"})

#Print Saquon's average yards per game
#print(rushing_agg / 19)

#Now we want to take a look at the number of "long runs" (runs greater than or equal to 20 yards) that were done by Barkley or Hurts
long_runs = small_data[(small_data["play_type"] == "run") & (small_data["posteam"] == "PHI") & (small_data["rushing_yards"] >= 20) & ((small_data["rusher_player_name"] == "S.Barkley") | (small_data["rusher_player_name"] == "J.Hurts"))]
long_runs.groupby(["rusher_player_name"], as_index = False)
#print(len(long_runs))
#print(long_runs)

#2022 long runs for the eagles
prev_long_runs = long_runs = small_data[(small_data["play_type"] == "run") & (small_data["posteam"] == "PHI") & (small_data["rushing_yards"] >= 20) & (small_data["rusher_player_name"] == "J.Hurts")]
prev_long_runs_sb = long_runs = small_data[(small_data["play_type"] == "run") & (small_data["posteam"] == "NYG") & (small_data["rushing_yards"] >= 20) & (small_data["rusher_player_name"] == "S.Barkley")]
#print(len(prev_long_runs))
#print(len(prev_long_runs_sb))

#Grab the 3rd down converted and 3rd down failed numbers for KC and PHI
small_data = small_data[((small_data["third_down_converted"] == 1) | (small_data["third_down_failed"] == 1)) & ((small_data["posteam"] == "PHI") | (small_data["posteam"] == "KC"))]

#Look at Patrick mahomes rushing plays on third downs
mahomes = small_data[(small_data["play_type"] == "run") & (small_data["rusher_player_name"] == "P.Mahomes")]

#aggregate the conversions and failures
mahomes_conversion = mahomes.groupby(["rusher_player_name"], as_index = False).agg({"third_down_converted": "sum", "third_down_failed": "sum"})
mahomes_conversion["rushing_conversion_rate"] = mahomes_conversion["third_down_converted"] / (mahomes_conversion["third_down_converted"] + mahomes_conversion["third_down_failed"])
#print(mahomes_conversion)


#aggregate the conversions and failures
third_down = small_data.groupby(
    ["posteam"], as_index = False).agg({"third_down_converted": "sum", "third_down_failed": "sum"})

third_down["conversion_rate"] = third_down["third_down_converted"] / (third_down["third_down_converted"] + third_down["third_down_failed"])
#print(third_down)
