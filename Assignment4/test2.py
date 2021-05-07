import pandas as pd

df1 = pd.DataFrame({"a":[1, 2, 3, 4],
                    "b":[5, 6, 7, 8]})

df2 = pd.DataFrame({"a":[1, 2, 3],
                    "b":[5, 6, 7]})


# df1.pd.(df2, ignore_index = True)
df1 = pd.concat([df1, df2])
df1.reset_index(drop=True, inplace=True)

print(df1)