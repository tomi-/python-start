# -*- coding: utf-8 -*-

def make_incrementor(n):
	return lambda x: x+n

f = make_incrementor(30)
print(f(0));
print(f(5))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(pairs);
pairs.sort(key=lambda pair: pair[1])

print(pairs);
