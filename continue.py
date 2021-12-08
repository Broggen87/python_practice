# data = []

# while True:
# 	name = input('請輸入產品名稱: ')
# 	if name == 'end':
# 		break
# 	price = input('請輸入購買價格: ')
# 	data.append([name, price])

# with open('456.csv', 'w', encoding = 'utf-8') as d:
# 	d.write('商品, 價格' + '\n')
# 	for i in data:
# 		d.write(i[0] + ',' + i[1] + '\n')

data = []

with open('456.csv', 'r', encoding = 'utf-8') as f:
	for i in f:
		if '商品, 價格' in i:
			continue
		name, price = i.strip().split(',')
		data.append([name, price])
print(data)	
