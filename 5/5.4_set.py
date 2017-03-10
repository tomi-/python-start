# -*- coding: utf-8 -*-

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

print('orange' in basket)

a = set('abracadabra')
b = set('alacazam')

# ユニーク
print(a)
print(b)

# a not in b
print(a-b)
# a or b
print(a|b)
# a and b
print(a&b)
# a nand b
print(a^b)