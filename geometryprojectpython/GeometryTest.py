#Imports Rectangle and Square classes from Rectangle.py and Square.py
from Rectangle import Rectangle
from Square import Square

#Creates class with main() static function
class GeometryTest:
    @staticmethod
    def main():
        
        shapes = []

        #Creates 2 objects of Rectangle Class
        rectangle1 = Rectangle ("Rectangle 1", 40, 20)
        rectangle2 = Rectangle ("Rectangle 2", 60, 30)

        #Creates 2 objects of Square Class
        square1 = Square ("Square 1", 15)
        square2 = Square ("Square 2", 25)

        shapes.append (rectangle1)
        shapes.append (rectangle2)
        shapes.append (square1)
        shapes.append (square2)

        print("\n")

        #Displays the instance variables of each object of the Rectangle class from the list using getter functions
        print("Rectangle 1")

        print("Name: " + shapes[0].getName())
        print("Length = " + str(shapes [0].getLength()))
        print("Width = " + str(shapes [0].getWidth()))

        print("\n")

        print("Rectangle 2")

        print("Name: " + shapes[1].getName())
        print("Length = " + str(shapes [1].getLength()))
        print("Width = " + str(shapes [1].getWidth()))

        print("\n")

        #Displays the instance variables of each object of the Square class from the list using getter functions
        print("Square 1")
        
        print("Name: " + shapes[2].getName())
        print("Length = " + str(shapes [2].getLength()))

        print("\n")

        print("Square 2")

        print("Name: " + shapes[3].getName())
        print("Length = " + str(shapes [3].getLength()))

        print("\n")

        #Runs the calculateArea() function on all the objects of the Rectangle and Square classes from the list using a for loop demonstrating polymorphism

        for apended in shapes:
            print("\n")
            apended.calculateArea()

        print("\n")

        #Runs the calculatePerimeter() function on all the objects of the Rectangle class from the list using index numbers demonstrating polymorphism

        print("Rectangle 1")
        shapes[0].calculatePerimeter()
        print("\n")
        print("Rectangle 2")
        shapes[1].calculatePerimeter()

        print("\n")

        #Runs the calculatePerimeter() function on all the objects of the Square class from the list using index numbers demonstrating polymorphism

        print("Square 1")
        shapes[2].calculatePerimeter()
        print("\n")
        print("Square 2")
        shapes[3].calculatePerimeter()

        print("\n")

GeometryTest.main()