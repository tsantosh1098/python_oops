class person:

    def __init__(self,first,last,age):
        self.a=None
        self.b=None
        self.c=None
        self.assign(first,last,age)

    def assign(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __str__(self):
        return self.a + " " + self.b + ", " + str(self.c)

class employ(person):

    def __init__(self,first,last,age,sal):
        super().__init__(first,last,age)
        self.d=sal
    def __str__(self):
        return super().__str__() + ", " + str(self.d)



p2=employ("james","bond",40,34000)

print(p2)