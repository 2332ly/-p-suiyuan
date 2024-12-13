d = {'apple':1,
     'pear':'a',
     'orange':2}
#in 是否存在键
print('apple' in d) #True
print('a' in d)     #False
#dict.keys() 所有键
print(d.keys())
#dict.values() 所有值
print(d.values())
#dict.items() 变为元组(列表[])形式
print(d.items())
for a,b in d.items():
    print(a,b)


