a = True
while a:
    b = input('type something:')
    if b == '1':
        #a = False      #a修改为False 继续执行当前循环 下一次循环终止 
        break           #终止语句跳出执行
        #continue       #跳到下一个循环，不终止
    else:
        pass            #不执行任何功能
    print('still in while')
print('finish')
