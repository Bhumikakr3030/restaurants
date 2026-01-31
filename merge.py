import pandas as pd

# ----------------------------
# STEP 1: Load CSV files
# ----------------------------
orders_df = pd.read_csv("orders.csv")
users_df = pd.read_csv("users.csv")
restaurants_df = pd.read_csv("restuarants.csv")

# ----------------------------
# STEP 2: Merge Orders + Users
# ----------------------------
merged_df = pd.merge(
    orders_df,
    users_df,
    on="user_id",
    how="left"
)

# ----------------------------
# STEP 3: Merge with Restaurants
# ----------------------------
final_df = pd.merge(
    merged_df,
    restaurants_df,
    on="restaurant_id",
    how="left"
)

# ----------------------------
# STEP 4: Save Final CSV
# ----------------------------
final_df.to_csv("final_food_delivery_dataset.csv", index=False)

print("✅ Merge completed successfully!")
