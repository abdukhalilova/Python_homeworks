# Homework1:
# 1. Create a tuple literal named cardinal_numbers that holds the strings "first", "second", and "third", in that order.
cardinal_numbers = ("first", "second", "third")

# 2. Using index notation and print(), display the string at index 1 in cardinal_numbers.
print(cardinal_numbers[1])
# 3. In a single line of code, unpack the values in cardinal_numbers into three new strings named position1, position2,
# and position3. Then print each value on a separate line.
position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)
# 4. Using tuple() and a string literal, create a tuple called my_name that contains the letters of your name.

my_name = tuple("Oysha")
# 5. Check whether the character "x" is in my_name using the in keyword.
if 'x' in my_name:
    print("Exists")
else:
    print("Not exists")
# 6. Create a new tuple containing all but the first letter in my_name using slice notation.
new_tuple = tuple(my_name[1::])
print(new_tuple)

# Homework2:
# 1. Create a list named food with two elements, "rice" and "beans".
food = ["rice", "beans"]
# 2. Append the string "broccoli" to food using .append().
food.append("broccoli")
# 3. Add the strings "bread" and "pizza" to food using .extend().
food.extend(["bread", "pizza"])
# 4. Print the first two items in the food list using print() and slice no tation.
print(food[:2])
# 5. Print the last item in food using print() and index notation.
print(food[-1])
# 6. Create a list called breakfast from the string "eggs, fruit, orange juice" using the string .split() method.
breakfast = ["eggs", "fruit", "orange juice"]
# 7. Verify that breakfast has three items using len().
print(len(breakfast))
# 8. Create a new list called lengths using a list comprehension that con tains the lengths of each string in the breakfast list
lengths = [len(x) for x in breakfast]
print(lengths)

# Homework3:
# Given two integer variables: a and b. Swap the values of the variables.
a = int(input())
b = int(input())
# write code here. Don't change given conditions
x = a
a = b
b = x
print(a, b)

# practice for lists
# level1
# task1
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.extend(["grape", "kiwi"])
print(fruits)

# task2
numbers = [10, 20, 40, 50]
numbers.insert(2, 30)
print(numbers)

# task3
colors = ["red", "green", "blue", "yellow", "blue"]
colors.remove("blue")
print(colors)

# task4
animals = ["cat", "dog", "bird", "fish"]
print(animals.index("bird"))

# task5
nums = [1, 2, 3, 4, 1, 2, 1]
print(nums.count(1))

# task6
integers = [5, 10, 15, 20, 25]
integers.reverse()
print(integers)

# task7
n = [7, 3, 9, 1, 5]
n.sort()
print(n)
n.sort()
n.reverse()
print(n)

# task8
cities = ["New York", "Paris", "Tokyo", "Sydney"]
copy_cities = cities.copy()
cities.append("Tashkent")
print(copy_cities)
print(cities)

# task9
r_numbers = [8, 4, 6, 2, 9]
r_numbers.clear()
print(r_numbers)

# task10
months = ["January", "February", "March", "April", "May"]
last_element = months.pop()
print(last_element)
second_element = months.pop(1)
print(second_element)

# level2
# task1
random_nums = [7, 8, 3, 2, 9]
random_nums.append(19)
random_nums[1] = 5
random_nums.pop(2)
print(random_nums)

# task2
ls = [15, 2, 78, 34, 7, 90]
max_value = max(ls)
min_value = min(ls)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# task3
ls1 = [10, 20, 30, 40, 50]
sum_ls1 = sum(ls1)
avg_ls1 = sum_ls1 / len(ls1)
print("Sum of lists:", sum_ls1)
print("Average of lists:", avg_ls1)

# task4
strings = ["banana", "apple", "cherry", "date"]
strings.sort()
print(strings)
strings.sort()
strings.reverse()
print(strings)

# practice for tuples
# task1
tuple1 = 7, "string", 2.3, True, [2, 3, 7, 8]

# task2
tuple2 = ("apple", "banana", "cherry", "date")
print(tuple2[1])
print(tuple2[-1])

# task3
tuple3 = (10, 20, 30, 40, 50, 60)
sliced_tuple = tuple3[1:4]
print(sliced_tuple)


# task4
tuple4 = ("red", "green", "blue", "yellow")

# task5
tuple5 = (1, 2, 3, 4, 5, 6)
print(len(tuple5))

# task6
tuple6_1 = ("a", "b", "c")
tuple6_2 = (1, 2, 3)
tuple6 = tuple6_1 + tuple6_2
print(tuple6)

# task7
tuple7 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tuple7.count(4))

# task8
tuple8 = ("cat", "dog", "bird", "fish")
print(tuple8.index("dog"))

# task9
tuple9 = ("Python", 3.10, "Programming")
var1, var2, var3 = tuple9
print(var1)
print(var2)
print(var3)

# task10
tuple10 = (10, 20, 30)
# tuple10[0] = 15
print(tuple10)


