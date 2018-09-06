def calc(n1, n2, op):
	if op == '+':
		return n1 + n2
	elif op == '-':
		return n1 - n2
	elif op == '*':
		return n1 * n2
	elif op == '/':
		if n2 == 0:
			return 0
		else:
			return n1/n2
#print(calc(4,2,'/'))

def test_calc():
	assert calc(4,2,'+') == 6
