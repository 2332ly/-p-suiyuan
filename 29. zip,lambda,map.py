'''zip'''
a = [1,2,3]
b = [4,5,6]
print(list(zip(a,b)))   #[(a1,b1),(a2,b2),.......]
for i,j in zip(a,b):
    print(i/2,j*2)
print(list(zip(a,a,b,b)))

'''lambda'''
def fun1(x,y):
    return(x+y)
print(fun1(2,3))

fun2 = lambda x,y:x+y   #定义简单函数 参数：功能
print(fun2(2,3))

'''map'''
print(list(map(fun1,[1,2,3],[2,3,4]))) #函数功能绑定 map(函数，[参数1],[参数2])


    
