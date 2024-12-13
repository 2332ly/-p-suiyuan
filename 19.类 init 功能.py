class Calculator:
    name = 'Good calculator'
    pice = 18
    def __init__(self,name,price,height,width,weight):
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight
    def add(self,x,y):
        print(self.name)
        result = x+y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        result = x*y
        print(result)
    def divide(self,x,y):
        result = x/y
        print(result)

