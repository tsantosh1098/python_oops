class student:

    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
    
    def setter(self,a,b,c):
        self.__student_id=a
        self.__age=b
        self.__marks=c

    def getter(self):
        return self.__student_id ,self.__age,self.__marks

    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True

    def validate_age(self):
        if self.__age > 20:
            return True

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks >=65:
                return True
            else:
                return False

def main():
    p1=student()
    p=[]
    p.append(int(input("Enter your student id")))
    p.append(int(input("Enter your student age")))
    p.append(int(input("Enter your student marks")))
    p1.setter(p[0],p[1],p[2])
    p1.getter()
    if p1.check_qualification():
        print("You are elegible")
    else:
        print("Ypu are not elegible")
    



if __name__=="__main__":
    main()