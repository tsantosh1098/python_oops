class a:
    def m(self):
        print("This is a")
class b:
    def m(self):
        print("This is b: ")
        
class c(a,b):
    pass
    

if __name__=="__main__":
    p1=c()
    p1.m()
