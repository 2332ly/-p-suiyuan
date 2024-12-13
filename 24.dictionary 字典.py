'''创建字典
{键key：值value}'''
d = {'apple':1,     #没有顺序
     'pear':'a',
     'orange':2}
print(d['apple'],'\n')  
print(d.get('apple'),'\n')  #get访问
#dict()
d1 = dict({'apple':2,4:'car'})
print(d1['apple'],'\n')

#zip() 详见"zip,lambda,map.py"
d3 = {} 
a = [1,2,3]
b = ['apple','car','char']
d3 = dict(zip(a, b))
print(d3,'\n')
#or
for i,j in zip(a,b):
    d3[i] = j
print(d3,'\n')


'''添加元素'''
d['age'] = 20
d.update(gate = 2)  #update添加
print(d,'\n')

#删除元素
del d['age']   
d.pop('apple')
print(d,'\n')
d.clear()   #清除d
print(d,'\n')

#嵌套
d2 = {1:'a',
      'c':d3}    
print(d2)
print(d2['c'][1],'\n')
