import random
r = random.randint(1, 100)
a = int(input('請輸入一個數字 1~100: '))
c = 1
while a != r:
	c+=1
	if a > r:
		print('輸入的數字比答案大')
	else:
		print('輸入的數字比答案小')
	a = int(input('請重新輸入一個數字 1~100: '))
print('答對啦，總共嘗試了', c, '次')