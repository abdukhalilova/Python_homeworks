import datetime
# Homework 1. ToDo List Application
# Create a Task class with attributes such as task title, description, due date, and status
class Task:
    def __init__(self,title,description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'Incomplete'
    def __str__(self):
        return f"{self.title} - {self.description};  Due:  {self.due_date} - {self.status}"

# Create a ToDoList class that manages a list of tasks.
class Todolist:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = 'Completed'
                print(f"task '{task.title}' marked as completed")
                return

    def list_incompleted(self):
        incomplete_tasks = [task for task in self.tasks if task.status == 'Incomplete']
        if not incomplete_tasks:
            print("No tasks available")
        for task in incomplete_tasks:
            print(task)


todolist = Todolist()

print("To-Do List Application")
print("1. Add Task")
print("2. Mark Task as Complete")
print("3. List All Tasks")
print("4. List Incomplete Tasks")
print("5. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        todolist.add_task(Task(title, description, due_date))
        print("Task added successfully.")
    elif choice == 2:
        title = input("Enter task title to mark as complete: ")
        todolist.mark_completed(title)
    elif choice == 3:
        print("\nAll Tasks:")
        todolist.list_all_tasks()
    elif choice == 4:
        print("All Incomplete Tasks:")
        todolist.list_incompleted()
    elif choice == 5:
        break

# Homework 2. Simple Blog System
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}, Author: {self.author}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully.")
        return
    def list_all_posts(self):
        if not self.posts:
            print("No posts available")
            return
        for post in self.posts:
            print(post)
    def display_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post)
            else:
                print("Author is not found")

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print("Post deleted successfully.")
            else:
                print("Post is not found")
                return

    def edit_post(self, title, content):
        for post in self.posts:
            if post.title ==  title:
                post.content = content
                print("Post content is edited successfully.")
            else:
                print("Post is not found")
                return

    def display_latest_posts(self):
        for post in self.posts:
            print(post)

def main():
    blog = Blog()

    print("To-Do List Application")
    print("1. Add post")
    print("2. List All Posts")
    print("3. Display Post by Author")
    print("4. Delete Post")
    print("5. Edit Post")
    print("6. Display Latest Posts")
    print("7. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter task title: ")
            content = input("Enter task content: ")
            author = input("Enter author name: ")
            blog.add_post(Post(title, content, author))
        elif choice == 2:
            print("\nAll Tasks:")
            blog.list_all_posts()
        elif choice == 3:
            author = input("Enter author name: ")
            blog.display_by_author(author)
        elif choice == 4:
            title = input("Enter post title to delete: ")
            blog.delete_post(title)
        elif choice == 5:
            title = input("Enter post title to edit post")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)
        elif choice == 6:
            print("Latest Posts:")
            blog.display_latest_posts()
        elif choice == 7:
            break

main()
# Homework 3. Simple Banking System
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer.")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transferred ${amount} to {recipient.holder_name}. New balance: ${self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} created for {account.holder_name}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def display_accounts(self):
        for account in self.accounts.values():
            print(account)

def main():
    bank = Bank()

    while True:
        print("\nSimple Banking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Accounts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            bank.add_account(Account(acc_num, name))
        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(acc_num)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(acc_num)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "5":
            sender_num = input("Enter your account number: ")
            recipient_num = input("Enter recipient account number: ")
            amount = float(input("Enter transfer amount: "))
            sender = bank.get_account(sender_num)
            recipient = bank.get_account(recipient_num)
            if sender and recipient:
                sender.transfer(recipient, amount)
            else:
                print("One or both accounts not found.")
        elif choice == "6":
            bank.display_accounts()
        elif choice == "7":
            break


