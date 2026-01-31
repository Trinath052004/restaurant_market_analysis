import pandas as pd
import json
import re

# Step 1: Load CSV Data (Orders)
print("Step 1: Loading orders.csv...")
orders_df = pd.read_csv('orders.csv')
print(f"  Orders loaded: {len(orders_df)} records")
print(f"  Columns: {list(orders_df.columns)}")

# Step 2: Load JSON Data (Users)
print("\nStep 2: Loading users.json...")
with open('users.json', 'r') as f:
    users_data = json.load(f)
users_df = pd.DataFrame(users_data)
print(f"  Users loaded: {len(users_df)} records")
print(f"  Columns: {list(users_df.columns)}")

# Step 3: Load SQL Data (Restaurants)
print("\nStep 3: Loading restaurants.sql...")
with open('restaurants.sql', 'r') as f:
    sql_content = f.read()

# Parse INSERT statements to extract restaurant data
pattern = r"INSERT INTO restaurants VALUES \((\d+), '([^']+)', '([^']+)', ([\d.]+)\);"
matches = re.findall(pattern, sql_content)

restaurants_data = []
for match in matches:
    restaurants_data.append({
        'restaurant_id': int(match[0]),
        'restaurant_name_sql': match[1],
        'cuisine': match[2],
        'rating': float(match[3])
    })

restaurants_df = pd.DataFrame(restaurants_data)
print(f"  Restaurants loaded: {len(restaurants_df)} records")
print(f"  Columns: {list(restaurants_df.columns)}")

# Step 4: Merge the Data using Left Joins
print("\nStep 4: Merging datasets...")

# First merge: orders with users (on user_id)
merged_df = pd.merge(orders_df, users_df, on='user_id', how='left')
print(f"  After merging with users: {len(merged_df)} records")

# Second merge: result with restaurants (on restaurant_id)
merged_df = pd.merge(merged_df, restaurants_df, on='restaurant_id', how='left')
print(f"  After merging with restaurants: {len(merged_df)} records")

# Step 5: Create Final Dataset
print("\nStep 5: Creating final dataset...")

# Rename columns for clarity
final_df = merged_df.rename(columns={
    'name': 'user_name',
    'restaurant_name': 'restaurant_name_orders'
})

# Select and reorder columns for the final output
final_columns = [
    'order_id', 'user_id', 'user_name', 'city', 'membership',
    'restaurant_id', 'restaurant_name_orders', 'cuisine', 'rating',
    'order_date', 'total_amount'
]

# Check which columns exist
available_columns = [col for col in final_columns if col in final_df.columns]
final_df = final_df[available_columns]

# Save to CSV
output_file = 'final_food_delivery_dataset.csv'
final_df.to_csv(output_file, index=False)
print(f"\n{'='*50}")
print(f"Final dataset saved to: {output_file}")
print(f"Total records: {len(final_df)}")
print(f"Columns: {list(final_df.columns)}")
print(f"{'='*50}")

# Display sample data
print("\nSample data (first 5 rows):")
print(final_df.head().to_string())

# Display summary statistics
print("\n\nDataset Summary:")
print(f"  - Total Orders: {len(final_df)}")
print(f"  - Unique Users: {final_df['user_id'].nunique()}")
print(f"  - Unique Restaurants: {final_df['restaurant_id'].nunique()}")
print(f"  - Cities: {final_df['city'].dropna().unique().tolist()}")
print(f"  - Cuisines: {final_df['cuisine'].dropna().unique().tolist()}")
print(f"  - Membership Types: {final_df['membership'].dropna().unique().tolist()}")
print(f"  - Date Range: {final_df['order_date'].min()} to {final_df['order_date'].max()}")
print(f"  - Total Revenue: ${final_df['total_amount'].sum():,.2f}")
