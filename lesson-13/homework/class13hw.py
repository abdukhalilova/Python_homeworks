from datetime import datetime, timedelta
import time
import pytz
import re
# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
b_date_str = input("Enter your birth date YYYY-MM-DD: ")
b_date = datetime.strptime(b_date_str, "%Y-%m-%d")

today = datetime.today()
years = today.year - b_date.year
months = today.month - b_date.month
days = today.day - b_date.day
if days<0:
    months -=1
    days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month - 1, 1)).days
if months < 0:
    years -= 1
    months += 12
print(f"Your age is {years} years, {months} months, and {days} days.")
# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
next_birthday = datetime(today.year, b_date.month, b_date.day)
if next_birthday < today:
    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)
days_until_nbd = (next_birthday - today).days
print(f"Your next birthday is after {days_until_nbd} days")
# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
current_date_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_date = datetime.strptime(current_date_str, "%Y-%m-%d %H:%M")
hours = int(input("Enter the meeting duration in hours: "))
minutes = int(input("Enter the meeting duration in minutes: "))
meeting_duration = timedelta(hours=hours, minutes=minutes)
end_time = current_date + meeting_duration
print(f"The end time is {end_time}")
# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
current_time_str = input("Enter the current date and time in your time zone (YYYY-MM-DD HH:MM): ")
current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
from_timezone = pytz.timezone(input("Enter your current time zone (ex: America/New_York): "))
to_timezone = pytz.timezone(input("Enter the time zone to convert (ex: America/New_York): "))
local_dt = from_timezone.localize(current_time)
converted_dt = current_time.astimezone(to_timezone)
print(f"Time in {to_timezone} is {converted_dt}")
# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
future_date_str = input("Enter the current date and time (YYYY-MM-DD HH:MM:SS): ")
future_date = datetime.strptime(future_date_str, "%Y-%m-%d %H:%M:%S")
current_time = datetime.now()
difference = future_date - current_time
seconds = difference.total_seconds()
while True:
    seconds -= 1
    time.sleep(1)
    print(f"{seconds} seconds left")
    if seconds <= 0:
        print("Time is up")
        break
# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
email= input("Enter your email address: ")
pattern = r"^.+@.+\..+$"
matches = re.match(pattern, email)
if bool(matches)== 1:
    print("Valid Email")
else:
    print("Invalid Email")

# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
phone = input("Enter 10 digit phone number: ")
formatted = f'({phone[0:3]}) {phone[3:6]}-{phone[6:10]} '
if len(phone) !=10:
    print("Invalid phone number. Try again")
elif bool(re.match(r".+[0-9]", formatted)) == 0:
    print("Invalid phone number. Try again")
else:
    print(formatted)
# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
password = input("Enter password: ")
if len(password) <= 8:
    print("Password must contain at least 8 characters, Try again")
elif bool(re.match(r'.+[0-9]', password)) ==0:
    print("Password should contain at least one digit, Try again")
elif bool(re.match(r'.+[A-Z]', password)) ==0:
    print("Password should contain at least one uppercase letter, Try again")
elif bool(re.match(r'.+[a-z]', password)) ==0:
    print("Password should contain at least one lowercase letter. Try again")
else:
    print("Password is accepted")
# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
text = """Python is a powerful programming language. Python is widely used in web development, 
data science, and automation. Learning Python can be fun and rewarding."""
word_to_find = input("Enter the word you want to find: ")
matches = [(m.start(), m.end()) for m in re.finditer(rf'\b{re.escape(word_to_find)}\b', text, re.IGNORECASE)]
if matches:
    print(f"The word '{word_to_find}' was found {len(matches)} times at positions:")
    for start, end in matches:
        print(f"- Position {start} to {end}: '{text[start:end]}'")
else:
    print(f"The word '{word_to_find}' was not found in the text.")
# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
text = input("Enter the text: ")
date_pattern = r'\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b'
dates = re.findall(date_pattern, text)
if dates:
    print("Extracted Dates:")
    for date in dates:
        print(f"- {date}")
else:
    print("No dates found in the text.")

