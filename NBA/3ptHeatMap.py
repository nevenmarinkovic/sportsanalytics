import pandas as pd
from nba_api.stats.endpoints import shotchartdetail

#Specify the distances
distance_ranges = {
    'Less Than 5 ft': (0, 4),
    '5-9 ft': (5, 9),
    '10-14 ft': (10, 14),
    '15-19 ft': (15, 19),
    '20-24 ft': (20, 24),
    '25-29 ft': (25, 29),
    '30-34 ft': (30, 34),
    '35-39 ft': (35, 39),
    '40+ ft': (40, 100) 
}

#Grab the shot data
shot_chart = shotchartdetail.ShotChartDetail(
    team_id=0,  
    player_id=0, 
    season_nullable='1996-97',  
    season_type_all_star='Regular Season',
    context_measure_simple='FGA'  
    
)

shot_df = shot_chart.get_data_frames()[0]

results = []

#Iterate through the distance ranges and calculate the statistics
for range_name, (min_dist, max_dist) in distance_ranges.items():
    range_shots = shot_df[(shot_df['SHOT_DISTANCE'] >= min_dist) & (shot_df['SHOT_DISTANCE'] <= max_dist)]
    
    attempts = len(range_shots)
    made = range_shots['SHOT_MADE_FLAG'].sum()
    if attempts > 0:
        fg_percentage = (made / attempts) * 100
    else:
        fg_percentage = 0

    # Append results
    results.append({
        'Distance Range': range_name,
        'Attempts': attempts,
        'Made': made,
        'Field Goal Percentage': fg_percentage
    })

results_df = pd.DataFrame(results)
results_df.to_csv("Old3ptHeatMap.csv", index=False)

