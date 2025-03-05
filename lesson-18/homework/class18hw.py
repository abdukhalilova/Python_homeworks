import pandas as pd
from datetime import datetime
df = pd.read_csv(r'C:\Users\abduk\PycharmProjects\ternProject\tackoverflow_qa.csv')
print(df.head())

# Find all questions that were created before 2014
df['creationdate']=pd.to_datetime(df['creationdate'])
print(df[df['creationdate']<datetime(2010,1,1)])
# Find all questions with a score more than 50
print(df[df['score']>50])
# Find all questions with a score between 50 and 100
print(df[df['score'].between(50,100)])
# Find all questions answered by Scott Boston
print(df[df['ans_name']=='Scott Boston'])
# Find all questions answered by the following 5 users

# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
filtered = df[(df["creationdate"] >= datetime(2014, 3, 1)) & (df["creationdate"] <= datetime(2014, 10, 31))&(df['ans_name']=='Unutbu')&(df['score']<5)]
print(filtered.head())
# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
print(df[df['score'].between(5,10)&df['viewcount']>10000])

# Find all questions that are not answered by Scott Boston
print(df[df['ans_name']!='Scott Boston'])

df = pd.read_csv(r'C:\Users\abduk\PycharmProjects\ternProject\titanic.csv')
print(df.head())

# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
filter = df[(df['Sex']=='female')&(df['Pclass']==1)&(df["Age"].between(20,30))]
print(filter)
# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
print(df[df['Fare']>100])
# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
filter2 = df[(df['Survived'] ==0)&(df['SibSp']==0)&(df['Parch']==0)]
print(filter2)
# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
print(df[(df['Embarked']=='C')&(df['Fare']>50)])
# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
print(df[(df['SibSp']>=1)&(df['Parch']>=1)])
# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
print(df[(df['Age']<=15)&df['Survived']==1])
# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
print(df[(df['Cabin'].notna())&(df['Fare']>200)])
# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
print(df[df['PassengerId']%2==1])
# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
unique_tickets = df['Ticket'].value_counts() == 1
print(df[df['Ticket'].isin(unique_tickets[unique_tickets].index)])
# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
print(df[(df['Name'].str.contains('Miss'))&(df['Pclass']==1)])