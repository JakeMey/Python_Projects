#Creates Square class
class Square:

    def __init__(self, name, length):
        self.__name = name
        self.__length = length

    def getName(self):
        return self.__name
    
    def getLength(self):
        return self.__length
    
    def __str__(self):
        return "Name: " + self.__name + "Length = " + self.__length
    
    #Creates calculateArea function for Square class to implement polymorphism
    def calculateArea(self):
        area = self.__length * self.__length
        print("Area formula = length x length")
        print("Length = " + str(self.__length))
        print("Area of " + self.__name + ": " + str(area))

    #Creates calculatePerimieter function for Square class to implement polymorphism
    def calculatePerimeter(self):
        perimiter = 4 * self.__length
        print("Perimeter formula = 4 x length")
        print("Length = " + str(self.__length))
        print("Perimeter of " +self.__name + ": " + str(perimiter))