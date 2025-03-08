#Creates Rectangle class
class Rectangle:

    def __init__(self, name, length, width):
        self.__name = name
        self.__length = length
        self.__width = width

    def getName(self):
        return self.__name
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def __str__(self):
        return "Name: " + self.__name + "\nLength = " + (self.__length) + "\nWidth = " + (self.__width)
    
    #Creates calculateArea function for Rectangle class to implement polymorphism
    def calculateArea(self):
        area = self.__length * self.__width
        print("Area formula = length x width")
        print("Length = " + str(self.__length))
        print("Width = " + str(self.__width))
        print("Area of " + self.__name + ": " + str(area))

    #Creates calculatePerimiter function for Rectangle class to implement polymorphism
    def calculatePerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        print("Perimeter formula = 2 x (length + width)")
        print("Length = " + str(self.__length))
        print("Width = " + str(self.__width))
        print("Perimeter of " +self.__name + ": " + str(perimeter))
