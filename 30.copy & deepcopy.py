import copy         #引入copy模块
a = [1,2,[3,4]]
b = a
print(id(a),id(b))  #id()索引地址
b[0] = 11
a[1] = 22
print(b,'\n')

'''copy 浅复制'''
c = copy.copy(a)
print(id(a)==id(c))
c[1] = 222
print(a,c)
print(id(a[2])==id(c[2]))   #第二层列表同一索引
a[2][0] = 333
print(c,'\n')

'''deepcopy 深复制'''
d = copy.deepcopy(a)
print(id(a)==id(d))
print(id(a[2])==id(d[2]))   #全部不同

