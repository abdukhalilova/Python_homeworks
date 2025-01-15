# https://www.hackerrank.com/challenges/write-a-function/problem
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")

# https://www.hackerrank.com/challenges/py-if-else/problem
n = int(input("Enter number: "))
if n % 2 == 0:
    if n>2 and n<5:
        print("Not wierd")
    elif n>6 and n<20:
        print("Wierd")
    elif n>20:
        print("Not wierd")
else: print("Wierd")

# Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a%2==0 and b%2==0:
    print("Both of the numbers are even")
elif a%2==0 and b%2!=0:
    print(f"{a} is even number")
elif a%2!=0 and b%2==0:
    print(f"{b} is even number")
else:
    print("Both of the numbers are odd")