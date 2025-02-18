import pandas as pd
import plotly.express as px

df = pd.read_csv("leagueStats.csv")

small_df = df [
    ["Unnamed: 1",
       "Unnamed: 11"]
]

#Rename the columns
small_df.columns = ["Season", "3PA"]

#convert the 3pa column to a numeric type
small_df["3PA"] = pd.to_numeric(small_df["3PA"], errors = "coerce")
small_df = small_df[small_df["3PA"] > 0]
small_df.sort_values("Season", inplace = True)

#The season call data is in 1979-80, change this to be 1979 for each entry in the season column
small_df["Season"] = small_df["Season"].str.split("-", expand = True)[0]


#Plot the small_df. I want the season on the x axis, starting with the earliest season, and the 3PA on the y axis
fig = px.line(small_df, x = "Season", y = "3PA", title = "3 Point Attempts by Season")
#fig.show()


'''
Create a line graph with 2 other statistics proving/disproving the comment below:   
As a result of the three point shot becoming more popular teams have had to change their playstyle as well.  The floor became more spread out and, as a result, ball movement was less restricted to the paint.  
'''
#TOV% and FT/FGA
change_df = df [
    [
        "Unnamed: 1",
        "Unnamed: 30",
        "Unnamed: 28",
    ]
]


#print(change_df.head())
change_df.columns=["Season", "FT/FGA", "TOV%"]
change_df["Season"] = small_df["Season"].str.split("-", expand = True)[0]
change_df.sort_values("Season", inplace = True)
change_df["FT/FGA"] = pd.to_numeric(change_df["FT/FGA"], errors="coerce")
change_df = change_df[change_df["FT/FGA"].notnull()]
change_df["TOV%"] = pd.to_numeric(change_df["TOV%"], errors="coerce")
change_df = change_df[change_df["TOV%"].notnull()]

#print(change_df.head())

#FT/FGA over time
fig2 = px.line(change_df, x = "Season", y = "FT/FGA", title = "FT/FGA Over Time")
#fig2.show()

fig3 = px.line(change_df, x = "Season", y = "TOV%", title = "Turnover Percentage Over Time")
#fig3.show()

