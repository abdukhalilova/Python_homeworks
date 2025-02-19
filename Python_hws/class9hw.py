from datetime import date
import math
# https://www.w3resource.com/python-exercises/oop/index.php
# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self, radius):
        return f"Area of circle: {self.radius * self.radius*3.14}"
    def get_perimeter(self, radius):
        return f"Perimeter of circle: {2 * 3.14 * self.radius}"
r = int(input('Enter radius: '))
circle = Circle(r)
print(circle.get_area(r))
print(circle.get_perimeter(r))
# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self,name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date: {self.date_of_birth}"
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return f"Age: {age}"
person1 = Person('Oysha', 'Uzbekistan', date(2005, 2, 8))
print(person1)
print(person1.calculate_age())

# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class  Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def addition(self):
        return self.number1 + self.number2
    def subtraction(self):
        return self.number1 - self.number2
    def multiplication(self):
        return self.number1 * self.number2
    def division(self):
        return self.number1 / self.number2
sign = input('Enter operation to perform (+, -, *, /): ')
n1 = int(input('enter first number: '))
n2 = int(input('enter second number: '))
calc = Calculator(n1, n2)
if sign == '+':
    print(calc.addition())
elif sign == '-':
    print(calc.substraction())
elif sign == '*':
    print(calc.multiplication())
elif sign == '/':
    print(calc.division())
# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return f"Area: {math.pi * (self.radius ** 2)}"
    def calculate_perimeter(self):
        return f"Perimeter: {2 * math.pi * self.radius}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return f"Area: {self.width * self.height}"
    def calculate_perimeter(self):
        return f"Perimeter: {2 * (self.width + self.height)}"

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return f"Area: {(self.base * self.height) / 2}"
    def calculate_perimeter(self):
        return f"Perimeter: {self.side1 + self.side2 + self.side3}"

rad=8
c = Circle(rad)
print(c.calculate_area())
print(c.calculate_perimeter())

w = 5
h = 8
rect = Rectangle(w,h)
print(rect.calculate_area())
print(rect.calculate_perimeter())

base = 8
height = 6
side1 = 4
side2 = 5
side3 = 8
t = Triangle(base, height, side1, side2, side3)
print(t.calculate_area())
print(t.calculate_perimeter())

# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

print("Search 7:", bst.search(7))
print("Search 20:", bst.search(20))

# 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")
            return item
        else:
            print("Stack is empty. Nothing to pop.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Top element:", s.peek())
print("Stack size:", s.size())
s.pop()
s.pop()
s.pop()
s.pop()

# 7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end='')
            current = current.next
        print()
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if current:
            previous.next = current.next

llist = LinkedList()
llist.insert(7)
llist.insert(3)
llist.insert(8)
llist.display()
llist.delete(7)
llist.display()

# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class Shoppingcart:
    def __init__(self):
        self.items = []
        self.total_price = 0.0
    def add_item(self, name, price, quantity=1):
        self.items.append((name, price, quantity))
        self.total_price += price * quantity
        print(f"{quantity} x {name} added to the cart. Total price: ${self.total_price}")
    def remove_item(self, name, quantity=1):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                self.total_price -= item[1] * quantity
        print(f" {quantity} x {name} removed from the cart. Total price: ${self.total_price}")
    def display_cart(self):
        for item in self.items:
            print(f"{item[0]} x {item[1]} added to the cart")
        print(f'Total price: ${self.total_price}')

shop = Shoppingcart()
shop.add_item("Apple", 3.0, 3)
shop.add_item("Banana", 5.0, 2)
shop.display_cart()
shop.remove_item("Apple", 1)
shop.display_cart()
# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
class Stack:
    def __init__(self):
        self.elements = []
        self.top = -1
    def push(self, element):
        self.elements.append(element)
        self.top += 1
        print(f"Pushed {element} onto the stack.")
        return self.top
    def pop(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        else:
            print(f"Popped last element from the stack.")
            return self.elements.pop()
    def display(self):
        print(f"Stack: {self.elements}")

stck = Stack()
stck.push(7)
stck.push(8)
stck.push(3)
stck.pop()
stck.display()

# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_number_counter = 1000

    def create_account(self, customer_name, initial_balance):
        account_number = self.account_number_counter
        self.accounts[account_number] = {
            "customer_name": customer_name,
            "balance": initial_balance
        }
        self.account_number_counter += 1
        print(f"Account created for {customer_name}. Account Number: {account_number}")
        return account_number

    def deposit(self, account_number, deposit_amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += deposit_amount
            print(f"Deposited ${deposit_amount}. New balance: ${self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, withdraw_amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= withdraw_amount:
                self.accounts[account_number]["balance"] -= withdraw_amount
                print(f"Withdrew ${withdraw_amount}. New balance: ${self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account Balance: ${self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def transfer(self, from_account, to_account, transfer_amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account]["balance"] >= transfer_amount:
                self.accounts[from_account]["balance"] -= transfer_amount
                self.accounts[to_account]["balance"] += transfer_amount
                print(f"Transferred ${transfer_amount} from Account {from_account} to Account {to_account}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both accounts not found.")

bank = Bank()
account1 = bank.create_account("Oysha", 500)
account2 = bank.create_account("Indira", 300)
bank.deposit(account1, 200)
bank.withdraw(account2, 100)
bank.check_balance(account1)
bank.check_balance(account2)
bank.transfer(account1, account2, 150)
bank.check_balance(account1)
bank.check_balance(account2)
