import pandas as pd
import random
import sys

data = pd.read_csv("MM (version 2).csv")

#print(data.columns)
team1 = sys.argv[1]
team2 = sys.argv[2]

#Write me a check to ensure that the arguments given are in the data
if team1 not in data['School'].values:
    print('The first team you entered is not in the data. Please try again.')
    sys.exit()
if team2 not in data['School'].values:
    print('The second team you entered is not in the data. Please try again.')
    sys.exit()

#Grab Gonzaga and Georgia data rows from the dataframe
stats1 = data[data['School'] == team1].iloc[0]
stats2 = data[data['School'] == team2].iloc[0]

#Extract the relevant statistics
adjO1, adjD1, tempo1, sos1, lastFive1, oe1, e1 = stats1[['ORtg', 'DRtg', 'AdjT', 'NetRtgNorm', 'LastFiveNorm', 'OverEightScorersNorm', 'ExperienceNorm']]
adjO2, adjD2, tempo2, sos2, lastFive2, oe2, e2 = stats2[['ORtg', 'DRtg', 'AdjT', 'NetRtgNorm', 'LastFiveNorm', 'OverEightScorersNorm', 'ExperienceNorm']]

#Calculate the game tempo using the harmonic mean formula
gameTempo = (2 * tempo1 * tempo2)/(tempo1 + tempo2)

#print('Original OE for ', team1, ':', adjO1)
#print('Original OE for ', team2, ':', adjO2)

#Calculate Adjusted OE for each team
adjO1 = adjO1*(adjD2/104.7)
adjO2 = adjO2*(adjD1/104.7)

#print('Adjusted OE for ', team1, ':', adjO1)
#print('Adjusted OE for ', team2, ':', adjO2)

#Adjust points per possession on a range of factors: Luck, Last 5 games, OE, Experience
team1luck_factor = random.uniform(-0.05, 0.05)
team2luck_factor = random.uniform(-0.05, 0.05)

adjusted1 = (2 * team1luck_factor) + (3 * lastFive1) + (2.5 * oe1) + (2 * e1)
adjusted2 = (2 * team2luck_factor) + (3 * lastFive2) + (2.5 * oe2) + (2 * e2)

final_OE1 = adjO1 + adjusted1
final_OE2 = adjO2 + adjusted2

#print('Final OE for ', team1, ':', final_OE1)
#print('Final OE for ', team2, ':', final_OE2)
#print('Adjusted OE for ', team1, ':', adjO1)
#print('Adjusted OE for ', team2, ':', adjO2)

#Calculate the points per possession for each team
team1PPP = final_OE1/100
team2PPP = final_OE2/100



#Calculate the expected points for each team
Score1 = round(team1PPP*gameTempo, 0)
Score2 = round(team2PPP*gameTempo,0)

print('Expected Score for ', team1, ':', Score1)
print('Expected Score for ', team2, ':', Score2)
print('The adjusted factors below inform us how much of a bonus/penalty each team got based on their luck, last 5 games, number of players averaging 8 or more points a game, and years experience for the team.')
print('Adjusted factors for ', team1, ':', adjusted1)
print('Adjusted factors for ', team2, ':', adjusted2)
