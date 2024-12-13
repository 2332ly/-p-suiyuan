'''
元组 tuple () 不可变
'''
#创建元组
a_tuple = (1,2,3,4,5,6)
b_tuple = 2,4,6,8
c_tuple = (5)   #class 'int'
d_tuple = (5,)  #单个元素加逗号
print(type(a_tuple),type(c_tuple),type(d_tuple),'\n') #类型
#访问元组 0 or -1 起始
print(a_tuple[0],
      a_tuple[-1],
      a_tuple[1:],
      a_tuple[0:3],'\n')
#((包含)起始:结束(不包含))
#函数
print(len(a_tuple),'\n') #元素个数 1起始
print(max(a_tuple),'\n')    #最大值
print(min(a_tuple),'\n')    #最小值
a_list = [1,2,3]
print(type(tuple(a_list)),'\n')     #列表转为元组

#元组操作

print(a_tuple + b_tuple,'\n')    # + 组合
print((1,2,3)+(2,),'\n') 
print(3 in a_tuple,'\n') #判断存在
print(b_tuple*2,'\n')    #复制
a_list = [1,2,3]
print(type(tuple(a_list)),'\n')
#打印
print(a_tuple,b_tuple,'\n')
#遍历
for concent in a_tuple:
    print(concent,end = ' ')
print('\n')
for concent in b_tuple:
    print(concent,end = ' ')
print('\n')
for index in range(len(a_tuple)):
    print('index=',index,'number in list',a_tuple[index])


