class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

     

l=int(input("length1 :"))
b=int(input("breadth1 :"))
r1=Rectangle(l,b)
print("r1 area : ",r1.area ())
print("r1 perimeter : ",r1.perimeter())

l2=int(input("length2 :"))
b2=int(input("breadth2 :"))
r2=Rectangle(l2,b2)
print("r2 area : ",r2.area ())
print("r2 perimeter : ",r2.perimeter())

if r1.area()>r2.area() :
    print("r1 area is greater")
else:
    print("r2 area is greater")






