def monero_validation(address):
	a = str(address)
	length = 0
	valid = False
	not_base58 = False
	for i in a:
		length += 1
	if length == 95 or length == 106:
		if a[0] == '4' or a[0] == '8':
			for i in a:
				if i == 'O' or i == '0' or i == 'I' or i == 'l':
					not_base58 = True
					break
			if not_base58 == True:
				return valid 
			else:
				valid = True
				return valid

		else:
			return valid
	else:
		return valid	
