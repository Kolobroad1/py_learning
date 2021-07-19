class Person():
	def ager(self):
		current_year = 2021
		print(current_year - int(self.date_of_birth))
		return current_year - int(self.date_of_birth)

p1 = Person()
p1.date_of_birth = 2000
p1.ager()