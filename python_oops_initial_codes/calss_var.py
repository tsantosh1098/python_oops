class point:
    aa=345
    a=10
    def assign(self,x,y,z):
        
        self.a=x
        self.b=y
        self.c=z
    aa = 12 
        
        

    def prt(self):
        print(self.a,self.b,self.c)
    
p1=point()
print(p1.aa)
p1.assign(2,3,4)
p2=point()
p2.assign(5,6,7)
p1.prt()
print(p2.a)

