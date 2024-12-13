class Calculator:
    name = 'Good calculator'
    pice = 18
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
cal = Calculator()
