try:
    file = open('eeee.txt','r+')
except Exception as e:
    print('no file named as eeee.txt')
    response = input('do you want to careate a new file')
    if response =='y':
        file = open('eeee.txt','w')
        file.close()
    else:
        pass
else:
    file.write('This is text with eeee')
    file.close()
    
