def fun(a,b):
    return(a+b)

class point:
    def assign(self,x,y):
        self.a=x
        self.b=y
    def prt(self):
        print(self.a,self.b)


p1=point()
p1.assign(20,30)
p1.prt()
print(p1.a)
print("sum of two numbers : {} {} {}  " .format(fun(3,5),fun(3,5)+fun(3,5),fun(3,5)))


#the function is independent part of the code 
#method is the function inside the class which will be accessed only with the help of class object
