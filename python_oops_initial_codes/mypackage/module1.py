class triangle:

    def __init__(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z

    def prt(self):
        print(self.a,self.b,self.c)
    
def main():
    p1=triangle(3,4,5)
    p1.prt()
    
if __name__=="__main__":
    main()