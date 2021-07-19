class Parent:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("Parent")

	def say(self):
		print("Anakin")

########
class Child(Parent):
	def __init__(self, name, age, size):
		# Parent.__init__(self, name, age) below the same
		super().__init__(name, age)
		print("Child")

par = Parent("pepe", 11)
child1 = Child("Child", 1, None)
par.say()  # able to call method without self ->
			  # -> argument via - class or child class.method|

child1.say()  # child object automatically sends 
             # self to the method
