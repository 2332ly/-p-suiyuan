import time #1
print(time.localtime())
print(time.time(),'\n')

import time as t    #简称为t
print(t.localtime(),'\n')

from time import time,localtime     #调用指定功能
print(localtime(),time(),'\n')
 
from time import*                   #调用所有功能
print(gmtime())
print(localtime())
print(time())
     
