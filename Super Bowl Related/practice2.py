import pandas as pd
import plotly.graph_objects as go
import nfl_data_py as nfl

pbp = nfl.import_pbp_data([2022])

fields = pbp.columns.tolist()
#for field in fields:
 #   print(field)

#we only selected the columns we needed for today
pbp[
    [
        "play_type",
        "posteam",
        "rushing_yards",
        "rusher_id",
        "rusher_player_id",
        "rusher_player_name",
        "ydstogo",
        "down",
        "yardline_100",
        "run_location",
        "score_differential",
        "game_seconds_remaining"
    ]

].to_csv("pbp_2022.csv", index=False)