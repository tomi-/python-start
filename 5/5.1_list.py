# -*- coding: utf-8 -*-

a = [66.25, 333, 333, 1, 1234.5]

# count(arg) その値の出現回数
print(a.count(333), a.count(66.25), a.count('x'))

# insert(i, x) iの位置にxを挿入
a.insert(2, -1)
print(a)

# append(x) xを最後に追加
# append(len(a), x)と等価
a.append(333)
print(a)

# remove(x) 最初のxを取り除く、ない場合はエラー
a.remove(333)
print(a)

# reverse 逆順にする
a.reverse()
print(a)

# sort 昇順にする
a.sort()
print(a)

# pop 最後の値の取り出し
a.pop()
print(a)

# queue
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())

