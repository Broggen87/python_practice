import os

def read_file(file_name):
    data_1 = []
    if os.path.isfile(file_name):
        print('找到檔案，開啟中')
        with open(file_name, 'r', encoding = 'utf-8') as f:
            for i in f:
                if '商品名稱,價格' in i:
                    continue
                name, price = i.strip().split(',')
                data_1.append([name, price])
        print(data_1)
    else:
        print('該檔案不存在')
    return(data_1)

def items_input(products):
    sheet = []
    with open(products, 'w', encoding = 'utf-8') as f_1:
        name = '商品名稱'
        price = '價格'
        sheet.append([name, price])
        while True:
            name = input('請輸入產品名稱: ')
            if name == 'end':
                break
            price = input('請輸入產品金額: ')
            sheet.append([name, price])
        for i in sheet:
            f_1.write(i[0] + ',' + i[1] + '\n')
    return(sheet)

def print_data(w):
    for a in w:
        if '商品名稱,價格' in a:
            continue
        print(a[0], '花費', a[1], '元')

result = read_file(file_name = input('檔案名稱: '))
sheet = items_input(input('建立檔案名稱: '))
print_data(sheet)




