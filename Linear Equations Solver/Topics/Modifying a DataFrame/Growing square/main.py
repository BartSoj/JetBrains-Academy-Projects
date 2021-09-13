import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

# your code here
df = df.append({"a": 7, "b": 8}, ignore_index=True)
df["c"] = [3, 6, 9]
df = df.reset_index(drop=True)
