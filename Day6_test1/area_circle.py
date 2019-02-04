class Circle:
    def __init__(self,radius):
        self.radius=radius

    def find_area(self):
        return 3.14*self.radius**2
    def find_perimeter(self):
        return 2*3.14*self.radius
radius=int(input("Enter the radius:"))
r=Circle(radius)
print("Area of circle:",r.find_area())
print("Perimeter of circle:",r.find_perimeter())
