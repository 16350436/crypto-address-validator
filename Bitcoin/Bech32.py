def btc_validation(address):
	a = str(address)
	length = 0
	valid = False
	not_btc = False
	for i in a:
		length += 1
	if length == 42:
		if a[2] == '1' and a[0] == 'b' and a[1] == 'c':
			for i in a:
				if i == 'O' or i == 'I':
					not_btc = True
					break
			if not_btc == True:
				return valid 
			else:
				valid = True
				return valid

		else:
			return 'didn\'t start with bc1'
	else:
		return 'it\'s short'