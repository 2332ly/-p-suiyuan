APPLE = 100           #全局
a = None
def fun():
    global a
    a = 10
    return a+100
print(APPLE)
print(a)
print(fun())
print(a)


