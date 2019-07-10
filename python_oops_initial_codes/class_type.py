class point:
    def __init__(self,a,b,c):
        self.x=a
        self.y=b
        self.z=c
        self.prt()


    def prt(self):
        print(self.x,self.y,self.z)

p1=point(12,56,34)
p2=point(123,563,343)

#this will tell type of the variable p1 and p2
print(type(p1))
print(type(p2))
a=9
print(type(a))


