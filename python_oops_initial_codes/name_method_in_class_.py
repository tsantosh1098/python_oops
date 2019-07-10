# class point:
#     def __init__(self,x,y,z):
#         self.a=x
#         self.b=y
#         self.c=z
#     def prt(self):
#         print(self.a,self.b,self.c)
# p1=point(2,3,4)
# p1.prt()

# 
# class point:
#     def __init__(self,x,y,z):
#         self.assign(x,y,z)
#whenever we want to call the other method within a class we call it using object.method
#here self refers to the called object so self.assign() and parameters are passed without self
#bcz by default self(called object is the first parameter of all methods in the class)
    
#     def assign(self,x,y,z):
#         self.a=x
#         self.b=y
#         self.c=z

#     def prt(self):
#         print(self.a,self.b,self.c)


# def main():
#     p1=point(2,3,4)
#     p1.prt()

# if __name__=="__main__":
#     main()



class point:
    def __init__(self):
        self.a=None
        self.b=None
        self.c=None
        
        
    def assign(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def prt(self):
        print(self.a,self.b,self.c)

def main():
    p1=point()
    p1.assign(2,3,4)
    p1.prt()


if __name__=="__main__":
    main()
    
