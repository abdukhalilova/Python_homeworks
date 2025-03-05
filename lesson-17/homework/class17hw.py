import pandas as pd
# Homework 1
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print(df)
# Print the first 3 rows of the DataFrame
print(df.head(3))
# Find the mean age of the individuals
print(f'Mean age: {df['age'].mean()}')
# Select and print only the 'Name' and 'City' columns
print(f'{df[['first_name', 'City']]}')
# Add a new column 'Salary' with random salary values
df['Salary'] = [10000, 2000, 3000, 4000]
print(df)
# Display summary statistics of the DataFrame
print(df.describe())

# Homework 2
# Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data
data2 = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000, 6000, 7500, 8000], 'Expenses': [3000, 3500, 4000, 4500]}
df2 = pd.DataFrame(data2)
print(df2)
# Calculate and display the maximum sales and expenses.
print(f'max sales: {df2["Sales"].max()}')
print(f'max expenses: {df2["Expenses"].max()}')
# Calculate and display the minimum sales and expenses.
print(f'min sales: {df2["Sales"].min()}')
print(f'min expenses: {df2["Expenses"].min()}')
# Calculate and display the average sales and expenses.
print(f'average sales: {df2["Sales"].mean()}')
print(f'average expenses: {df2["Expenses"].mean()}')

# Homework 3
# Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories.
data3 = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 'January': [1200, 200, 300, 150], 'February': [1300, 220, 320, 160], 'March': [1400, 240, 330, 170], 'April': [1500, 250, 350, 180]}
df3 = pd.DataFrame(data3)
print(df3)
# Calculate and display the maximum expense for each category.
df3.set_index('Category', inplace=True)
print(f'Max Expenses: {df3.max(axis=1)}')
# Calculate and display the minimum expense for each category.
print(f'Min Expenses: {df3.min(axis=1)}')
# Calculate and display the average expense for each category.
print(f'Average Expenses: {df3.mean(axis=1)}')


