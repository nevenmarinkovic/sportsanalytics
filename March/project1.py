import pandas as pd
import random
import sys

data = pd.read_csv("Project1.csv")

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

#Grab the two schools we are interested in
stats1 = data[data['School'] == team1].iloc[0]
stats2 = data[data['School'] == team2].iloc[0]



#Extract the relevant statistics
O1, D1, tempo1, e1, diff1, ft1 = stats1[['ORtg_Avg','DRtg_Avg','Tempo_Avg','Experience_Norm','Difficulty_Norm', 'FT_Norm']]
O2, D2, tempo2, e2, diff2, ft2 = stats2[['ORtg_Avg','DRtg_Avg','Tempo_Avg','Experience_Norm','Difficulty_Norm', 'FT_Norm']]

#Calculate the game tempo using the harmonic mean formula
gameTempo = (2 * tempo1 * tempo2)/(tempo1 + tempo2)

'''
print('Tempo for ', team1, ':', tempo1)
print('Tempo for ', team2, ':', tempo2)
print('Game Tempo: ', gameTempo)
'''

#Calculate Adjusted OE for each team using the D-1 average
adjO1 = O1*(D2/104.7)
adjO2 = O2*(D1/104.7)

#Adjust the offensive efficiency for each team by factoring in experience, difficulty, and free throw percentage
adjusted1 = (2 * diff1) + (3 * ft1) + (2 * e1)
adjusted2 = (2 * diff2) + (3 * ft2) + (2 * e2)

final_OE1 = adjO1 + adjusted1
final_OE2 = adjO2 + adjusted2

#Calculate the points per possession for each team
team1PPP = final_OE1/100
team2PPP = final_OE2/100

#Calculate the expected points for each team
Score1 = round(team1PPP*gameTempo, 0)
Score2 = round(team2PPP*gameTempo,0)
print('This program will predict the score for a march madness game, factoring in offensive/defensive efficiency, tempo, experience, difficulty, and free throw percentage.')
print('Expected Score for ', team1, ':', Score1)
print('Expected Score for ', team2, ':', Score2)
print()
print('The adjusted factors below inform us how much of a bonus each team got based on their free throw percentage, strength of schedule, and years experience for the team.')
print('Adjusted factors for ', team1, ':', adjusted1)
print('Adjusted factors for ', team2, ':', adjusted2)