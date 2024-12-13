file = open('my file.txt','r')
'''content = file.read()
print(content)'''
first = file.readline()
print(first)
second = file.readline()
print(second)
content = file.readlines()
print(content)
