
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Account:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")


    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.owner.username}")
        print(f"Current Balance: {self.balance} INR")       



class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def process(self):
        if self.from_account.balance >= self.amount:
            self.from_account.withdraw(self.amount)
            self.to_account.deposit(self.amount)
            print("Transaction successful")
        else:
            print("Transaction failed: Insufficient funds")

class Bank:
    def __init__(self):
        self.users = {}
        self.accounts = {}

    def create_user(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            return True
        else:
            print("Username already exists")
            return False

    def create_account(self, username, account_number, balance):
        if username in self.users:
            user = self.users[username]
            account = Account(account_number, balance, user)
            self.accounts[account_number] = account
            return True
        else:
            print("User does not exist")
            return False




User
# Initialize the bank system
bank = Bank()

# Create users and their accounts
bank.create_user("alice_wonder", "alicePass789")
bank.create_account("alice_wonder", "1122334455", 30000)
bank.create_user("bob_builder", "buildBob123")
bank.create_account("bob_builder", "5566778899", 50000)

# Retrieve the account objects
alice_account = bank.accounts["1122334455"]
bob_account = bank.accounts["5566778899"]

# Execute transactions between accounts
transaction4 = Transaction(alice_account, bob_account, 7500)
transaction4.process()

transaction5 = Transaction(bob_account, alice_account, 12000)
transaction5.process()

transaction6 = Transaction(alice_account, bob_account, 5000)
transaction6.process()



print("\nUpdated Balances:")
alice_account.display_balance()
bob_account.display_balance()
