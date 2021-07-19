import itertools

main_list =  list( itertools.permutations('123',r=3))

return_list = list()
for item in main_list:
	temp_list = list()
	for digit in item:
		temp_list.append(digit)
	return_list.append(temp_list)
	temp_list = list()
print(return_list)

print_str = ""
for item in return_list:
	for digit in item:
		print_str += digit
	print(int(print_str))
	print_str = ""


