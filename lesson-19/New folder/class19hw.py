import pandas as pd
import sqlite3
# Homework Assignment 1: Analyzing Sales Data
# Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.

df = pd.read_csv('sales_data.csv')
print(df.head())
grouped = df.groupby(['Category']).agg(
    total_quantity = ("Quantity", 'sum'),
    Average_price = ("Price", 'mean'),
    Max_quantity = ("Quantity", 'max')).reset_index()
print(grouped)

# Identify the top-selling product in each category based on the total quantity sold.
product_sales = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_selling = product_sales.loc[product_sales.groupby("Category")["Quantity"].idxmax()]
print(top_selling)

# Find the date on which the highest total sales (quantity * price) occurred.
df['Total_sales'] = df['Quantity'] * df['Price']
date_sales = df.groupby("Date")['Total_sales'].sum().reset_index()
highest_sales_date = date_sales.loc[date_sales['Total_sales'].idxmax()]
print(highest_sales_date)

# Homework Assignment 2: Examining Customer Orders

df2 = pd.read_csv('customer_orders.csv')
print(df2.head(10))
# Group the data by CustomerID and filter out customers who have made less than 20 orders.
customer_order_counts = df2.groupby('CustomerID')['OrderID'].count()
filtered_customers = customer_order_counts[customer_order_counts<20].index
print(df2[df2['CustomerID'].isin(filtered_customers)])

# Identify customers who have ordered products with an average price per unit greater than $120.
avg_price = df2['Price'].mean()
customers = df2[df2['Price'] > avg_price]
print(customers)
# Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.
filtered_df2 = df2.groupby(['Product']).agg(
    total_quantity = ("Quantity", 'sum'),
    Average_price = ("Price", 'mean')).reset_index()
print(filtered_df2[filtered_df2['total_quantity'] <5])

# Homework Assignment 3: Population Salary Analysis

conn = sqlite3.connect('population.db')
query = "SELECT * FROM population"
df_population = pd.read_sql(query, conn)
conn.close()
print(df_population.head())

salary_band_path = "population_salary_analysis.xlsx"
df_salary_band = pd.read_excel(salary_band_path)

# print("Population Data Columns:", df_population.columns)
# print("Salary Band Data Columns:", df_salary_band.columns)
df_merged = df_population.merge(df_salary_band, how="left",
                                left_on="salary",
                                right_on="salary")

salary_stats = df_merged.groupby("Salary_Category").agg(
    Population_Count=("salary", "count"),
    Avg_Salary=("salary", "mean"),
    Median_Salary=("salary", "median")
).reset_index()

total_population = salary_stats["Population_Count"].sum()

salary_stats["Population_Percentage"] = (salary_stats["Population_Count"] / total_population) * 100

print(salary_stats)