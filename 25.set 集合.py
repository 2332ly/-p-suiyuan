'''集合 {} 无重复 无序'''
s1 = {'apple','pear','sate'}
print(type(s1))
print(s1,'\n')
#set创建 分割
s2 = set('12345')
print(s2,'\n')
s3 = (('apple','peach','banana'))
print(s3,'\n')
'''添加'''
#add
s1.add('orange')    #只能添加一个元素
print(s1,'\n')
#update
s1.update({1,2})
print(s1,'\n')
s1.update([2,3],[3,4])
print(s1,'\n')
'''删除'''
#set.remove(元素)  不存在报错
s1.remove('pear')
print(s1,'\n')
#set.discard()      不报错
s1.discard('apple')
print(s1,'\n')
#set.pop()  由于无序 随机删除 报错
print(s1.pop())
print(s1,'\n')
#运算
ch1 = set('123a')
ch2 = set('1abc')
print(ch1,
      ch2,
      ch1-ch2,          #差集 在 ch1 不在 ch2 
      ch1|ch2,          #并集
      ch1&ch2,          #交集
      ch1^ch2,          #对称差 不同时存在于两者
      ch2.issubset(ch1) #ch2是否是ch1子集
      )


