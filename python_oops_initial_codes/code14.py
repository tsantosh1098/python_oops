# class person:
#     def __init__(self,name,aadar):
#         self.a=name
#         self.b=aadar
#     def prt(self):
#         print(self.a,self.b)
    
# class employ(person):
#     def __init__(self,name,aadar):
#         self.a=name
#         self.b=1234
    
#     pass
# def main():
#     p1=person("xyz",87654567)
#     p2=employ("qwe",23498628)
#     p1.prt()
#     p2.prt()

# if __name__=="__main__":
#     main()


class person:

    def __init__(self,name,aadar):
        self.a="santosh"
        self.b=aadar
        self.prt()


    def prt2(self):
        print(self.a,self.b)



class employ(person):
    def __init__(self,name,aadar):
        self.a=name
        self.b=aadar
        

    def prt1(self):
        print("Heloo world")

class boy(employ,person):
    def __init__(self,x,y):
        self.a=x
        self.b=y
        self.prt2()

    def prt(self):
        print("werty")






def main():
    p2=employ("xyz",1234)
    p3=boy("fra",9887)

if __name__=="__main__":
    main()
    