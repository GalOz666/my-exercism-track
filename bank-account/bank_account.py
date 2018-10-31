from multiprocessing import Lock, Value

def open_check(method):
	def wrapper(self, *args, **kwargs):
		if self.op == True:
			return method(self, *args, **kwargs)
		else:
			raise ValueError("Cannot access closed account")
	return wrapper


class BankAccount:

	def __init__(self):
		self.lock = Lock([{}])
		self.balance = Value('d', 0)
		self.op = False

	def open(self):
		self.op = True

	@open_check
	def deposit(self, amount):
		if amount >= 0:
			self.lock.acquire()
			self.balance.value += amount
			self.lock.release()
		else:
			raise ValueError

	@open_check
	def get_balance(self):
		return int(self.balance.value)

	@open_check
	def withdraw(self, amount):
		if amount  < 0 or amount > self.balance.value:
			raise ValueError

		else:
			self.lock.acquire()
			self.balance.value -= amount
			self.lock.release()

	def close(self):
		self.op = False