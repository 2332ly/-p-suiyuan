'''列表 [] 可变'''
a = [1,2,3,2,3,4]
#访问
print(a,'\n')
print(a[0],'\n')
print(a[-1],'\n')
print(a[0:3],'\n')                   #输出0-2位
print(a[-3:],'\n')                   #输出-3--1

'''多维&嵌套列表'''
a = [1,2,3]
b = [2,3,4]
c = [3,4,5]
dim2_a = [a,b,c]
print(dim2_a,'\n')
dim2_a = [[1,2,3],  #等价
         [2,3,4],
         [3,4,5]]
print(dim2_a)
print(dim2_a[0][1],'\n')

