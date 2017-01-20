# -*- coding: utf-8 -*-
a,b = 0,1
# Fibonacci
# while 継続条件
while b<100:
	print(b)
	a, b = b, a+b

print('抜けた?');

a,b = 0,1
# 総和
# while 継続条件
while b<100:
	a+=b
	print(a,end=',');
	b=b+1