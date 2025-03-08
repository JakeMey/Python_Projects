class Transaction:
    @staticmethod

    def main():
        print("Please insert card")
        
        #Sets initial balance
        balance = 1000
        
        while True:
            #Prompts for PIN
            pin_input = input("Please enter your PIN: ")
            
            #Checks if PIN is correct
            if pin_input == "1234":
                # Prompts for Account Type
                account_type = input("Enter Account Type (e.g., Savings, Checking): ")
                
                #Displays opening balance
                print(f"Opening balance: ${balance}")
                
                #Prompts for transaction type
                transaction_type = input("Enter transaction type (D for Deposit, W for Withdrawal): ")
                
                #Checks transaction type
                if transaction_type == 'D':
                    #Prompts for deposit amount
                    deposit_amount = float(input("Enter deposit amount: "))
                    
                    #Calculates balance
                    balance += deposit_amount
                    
                    #Displays closing balance
                    print(f"Closing balance: ${balance}")
                    print("Please remove card")
                    print("Transaction complete. Thank you")

                    exit()
                    
                elif transaction_type == 'W':
                    #Prompts for withdrawal amount
                    withdrawal_amount = float(input("Enter withdrawal amount: "))
                    
                    #Checks if sufficient balance
                    if withdrawal_amount > balance:
                        #Insufficient balance
                        print("Insufficient funds in account. Transaction cancelled")
                        print("Please remove card")
                    else:
                        #Calculates balance
                        balance -= withdrawal_amount
                        
                        #Displays closing balance
                        print(f"Closing balance: ${balance}")
                        print("Transaction complete")
                        print("Please remove card")
                        
                else:
                    #Invalid transaction type
                    print("Error selecting transaction type. Please try again")
            
            else:
                #Invalid PIN
                print("Invalid PIN. Please remove card")
                break

#Calls the main function to start the transaction program        
Transaction.main()