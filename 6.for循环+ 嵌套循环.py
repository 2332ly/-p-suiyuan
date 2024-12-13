for i in range(1,5):
    for j in range (1,i+1):
        print('%4d'%(i*j),end = '')
    print('')

#冒泡算法
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n - 1):
    print(i)
    for j in range(n - 1 - i):  
        if arr[j] > arr[j + 1]:  
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
    
