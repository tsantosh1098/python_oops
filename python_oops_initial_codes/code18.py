class aa:
    def __init__(self):
        self.a=None
    def name1(self,first):
        self.a=first

class bb:
    def __init__(self):
        self.b=None
    def name2(self,last):
        self.b=last

class cc(bb,aa):
    def __init__(self):
        aa.__init__(self)
        bb.__init__(self)
        self.c=None

    def age(self,num):
        self.c=num

    def __str__(self):
        return str(self.a) + " " + str(self.b) + ", " + str(self.c) 

if __name__=="__main__":
    p1=cc()
    
    p1.age(26)
    print(p1)
