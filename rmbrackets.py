import pandas as pd
import re

temp_data = pd.read_csv("correct temps.csv")

df = pd.DataFrame(temp_data)

r = 0
c = 0

print(df)


def num_there(s):
    return any(i.isdigit() for i in s)


for col in df[:]:
    print("col: ", col, r, c)

    for val in df[col]:
        val = re.sub("[\(\[].*?[\)\]]", "", val)
        val = val.replace("\n", "")
        num_there(val)
        # print(df.iloc[c, r], r, c)
        if num_there(val):
            df.iloc[c, r] = val
        c += 1
        if c == 13:
            c = 0

        # df.iloc[c, r] = val

    r += 1
    if r == 47:
        break

print(df)
df.drop(df.columns[[0]], axis=1)
# df.to_csv("correct_temps_edited.csv")
