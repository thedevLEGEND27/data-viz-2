import pandas as pd

temp_data = pd.read_csv("country temp.csv")
eu_data = pd.read_csv("Countries-Europe.csv")

ski_data = pd.DataFrame(ski_data)
eu_data = pd.DataFrame(eu_data)

# print(ski_data.columns)
# eu_data.drop("zoom", axis=1)
# print(eu_data.loc[eu_data["name"] == "Ukraine", "latitude"])

# print(eu_data.head)
# print(ski_data.tail)
for country in eu_data.name:
    var = False
    for country2 in ski_data.Country:
        if country == country2:
            var = True
            print(eu_data.loc[eu_data["name"] == country, "longitude"])
            ski_data["longitude"] = float(
                eu_data.loc[eu_data["name"] == country, "longitude"]
            )
            ski_data["latitude"] = float(
                eu_data.loc[eu_data["name"] == country, "latitude"]
            )
    if var == False:
        ski_data.loc[len(ski_data)] = {
            "Country": country,
            "latitude": float(eu_data.loc[eu_data["name"] == country, "latitude"]),
            "longitude": float(eu_data.loc[eu_data["name"] == country, "longitude"]),
        }

ski_data = ski_data.drop(ski_data.columns[[0]], axis=1)
# ski_data.to_csv("lol.csv")
