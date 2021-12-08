import os

def read_file(file_name):
    data_1 = []
    with open(file_name, 'r', encoding = 'utf-8') as f:
        for i in f:
            if '商品名稱,價格' in i:
                continue
            name, price = i.strip().split(',')
            data_1.append([name, price])
        print(data_1)
    return(data_1)

def items_input():
    sheet = []
    while True:
        name = input('請輸入產品名稱: ')
        if name == 'end':
            break
        price = input('請輸入產品金額: ')
        sheet.append([name, price])
    return(sheet)

def print_data(w):
    for a in w:
        if '商品名稱,價格' in a:
            continue
        print(a[0], '花費', a[1], '元')

def creat_data(products, sheet):
    with open(products, 'w', encoding = 'utf-8') as f_1:
        f_1.write('商品名稱,價格\n')
        for i in sheet:
            f_1.write(i[0] + ',' + i[1] + '\n')

def main():
    file_name = input('檔案名稱: ')
    if os.path.isfile(file_name):
        print('找到檔案，開啟中')
        result = read_file(file_name)
    else:
        print('該檔案不存在')

    sheet = items_input()
    print(sheet)
    creat_data(file_name, sheet)

main()





