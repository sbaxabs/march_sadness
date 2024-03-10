import pandas
bracket = ["","sock"]
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

