import pandas as pd
import random

data = pd.read_csv("MM (version 2).csv")

#print(data.columns)

team1 = 'Gonzaga'
team2 = 'Alabama'

#Grab Gonzaga and Georgia data rows from the dataframe
stats1 = data[data['School'] == team1].iloc[0]
stats2 = data[data['School'] == team2].iloc[0]

#Extract the relevant statistics
adjO1, adjD1, tempo1, sos1, lastFive1, oe1, e1 = stats1[['ORtg', 'DRtg', 'AdjT', 'NetRtgNorm', 'LastFiveNorm', 'OverEightScorersNorm', 'ExperienceNorm']]
adjO2, adjD2, tempo2, sos2, lastFive2, oe2, e2 = stats2[['ORtg', 'DRtg', 'AdjT', 'NetRtgNorm', 'LastFiveNorm', 'OverEightScorersNorm', 'ExperienceNorm']]

#Calculate the game tempo using the harmonic mean formula
gameTempo = (2 * tempo1 * tempo2)/(tempo1 + tempo2)

print('Original OE for ', team1, ':', adjO1)
print('Original OE for ', team2, ':', adjO2)

#Calculate Adjusted OE for each team
adjO1 = adjO1*(adjD2/104.7)
adjO2 = adjO2*(adjD1/104.7)

print('Adjusted OE for ', team1, ':', adjO1)
print('Adjusted OE for ', team2, ':', adjO2)

#Adjust points per possession on a range of factors: Luck, SOS, Last 5 games, OE, Experience
team1luck_factor = random.uniform(-0.05, 0.05)
team2luck_factor = random.uniform(-0.05, 0.05)


final_OE1 = adjO1 + (.15 * team1luck_factor) + (.35 * sos1) + (.25 * lastFive1) + (.15 * oe1) + (.1 * e1)
final_OE2 = adjO2 + (.15 * team2luck_factor) + (.35 * sos2) + (.25 * lastFive2) + (.15 * oe2) + (.1 * e2)

print('Final OE for ', team1, ':', final_OE1)
print('Final OE for ', team2, ':', final_OE2)
#print('Adjusted OE for ', team1, ':', adjO1)
#print('Adjusted OE for ', team2, ':', adjO2)

#Calculate the points per possession for each team
team1PPP = adjO1/100
team2PPP = adjO2/100



#Calculate the expected points for each team
Score1 = round(team1PPP*gameTempo, 0)
Score2 = round(team2PPP*gameTempo,0)

#print('Expected Score for ', team1, ':', Score1)
#print('Expected Score for ', team2, ':', Score2)
