class a:
    def __init__(self,a):
        self.aa=a
        self.bb=None

    def m(self):
        print("The class is a: {} {}".format(self.aa,self.bb))

class b(a):
    def __init__(self,a):
        self.aa=a

    def m(self):
        print("The class is b {}".format(self.aa))
        super().m()

class c(a):
    def __init__(self,a):
        self.aa=a

    def m(self):
        print("The class is c {}".format(self.aa))
        super().m()

class d(b,c):
    def __init__(self,a):
        self.aa=a
        self.bb=None

    def m(self):
        print("The class is d {}".format(self.aa))
        super().m()
        

if __name__=="__main__":
    p1=d(3)
    p1.m()
    