# https://www.w3resource.com/python-exercises/python-exception-handling-exercises.php
# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    a = int(input('Enter dividend number: '))
    b = int(input('Enter divisor number: '))
    print(a/b)
except ZeroDivisionError as zex:
    print(f'{type(zex).__name__}: {zex}. Divisor cannot be zero. ')
# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    n = int(input('Enter an integer number: '))
except ValueError as vex:
    print(f'Error Type: {type(vex).__name__}: {vex}. ')
# 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
try:
    path = (input('Enter path to open a file: '))
    file = open(path, r)
    print(file.read())
    file.close()
except FileNotFoundError as filex:
    print(f'Error: {type(filex).__name__}: {filex}')
# 4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    n1 = float(input('Enter first number: '))
    n2 = float(input('Enter second number: '))
except TypeError as vex:
    print(f'Error Type: {type(vex).__name__}: {vex}. ')
# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
try:
    path = (input('Enter path to open a file: '))
    file = open(path, r)
    print(file.read())
    file.close()
except PermissionError as filex:
    print(f'Error: {type(filex).__name__}: {filex}')
# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
lists = [1, 2, 3, 4]
try:
    i = int(input('Enter an index: '))
    print(lists[i])
except IndexError as iex:
    print(f'Error: {type(iex).__name__}: {iex}')
# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    num = int(input('Enter a number: '))
    print(num)
except KeyboardInterrupt as kex:
    print(f'{type(kex).__name__}: {kex}')
# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    div1 = int(input('Enter dividend number: '))
    div2 = int(input('Enter divisor number: '))
    print(div1/div2)
except ArithmeticError as aex:
    print(f'{type(aex).__name__}: {aex}')
# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    encode = input('Enter the encoding for the file: ')
    path = (input('Enter path to open a file: '))
    file = open(path, r)
    print(file.read())
    file.close()
except UnicodeDecodeError as udex:
    print(f'Error: {type(udex).__name__}: {udex}')
# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    r = len(nums)
    print("Length of the list:", r)
except AttributeError as aexept:
    print(f'Error: {type(aexept).__name__}: {aexept}')

# https://www.w3resource.com/python-exercises/file/
# 1. Write a Python program to read an entire text file.
# file_path=input("Enter the path of the file: ")
file_path = r'C:\Users\abduk\OneDrive\Documents\class8.txt'
with open(file_path, 'r') as file1:
    print(file1.read())
# 2. Write a Python program to read first n lines of a file.
with open(file_path, 'r') as file1:
    n=int(input('Enter number of lines to read: '))
    for i in range(n):
        print(file1.readline())
        if i==n:
            break
# 3. Write a Python program to append text to a file and display the text.
with open(file_path, 'r+') as file1:
    text = input('Enter the text: ')
    print(file1.write(text))
    print(file1.read())
# 4. Write a Python program to read last n lines of a file.
with open(file_path, 'r') as file1:
    n1=int(input('Enter number of lines to read last lines: '))
    lines=file1.readline()
    last_lines = lines[-n1:]
    for line in last_lines:
        print(line)
# 5. Write a Python program to read a file line by line and store it into a list.
with open(file_path, 'r') as file1:
    list_file = []
    for line in file1:
        print(line)
        list_file.append(line)
    print(list_file)
# 6. Write a Python program to read a file line by line store it into a variable.
with open(file_path, 'r') as file1:
    variable = file1.readlines()
    print(variable)
# 7. Write a Python program to read a file line by line store it into an array.
with open(file_path, 'r') as file1:
    array = []
    for line in file1:
        print(line)
        array.append(line)
    print(array)
# 8. Write a python program to find the longest words.

# 9. Write a Python program to count the number of lines in a text file.
with open(file_path, 'r') as file1:
    l_numbers = 0
    for line in file1:
        l_numbers += 1
    print(f'Number of lines: {l_numbers}')
# 10. Write a Python program to count the frequency of words in a file.

# 11. Write a Python program to get the file size of a plain file.

# 12. Write a Python program to write a list to a file.
with open(file_path, 'a') as file1:
    list2 = ['one\n', 'two\n', 'three\n', 'four\n']
    for i in list2:
        file1.write(i)
with open(file_path, 'r') as file1:
    print(file1.read())
# 13. Write a Python program to copy the contents of a file to another file .
file2_path = r'C:\Users\abduk\OneDrive\Documents\class8copy.txt'
with open(file_path, 'r') as file1:
    with open(file2_path, 'w') as file2:
        for line in file1:
            file2.write(line)
with open(file2_path, 'r') as file2:
    print(file2.read())
