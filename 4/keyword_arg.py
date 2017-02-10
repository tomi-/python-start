# -*- coding: utf-8 -*-
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")
	print("------")

parrot(100); # argument is voltage only.
parrot(100, 'test state'); # argument is voltage and state.
parrot(100, 'test state', 'test action'); # argument is voltage and state and action.


parrot(100, type='type Moon.'); # argument デフォルトのない引数が埋まってれば後はキーワードできるらしい
parrot(voltage=100, type='type Moon.'); # argument 最初の引数をキーワードしたのでそれ以降も必要になるらしい
parrot(voltage=100, type='type Moon.', action=' Action. '); # argument 全部キーワードなら順番は変わっても平気