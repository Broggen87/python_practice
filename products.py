products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == '結束':
        break
    price = input('請輸入價格: ')
    products.append([name, price])

for i in products:
    print(i[0], '，', '花費', i[1], '元')

with open('products.txt', 'w', encoding = 'utf-8') as p:
    for price in products:
        p.write(price[0] + ',' + '花費' + price[1] + '元' + '\n')

# with open('products.txt', 'r+') as p:
#     for i in p:
#         print(i)
