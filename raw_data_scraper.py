import pandas
bracket = ["Alabama Crimson Tide","Texas A&M-Corpus Christi Islanders","Maryland Terrapins","West Virginia Mountaineers","San Diego State Aztecs","Charleston Cougars","Virginia Cavaliers","Furman Paladins","Creighton Bluejays","NC State Wolfpack","Baylor Bears","UC Santa Barbara Gauchos","Missouri Tigers","Utah State Aggies","Arizona Wildcats","Princeton Tigers","Houston Cougars","Northern Kentucky Norse","Iowa Hawkeyes","Auburn Tigers","Miami Hurricanes","Drake Bulldogs","Indiana Hoosiers","Kentucky Wildcats","Iowa State Cyclones","Pittsburgh Panthers","Xavier Musketeers","Kennesaw State Owls","Texas A&M Aggies","Penn State Nittany Lions","Texas Longhorns","Colgate Raiders","Purdue Boilermakers","Fairleigh Dickinson Knights","Memphis Tigers","Florida Atlantic Owls","Duke Blue Devils","Oral Roberts Golden Eagles","Tennessee Volunteers","Louisiana Ragin' Cajuns","Kentucky Wildcats","Providence Friars","Kansas State Wildcats","Montana State Bobcats","Michigan State Spartans","USC Trojans","Marquette Golden Eagles","Vermont Catamounts","Kansas Jayhawks","Howard Bison","Arkansas Razorbacks","Illinois Fighting Illini","Saint Mary's Gaels","VCU Rams","UConn Huskies","Iona Gaels","TCU Horned Frogs","Arizona State Sun Devils","Gonzaga Bulldogs","Grand Canyon Lopes","Northwestern Wildcats","Boise State Broncos","UCLA Bruins","UNC Asheville Bulldogs"]
real = [["Alabama Crimson Tide","Maryland Terrapins","San Diego State Aztecs","Furman Paladins","Creighton Bluejays","Baylor Bears","Missouri Tigers","Princeton Tigers","Houston Cougars","Auburn Tigers","Miami Hurricanes","Indiana Hoosiers","Pittsburgh Panthers","Xavier Musketeers","Penn State Nittany Lions","Texas Longhorns","Fairleigh Dickinson Knights","Florida Atlantic Owls","Duke Blue Devils","Tennessee Volunteers","Kentucky Wildcats","Kansas State Wildcats","Michigan State Spartans","Marquette Golden Eagles","Kansas Jayhawks","Arkansas Razorbacks","Saint Mary's Gaels","UConn Huskies","TCU Horned Frogs","Gonzaga Bulldogs","Northwestern Wildcats","UCLA Bruins"],["Alabama Crimson Tide","San Diego State Aztecs","Creighton Bluejays","Princeton Tigers","Houston Cougars","Miami Hurricanes","Xavier Musketeers","Texas Longhorns","Florida Atlantic Owls","Tennessee Volunteers","Kansas State Wildcats","Michigan State Spartans","Arkansas Razorbacks","UConn Huskies","Gonzaga Bulldogs","UCLA Bruins"],["San Diego State Aztecs","Creighton Bluejays","Miami Hurricanes","Texas Longhorns","Florida Atlantic Owls","Kansas State Wildcats","UConn Huskies","Gonzaga Bulldogs"],["San Diego State Aztecs","Miami Hurricanes","Florida Atlantic Owls","UConn Huskies"],["San Diego State Aztecs","UConn Huskies"],["Uconn Huskies"]]

print(bracket)
df = pandas.read_excel("2023_data.xlsx")
def EffFGP(row):
    return((row["FGM"]+(.5*row["3PM"]))/row["FGA"])
def RebRate(row):
    return((row["OR"]/(row["OR"]+row["DR"])))
def TurnoverRate(row):
    possesions = (row["FGA"]+(.475*row["FTA"])-row["OR"]+row["TO"])/row["GP"]
    return(row["TO"]/possesions)
def FreeThrowRate(row):
    return(row["FTA"]/row["FGA"])

df["Effective Field Goal %"] = df.apply(EffFGP, axis = 1)
df["Rebound Rate"] = df.apply(RebRate, axis = 1)
df["Turnover Rate"] = df.apply(TurnoverRate, axis = 1)
df["Free Throw Rate"] = df.apply(FreeThrowRate, axis = 1)

desired_columns = ['TEAM', 'Turnover Rate']
criteria_df = df.loc[:, desired_columns]
print(criteria_df)
def compare_teams(team1, team2, criteria_df):
    # Compare teams based on criteria
    team1_criteria = criteria_df.loc[criteria_df['TEAM'] == team1].iloc[:, 1:].values.flatten()
    team2_criteria = criteria_df.loc[criteria_df['TEAM'] == team2].iloc[:, 1:].values.flatten()
    
    # Return the team with the higher total criteria values
    return team1 if sum(team1_criteria) > sum(team2_criteria) else team2

# def normalize_column(column):
#     min_val = column.min()
#     max_val = column.max()
#     return ((column - min_val) / (max_val - min_val)) * 100

# # Columns you want to normalize
# columns_to_normalize = ['Effective Field Goal %', 'Rebound Rate','Turnover Rate','Free Throw Rate']

# # Normalize the specified columns
# for col in columns_to_normalize:
#     criteria_df[col] = normalize_column(criteria_df[col])

score = 0
weight = 0
while len(bracket) > 1:
    winners = []
    for i in range(0, len(bracket), 2):
        team1 = bracket[i]
        team2 = bracket[i + 1]
        winner = compare_teams(team1, team2, criteria_df)
        winners.append(winner)
    for i in range(len(winners)):
        if winners[i]==real[weight][i]:
            score += 100*2**weight
    bracket = winners
    print(bracket)
print(score)

# Print the winner
print("The winner is:", bracket[0])