a = [1,2,3,4]
b = {1,2,3,4,5,6}

def comparador(some_set, some_list):

	#if(len(some_list) != len(some_set)):
		#return "Oh kurwa, lenghts are different"
	for item in some_list:
		if item in some_set:
			continue
		elif item not in some_set:
			return False
	return "Items are equal"

print(comparador(b, a))