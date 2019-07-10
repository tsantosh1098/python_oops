class person:
    def __init__(self):
        self.a=None
        self.b=None

    def name(self,first,last):
        self.a=first
        self.b=last

class comp(person):
    def __init__(self):
        super().__init__()
        self.c=None
    def emp(self,name):
        self.c=name
    
class ideay(comp):
    def __init__(self):
        super().__init__()
        
        self.d=None
    def num(self,id):
        self.d=id
    def __str__(self):
        return str(self.a) + " " + str(self.b) + ", " + str(self.c) + ", " + str(self.d)
    

p1=ideay()
p1.num(1234)  
p1.emp("bosch")

print(p1)

