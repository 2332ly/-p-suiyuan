print('Hello World','sui','123') #间隔默认空格 ,sep = ' '
#默认换行 end = '\n'
print('Hello World','sui',end = '\t')
print('Hello World','sui','123',sep = '***')

age = 18
name = 'hua'
print('I\'m %s,age %.2f'%(name,age))
#%c 字符 %s字符串 %d整数 %f浮点 %e科学计数

'''str.format() 格式化字符串
{}字符 {:}数字 '''
print('{1} {0} {1}'.format('study','hard'))
#1hard 0study 1hard
year, month, day = 2024, 11, 27
print('{} = {:d},{} = {:d},{} = {:d}'.format('year',year,
                                             'month',month,
                                             'day',day))




