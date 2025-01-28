# task 1
txt = list(input("Enter a string: "))
new_txt = ''
i=0
for letter in txt:
    new_txt += letter
    if i == 2:
        new_txt += '_'
    i += 1
print(new_txt)

# task2
list1 = [1, 1, 2]
list2 = [2, 3, 4]
new_list = []
for i in list1:
    if i not in list2:
        new_list.append(i)
for j in list2:
    if j not in list1:
        new_list.append(j)
print(new_list)

# https://www.hackerrank.com/challenges/python-loops/problem
num = int(input("Enter a number(between 0 and 20): "))
for i in range(20):
    if i==num:
        break
    else:
        print(i**2)

# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/
# Exercise 1: Print first 10 natural numbers using while loop
for i in range(11):
    print(i)
# Exercise 2: Print the following pattern
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print(' ')
# Exercise 3: Calculate sum of all numbers from 1 to a given number
sum = 0
n = int(input('Enter a number: '))
for i in range(1, n+1):
    sum += i
print(sum)
# Exercise 4: Print multiplication table of a given number
n1 = int(input('Enter a number: '))
for i in range(1, 11):
    print(i*n1)
# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num>500:
        break
    elif num%5 ==0 and num<=150:
        print(num)
# Exercise 6: Count the total number of digits in a number
n2 = int(input('Enter a number: '))
counter = 0
while n2!=0:
    n2//=10
    counter+=1
print(f'number of digits: {counter}')
# Exercise 7: Print the following pattern
for i in range(1, 6):
    for j in range(6-i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list2 = reversed(list1)
l = len(list1)
for i in list2:
    print(i)
# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)
# Exercise 10: Display a message “Done” after the successful execution of the for loop
for i in range(5):
    print(i)
else:
    print("Done!")

