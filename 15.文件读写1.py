text = 'This is my first test.\nThis is next line.\nThis is last line.'
print(text)
my_file = open('my file.txt','w') #w write r read
my_file.write(text)
my_file.close()
