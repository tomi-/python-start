# -*- coding: utf-8 -*-
def odd_val(n=100, L=[]):
	a = 0;
	while a<=n:
		if a % 2 == 1:
			print(a,end=", ")
		else:
			L.append(a)
		a += 1
	return L;
print(odd_val())
print('')
print(odd_val(10))
print('')
print(odd_val())


