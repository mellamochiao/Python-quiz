print('welcome to the calculator program !')	#歡迎訊息
choice = ''
while choice != 'no':	#當選擇不為no時執行
	n1 = float(input('Enter the first number :'))
	n2 = float(input('Enter the second number :'))
	c =  input('Select an arithmetic operation (+, -, *, /) :')
	#分符號進行運算
	if c == '+':
		print('Resilt : ', n1+n2)
	if c == '-':
		print('Resilt : ', n1-n2)
	if c == '*':
		print('Resilt : ', n1*n2)
	if c == '/':
		if n2 != 0:						#考慮除以零的情況
			print('Resilt : ', n1/n2)
		else :
			print('Error : division by zero')
			continue
	choice = input('Do you want to perform another calculation? (yes/no)')
	if choice == 'no':
		print('Goodbye~')					#再見


