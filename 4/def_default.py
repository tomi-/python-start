# -*- coding: utf-8 -*-
def odd_val(n=100):
	a = 0;
	while a<=n:
		if a % 2 == 0:
			print(a,end=", ")
		a += 1
odd_val()
print('')
odd_val(10)
print('')
odd_val()