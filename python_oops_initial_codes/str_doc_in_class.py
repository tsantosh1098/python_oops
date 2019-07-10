'This code is used to save 3d co-ordinates'
class point:
    'this class is used to save only one 3d point'
    def __init__(self,x,y,z):
        'This init method will call all methods'
        self.assign(x,y,z)
        self.prt()

    def assign(self,x,y,z):
        'This is called by object when we need to assign user defined variables'
        self.a=x
        self.b=y
        self.c=z
    def prt(self):
        'This method is used to print the co-ordinate'
        print(self.a,self.b,self.c)


#to know what for this code is then
# print(__doc__)
#if u want to know about any specific method in class then
p1=point(2,8,6)
# print(p1.assign.__doc__)
# print(p1.prt.__doc__)

#if u need what class do then
# print(p1.__doc__)

#if u need any help from class
# print(help(p1))

#if u need any help to specific method of class
print(help(p1.assign))

