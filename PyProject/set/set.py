a = [1,2,1,2,3,4,3,4]

def list_unicum(some_list):
	checker_set = set(some_list)
	summa = 0
	for item in checker_set:
		summa += item

	return summa

print(list_unicum(a))

print(sum(set(a)))