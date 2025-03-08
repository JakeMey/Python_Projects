#Creates arithmetic class with main() static function
class Arithmetic:
    @staticmethod

    def main():
        #Creats while loop to continuously prompt user for input
        while True:    
            
            #Prompts user for the first number using input function
            num1 = input("Enter 1st number ")
            
            #Checks if the input is a digit
            if not num1.isdigit():
                print("Error: Please enter a number. ")
                continue #Restart the loop if input condition is invalid
            
            #Converts the first input to an integer
            number1 = int(num1)

            #Prompts the user for second number using input function
            num2 = input("Enter 2nd number ")

            #Checks if the input is a digit
            if not num2.isdigit():
                print("Error: Please enter a number. ")
                continue #Restart the loop if input condition is invalid
            
            #Converts the second number to an integer
            number2 = int(num2)

            #Prompts the user for arithmetic operation using input function
            arithmetic_op = input("Please enter arithmetic operation +, -, * or /: ")

            #Performs addition if the operation is '+'
            if arithmetic_op == '+':
                arithmetic_op_addition = number1 + number2
                print(f"{number1} + {number2} = {arithmetic_op_addition}")

            #Performs subtraction if the operation is '-'
            elif arithmetic_op == '-':
                arithmetic_op_subtract = number1 - number2
                print(f"{number1} - {number2} = {arithmetic_op_subtract}")

            #Performs multiplication if the operation is '*'
            elif arithmetic_op == '*':
                arithmetic_op_multiply = number1 * number2
                print(f"{number1} * {number2} = {arithmetic_op_multiply}")
            
            #Performs division if the operation is '/'
            elif arithmetic_op == '/':
                    if number2 !=0:
                        arithmetic_op_division = number1 / number2
                        print(f"{number1} / {number2} = {arithmetic_op_division}")
                    else:
                        print("Error: Cannot divide by zero")
                        continue  #Restarts the loop if trying to divide by zero
            
            #Handles invalid arithmetic operation input
            else:
                print("Error: Please only input an arithmetic operation. ")      

#Calls the main function to start the program
Arithmetic.main()