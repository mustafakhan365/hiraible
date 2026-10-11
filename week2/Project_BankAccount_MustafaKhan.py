# Code By Mustafa Samad Khan
class BankAccount:
	def __init__(self, account_holder, account_number, balance=0):
		self.account_holder = account_holder
		self.account_number = account_number
		self.__balance = balance

	def deposit(self, amount):
		if amount <= 0:
			print("Enter amount greater than 0")
			return
		self.__balance = self.__balance +amount
		print(f"✅ {amount} deposited successfully!")
	def withdraw(self, amount):
		if amount <= 0:
			print("Enter an amount greater than 0!")
		elif amount > self.__balance:
			print("❌ Insufficient balance!")
		else:
			self.__balance = self.__balance - amount
			print(f"✅ {amount} withdrawn successfully!")
	def check_balance(self):
		balance = self._get_balance()
		print(f"💰 Current Balance: {balance}")
		return balance
	def _get_balance(self):
		return self.__balance
	def show_details(self):
		print(
			f"Account Holder: {self.account_holder} | Account No: "
			f"{self.account_number} | Balance: {self.__balance}"
		)

class SavingsAccount(BankAccount):
	def __init__(self, account_holder, account_number, balance=0, interest_rate=0):
		super().__init__(account_holder, account_number, balance)
		self.interest_rate = interest_rate
	def add_interest(self):
		interest = self._get_balance() * self.interest_rate / 100
		self.deposit(interest)
		print(f"📈 Interest of {self.interest_rate}% added!")
	def show_details(self):
		print(
			f"[Savings] Account Holder: {self.account_holder} | Account No: "
			f"{self.account_number} | Balance: {self._get_balance()} | "
			f"Interest Rate: {self.interest_rate}%"
		)

def execute():
	print("===============================================")
	print("               HBL System 🏦")
	print("===============================================")
	account = BankAccount("Mustafa", 1012345678, 1000)
	account.show_details()
	account.deposit(float(input("Enter deposit amount:")))
	account.check_balance()
	account.withdraw(float(input("Enter withdrawal amount:")))
	account.check_balance()

	savings = SavingsAccount("Ali", 1023456789, 5000, 10)
	savings.show_details()
	savings.deposit(float(input("Enter deposit amount for Savings Account:")))
	savings.add_interest()
	savings.check_balance()

execute()