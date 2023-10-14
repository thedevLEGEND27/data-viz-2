import pandas as pd
import numpy as np

ski_data = pd.read_csv("European_Ski_Resorts.csv")
eu_data = pd.read_csv("Countries-Europe.csv")

ski_data = pd.DataFrame(ski_data)
eu_data = pd.DataFrame(eu_data)

print(ski_data.describe())
