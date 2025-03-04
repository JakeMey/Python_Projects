class arithmetic:
    @staticmethod

    def main():

        while True:    

            num1 = input("Enter 1st number ")
            
            if not num1.isdigit():
                print("Error: Please enter a number. ")
                continue
            
            number1 = int(num1)

            num2 = input("Enter 2nd number ")

            if not num2.isdigit():
                print("Error: Please enter a number. ")
                continue
            
            number2 = int(num2)

            arithmetic_op = input("Please enter arithmetic operation +, -, * or /: ")

            if arithmetic_op == '+':
                arithmetic_op_addition = number1 + number2
                print(f"{number1} + {number2} = {arithmetic_op_addition}")

            elif arithmetic_op == '-':
                arithmetic_op_subtract = number1 - number2
                print(f"{number1} - {number2} = {arithmetic_op_subtract}")

            elif arithmetic_op == '*':
                arithmetic_op_multiply = number1 * number2
                print(f"{number1} * {number2} = {arithmetic_op_multiply}")
            
            elif arithmetic_op == '/':
                    if number2 !=0:
                        arithmetic_op_division = number1 / number2
                        print(f"{number1} / {number2} = {arithmetic_op_division}")
                    else:
                        print("Error: Cannot divide by zero")
                        continue

            else:
                print("Error: Please only input an arithmetic operation. ")      

arithmetic.main()