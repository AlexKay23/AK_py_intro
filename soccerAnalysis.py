#https://github.com/nwslR/nwslpy

import nwslpy


stats = nwslpy.load_player_match_stats("portland-thorns-fc-vs-kansas-city-current-2022-10-29")
players = nwslpy.load_players()

# Select the columns of interest
stats = stats[["shots_total"]]
# Join with information about the players
stats = stats.join(players)[["shots_total", "player_match_name"]]
# Find the players with the most shots
stats = stats.sort_values("shots_total", ascending=False)


import pandas as pd
import matplotlib.pyplot as plt

statsDF = pd.DataFrame(stats)

statsDF.describe()

# Plotting Time
statsDF.plot(y="shots_total",x="player_match_name",kind="bar")


#Player Name analysis
playerDF = pd.DataFrame(players)

playerDF.head()

playerDF['count']=playerDF.groupby('player_nationality')['player_nationality'].transform('count')

print(playerDF)

playerDF.plot(x="player_nationality",y="count",kind="bar")