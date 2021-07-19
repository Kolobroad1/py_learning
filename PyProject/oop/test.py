place = int(input())
arr = list()
num = 1
for k in range(9):
	arr2 = []

	for j in range(4):
		arr2.append(num)
		num+=1

	arr.append(arr2)

for item in arr:
	print(item)
