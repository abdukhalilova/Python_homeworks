#https://www.w3resource.com/python-exercises/dictionary/
#1. Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 'one', 3: 'three', 2: 'two', 0: 'zero'}
for key in sorted(d):
    print(f'{key}: {d[key]}')
# 2. Write a Python script to add a key to a dictionary.
# Expected Result : {0: 10, 1: 20, 2: 30}
dict2 = {0: 10, 1: 20}
dict2[2] = 30
print(dict2)
# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
# 4. Write a Python script to check whether a given key already exists in a dictionary.
given_key = int(input("Enter key value to check: "))
if given_key in dict2:
    print(f"{given_key} is in the dictionary")
else:
    print(f"{given_key} is not in the dictionary")
# 5. Write a Python program to iterate over dictionaries using for loops.
d = {'a': 1, 'b': 2, 'c': 3}
for dkey, dvalue in d.items():
    print(f'{dkey}: {dvalue}')
# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = int(input("Input a number "))
d = {}
for x in range(1, n + 1):
    d[x] = x * x
print(d)

# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d_sqr = {}
for x in range(1, 16):
    d_sqr[x] = x * x
print(d_sqr)
# 8. Write a Python script to merge two Python dictionaries.
d1 = {1: 'a', 2: 'b'}
d2 = {3: 'c', 4: 'd'}
merge_dict = d1.copy()
merge_dict.update(d2)
print(merge_dict)
# 9. Write a Python program to iterate over dictionaries using for loops.
d = {'a': 1, 'b': 2, 'c': 3}
for dkey, dvalue in d.items():
    print(f'{dkey}: {dvalue}')
# 10. Write a Python program to sum all the items in a dictionary.
dsum=0
for dkey, dvalue in d.items():
    dsum+=dvalue
print(f'sum of all values in dictionary: {dsum}')
# 11. Write a Python program to multiply all the items in a dictionary.
mult=0
for dkey, dvalue in d.items():
    mult+=dvalue
print(f'multiplication of all values in dictionary: {mult}')
# 12. Write a Python program to remove a key from a dictionary.
d.pop('a')
print(d)
# 13. Write a Python program to map two lists into a dictionary.
keys = ['one', 'two', 'three', 'four']
values = [1, 2, 3, 4]
mapped_dict = dict(zip(keys, values))
print(mapped_dict)
# 14. Write a Python program to sort a given dictionary by key.
for key in sorted(mapped_dict):
    print(f'{key}: {mapped_dict[key]}')
# 15. Write a Python program to get the maximum and minimum values of a dictionary.
max_key=0
min_key=0
for key, value in mapped_dict.items():
    if value > max_key:
        max_key=value
    if value < min_key:
        min_key=value
print(f'maximum value: {max_key}, minimum value: {min_key}')
# 16. Write a Python program to get a dictionary from an object's fields.

# 17. Write a Python program to remove duplicates from the dictionary.
input_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 1}
unique_values = set()
new_dict = {}

for key, value in input_dict.items():
    if value not in unique_values:
        new_dict[key] = value
        unique_values.add(value)
print("Original Dictionary:", input_dict)
print("Dictionary after removing duplicates:", new_dict)
# 18. Write a Python program to check if a dictionary is empty or not.
my_dict = {2:4,5:6}
if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")








