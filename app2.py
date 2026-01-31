import pandas as pd

df = pd.read_json("users.json")
df.to_csv("output2.csv", index=False)

print("✅ JSON converted to CSV")
