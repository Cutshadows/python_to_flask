class Account():

	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def __repr__(self):
		return f'Account Owner {self.owner} and Current Balance are {self.balance}'

	def deposit(self, dept_ammount):
		self.balance = self.balance + dept_ammount
		print('Deposit Created!!')

	def withdraw(self, wd_ammount):
		if wd_ammount > self.balance:
			print('You can`t not witdhdraw this mount')
		else:
			self.balance = self.balance - wd_ammount
			print('widthDraw Successful')


acct1 = Account('Douglas', 100)

print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(175)
