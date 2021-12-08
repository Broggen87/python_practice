import random
# r = random.randint(int(input('請輸入猜數字遊戲下限: ')), int(input('請輸入猜數字遊戲上限: '))
b = int(input('猜數字遊戲下限: '))
d = int(input('猜數字遊戲上限: '))
r = random.randint(b, d)
a = int(input('請輸入一個數字: '))
c = 0
while a != r:
	c+=1
	print('第', c, '次嘗試')
	if a > r:
		print('輸入的數字比答案大')
	else:
		print('輸入的數字比答案小')
	a = int(input('請重新輸入一個數字: '))
print('答對啦，總共嘗試了', c+1, '次')