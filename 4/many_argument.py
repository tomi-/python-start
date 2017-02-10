# -*- coding: utf-8 -*-
def many_arguments(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	keys = sorted(keywords.keys())
	for kw in keys:
		print(kw, ":", keywords[kw])

# many_arguments('Kind.') # *argumentsは必須ではない
# many_arguments('衝撃のファーストブリッド','撃滅のセカンドブリッド','抹殺のラストブリッド') # *arguments keyのない引数

many_arguments('ShellBullet', '衝撃のファーストブリッド','撃滅のセカンドブリッド','抹殺のラストブリッド', first='Bullet', seccond="bullet",last='bullet') # **keywords keyつきの引数

def concat(*arg, sep=","):
	return sep.join(arg)

print(concat('Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'))
print(concat('水','金','地','火','木','土','天王','海王','冥王星',sep="星/"))
