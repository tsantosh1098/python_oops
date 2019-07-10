class arr:
    def __init__(self,x,y,z):
        self.a=x
        self._b=y
        self.__c=z
        self.__prtq(x)

    def prt(self):
        print(self.a,self._b,self.__c)

    def __prtq(self,x):
        print("hekko: {}".format(x))

p1=arr(1,2,3)
p1.prt()
print(p1._arr.__c)

