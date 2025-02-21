from datetime import date
# task1 Create a program to ask name and year of birth from user and tell them their age

name = input("Enter your name: ")
year = int(input("Enter your year: "))
current_date = date.today()
current_year = current_date.year
age = current_year-year
print(f"Your age is {age}")

# task2 Extract car names from this text
text1 = 'LMaasleitbtui'
print(text1[0::2])
print(text1[1::2])

# task3 Extract car names from this text
text2 = 'MsaatmiazD'
print(text2[0::2])
print(text2[-1::-2])

# task4 Extract residence from this text
text3 = 'I am John. I am from London'
resident = text3.split()
print(resident[-1])