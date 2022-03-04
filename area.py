class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
a=int(input("enter length of rectangle1: "))
b=int(input("enter breadth of rectangle1: "))
r1= rectangle(a,b)
c=int(input("enter length of rectangle2: "))
d=int(input("enter breadth of rectangle2: "))
r2=rectangle(c,d)
print("perimeter of rectangle1",r1.perimeter())
print("area of rectangle1",r1.area())
print("area of rectangle2",r2.area())
print("perimeter of rectangle2",r2.perimeter())
if r1.area()==r2.area():
    print("both areas are same")
else:
    print("not equal")
