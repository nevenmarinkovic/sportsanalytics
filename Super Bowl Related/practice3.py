import pandas as pd
import plotly.graph_objects as go
import nfl_data_py as nfl

data = nfl.import_pbp_data([2022])
players = nfl.import_seasonal_rosters([2022])
teams = nfl.import_team_desc()

condensed_data = data [
    [
        "season_type",
        "two_point_attempt",
        "play_type",
        "posteam",
        "passer_player_id",
        "week",
        "passing_yards",
        "pass_touchdown",
    ]
]
#condensed_data.to_csv("test1.csv", index=False)

#filter to regular season
condensed_data = condensed_data[condensed_data["season_type"] == "REG"]

#remove two point attempts
condensed_data = condensed_data[condensed_data["two_point_attempt"] == False]

#Filter to pass plays
pass_data = condensed_data[condensed_data["play_type"] == "pass"]
#pass_data.to_csv("test2.csv", index=False)

#join with the roster table to get player names
pass_data = pass_data.merge(
    players[["player_id", "player_name"]],
    left_on="passer_player_id",
    right_on="player_id"
)
#pass_data.to_csv("mergedTables.csv", index=False)

#join with the team table to get team color for plot
pass_data = pass_data.merge(
    teams[["team_abbr", "team_color"]],
    left_on="posteam",
    right_on="team_abbr"
)
#pass_data.to_csv("colorsAdded.csv", index=False)

agg = pass_data.groupby(
    ["player_name", "team_abbr", "team_color", "week"], as_index = False).agg({"passing_yards": "sum", "pass_touchdown": "sum"})
print(agg.head())

