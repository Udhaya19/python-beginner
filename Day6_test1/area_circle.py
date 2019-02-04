class Circle:
    def find_area_perimeter(self,radius,pi):
        self.radius=radius
        self.pi=pi
        print("area:",pi*radius**2)
        print("Perimeter:",2*pi*radius)

c=Circle()
c.find_area_perimeter(3,3.14)