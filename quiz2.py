# user input
p = float(input('Enter the shopping amount : '))
l = input('Enter the member ship level : ')

if l == 'Regular':
	if p <=1000:
		print(l,p)
	else:
		if p >= 1000 and p < 2000:
			final_p = p*0.90
			print(l, final_p)
		else:
			if p  < 3000:
				final_p = p*0.85
				print(l, final_p)
			else:
				if p > 3000:
					final_p = p*0.80
					print(l, final_p)
else:
	if l == 'Gold':
		if p <=1000:
			print(l,p)
		else:
			if p >= 1000 and p < 2000:
				final_p = p*0.85
				print(l, final_p)
			else:
				if p  < 3000:
					final_p = p*0.80
					print(l, final_p)
				else:
					if p > 3000:
						final_p = p*0.75
						print(l, final_p)
	else: print('Invalid member level. Please enter “Regular” nor “Gold”.')