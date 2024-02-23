from abc import ABC,abstractmethod
from math import sqrt

class Shape(ABC):

    @abstractmethod
    def area(self):
        raise NotImplementedError("Function Not Implemented")

class Triangle(Shape):
    def __init__(self,base,height) -> None:
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height

class Square(Shape):
    def __init__(self,side) -> None:
        self.side = side
    def area(self):
        return self.side**2

class Pentagon(Shape):
    def __init__(self,side) -> None:
        self.side = side
    def area(self):
        return (1/4)*sqrt(5*(5+(2*sqrt(5))))*(self.side**2)

class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)

def execute():
    ch='y'
    while(ch=='y'or ch=='Y'):
        print("-- Area of Shapes --")
        choice = int(input("1.Triangle\t2.Square\n3.Pentagon\t4.Circle\n\nEnter your choice : "))
        if choice==1:
            print("-- Triangle --")
            base=int(input("Base(cm) : "))
            height=int(input("Height(cm) : "))
            Triangle1 = Triangle(base,height)
            area = Triangle1.area()
        elif choice==2:
            print("-- Square --")
            side=int(input("Side(cm) : "))
            Square1=Square(side)
            area = Square1.area()
        elif choice==3:
            print("-- Pentagon --")
            side=int(input("Side(cm) : "))
            Pentagon1=Pentagon(side)
            area = Pentagon1.area()
        elif choice==4:
            print("-- Circle --")
            radius=int(input("Radius(cm) : "))
            Circle1=Circle(radius)
            area = Circle1.area()
        else:
            print("INVALID CHOICE !!")
        print(f"Area : {area} sqcm")
        ch=input("Do you wish to calculate another area?(Y/N) : ")

execute()

    
        
