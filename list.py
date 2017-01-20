# -*- coding: utf-8 -*-
list = [1,2,3,4]
print(list)
list[2]=33
print(list)
list.append(5)
print(list)

list[1:2] = [9,8]
print(list)
list[1:2] = [1,2,3]
print(list)

list[1:2] = []
list[3:5] = []
print(list);