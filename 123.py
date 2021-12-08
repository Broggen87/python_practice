password = '123456'
b = 3
while b > 0:
	a = input('請輸入密碼: ')
	if a == password:
		print('登入成功')
		break
	elif b > 1:
		b-=1
		print('密碼錯誤! 還有', b, '次機會')
	else:
		print('密碼輸入錯誤已達三次，請一小時後再嘗試!')
		break