import pandas as pd

# Load the data
data = pd.read_csv('players_stats_by_season_full_details.csv')

# Clean column names
data.columns = data.columns.str.strip()

# Calculate metrics
data['Field Goal Accuracy'] = data['FGM'] / data['FGA']
data['Three Point Accuracy'] = data['3PM'] / data['FGA']  # Assuming FGA includes 3PM
data['Free Throw Accuracy'] = data['FTM'] / data['FTA']
data['Points per Minute'] = data['PTS'] / data['MIN']

# Overall shooting accuracy (assuming it includes all types of shots)
data['Overall Shooting Accuracy'] = (data['FGM'] + data['3PM'] + data['FTM']) / (data['FGA'] + data['FTA'])

# Average blocks and steals per game
data['Average Blocks per Game'] = data['BLK'] / data['GP']
data['Average Steals per Game'] = data['STL'] / data['GP']

# Create a DataFrame for the top 100 players for each metric
metrics = [
    'Field Goal Accuracy',
    'Three Point Accuracy',
    'Free Throw Accuracy',
    'Points per Minute',
    'Overall Shooting Accuracy',
    'Average Blocks per Game',
    'Average Steals per Game'
]

top_players = {}
for metric in metrics:
    top_players[metric] = data[['Player', 'Season', metric]].nlargest(100, metric)

# Display the top 100 players for each metric
for metric, df in top_players.items():
    print(f"Top 100 Players for {metric}:")
    print(df)
    print("\n")
