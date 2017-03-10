# -*- coding: utf-8 -*-

a = 2,4,11

print(a[0])

b = a,(33,4)

print(b)

print(a[0]);

# タプルは上書きできない
# a[0] = 334

# 上書きする必要があるならlistにしよう
v = ([2,4,11],[33,4])
v[1].append('33-4')

print(v)

# 逆の演算もできる
x,y,z = a;
print(x)
print(y)
print(z)