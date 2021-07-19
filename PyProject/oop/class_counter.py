class Test():
	counter = 0
	def __init__(self, name):
		self.name = name
		Test.counter += 1
		print(Test.counter)

t1 = Test("sas")
