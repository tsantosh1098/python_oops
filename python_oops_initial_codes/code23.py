class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return("({0},{1},{2})".format(self.x,self.y,self.z))

    def __add__(self,other):
        p3=point(self.x + other.x,self.y + other.y,self.z + other.z)
        return p3


def main():
    p1=point(1,2,3)
    p2=point(5,6,7)
    print(p1,p2)
    print(p1 + p2)
    print(p1,p2)
    
if __name__=="__main__":
    main()