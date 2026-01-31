import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

USERNAME = "root"
PASSWORD = quote_plus("Bhumikakr@2003")  # 🔥 FIX HERE
DATABASE = "restuarant"
TABLE = "restaurants"

engine = create_engine(
    f"mysql+pymysql://{USERNAME}:{PASSWORD}@localhost/{DATABASE}"
)

query = f"SELECT * FROM {TABLE}"

df = pd.read_sql(query, engine)
df.to_csv("output.csv", index=False)

print("✅ CSV file created successfully!")
