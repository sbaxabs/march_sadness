import pandas
bracket = ["Alabama Crimson Tide","Texas A&M-Corpus Christi Islanders","Maryland Terrapins","West Virginia Mountaineers","San Diego State Aztecs","Charleston Cougars","Virginia Cavaliers","Furman Paladins","Creighton Bluejays","NC State Wolfpack","Baylor Bears","UC Santa Barbara Gauchos","Missouri Tigers","Utah State Aggies","Arizona Wildcats","Princeton Tigers","Houston Cougars","Northern Kentucky Norse","Iowa Hawkeyes","Auburn Tigers","Miami Hurricanes","Drake Bulldogs","Indiana Hoosiers","Kentucky Wildcats","Iowa State Cyclones","Pittsburgh Panthers","Xavier Musketeers","Kennesaw State Owls","Texas A&M Aggies","Penn State Nittany Lions","Texas Longhorns","Colgate Raiders","Purdue Boilermakers","Fairleigh Dickinson Knights","Memphis Tigers","Florida Atlantic Owls","Duke Blue Devils","Oral Roberts Golden Eagles","Tennessee Volunteers","Louisiana Ragin' Cajuns","Kentucky Wildcats","Providence Friars","Kansas State Wildcats","Montana State Bobcats","Michigan State Spartans","USC Trojans","Marquette Golden Eagles","Vermont Catamounts","Kansas Jayhawks","Howard Bison","Arkansas Razorbacks","Illinois Fighting Illini","Saint Mary's Gaels","VCU Rams","UConn Huskies","Iona Gaels","TCU Horned Frogs","Arizona State Sun Devils","Gonzaga Bulldogs","Grand Canyon Lopes","Northwestern Wildcats","Boise State Broncos","UCLA Bruins","UNC Asheville Bulldogs"]
print(bracket)
df = pandas.read_excel("team_data.xlsx")
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
print(df)


