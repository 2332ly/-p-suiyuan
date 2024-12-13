a = [1,2,3]
b = [2,3,4]
c = [3,4,5]
#列表操作 同元组
print([1,2,3]+[2],
      a+b,
      a*2,
      sep='\n')

#函数 同元组
a_tuple = (1,2,3)
print(len(a),   #元素个数
      min(a),   #最小值
      max(a),   #最大值
      type(list(a_tuple)),  #转为列表
      sep='\n')
print(a,'\n')
print(a.count(1),'\n')      #出现次数
print(a.index(2),'\n')      #返回索引位置
a.sort()                    #从小到大排序覆盖原列表
print(a,'\n')
a.reverse()                 #反向排序
print(a,'\n')               #从大到小
'''等同于
a.sort(reverse = True)      #从大到小
print(a,'\n')'''
#添加元素
a.append(0)
print(a,'\n')
#指定位置添加（位置，内容）
a.insert(1,0)
print(a,'\n')
#删除 list.remove(去掉的值)第一次出现
a.remove(2,)                     
print(a,'\n')

#del list[位置]0起始
del a[-1]
print(a,'\n')

#list.pop(位置)
a.pop(-2)
print(a,'\n')
#遍历
a_list = [1,2,3,4,5,6]
for concent in a_list:
    print(concent)
for index in range(len(a_list)):
    print('index=',index,'number in list',a_list[index])
c = a.copy()    #复制
a.clear()       #清空
print(a,'\n')
print(c,'\n')


