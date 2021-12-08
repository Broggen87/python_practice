# data = [1, 3, 5, 7, 9]
# with open('test.txt', 'w') as f:
# 	for i in data:
# 		f.write(str(i) + '\n')

data = []
with open('456.csv', 'r') as f:
	for i in f:
		d = i.strip().split(',')
		# data.append(d)
		print(d)