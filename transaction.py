class transaction:
    @staticmethod

    def main():
        print("Please insert card")
        
        #Set initial balance
        balance = 1000
        
        while True:
            #Prompt for PIN
            pin_input = input("Please enter your PIN: ")
            
            #Check if PIN is correct
            if pin_input == "1234":
                # Prompt for Account Type
                account_type = input("Enter Account Type (e.g., Savings, Checking): ")
                
                #Display opening balance
                print(f"Opening balance: ${balance}")
                
                #Prompt for transaction type
                transaction_type = input("Enter transaction type (D for Deposit, W for Withdrawal): ")
                
                #Check transaction type
                if transaction_type == 'D':
                    #Prompt for deposit amount
                    deposit_amount = float(input("Enter deposit amount: "))
                    
                    #Calculate balance
                    balance += deposit_amount
                    
                    #Display closing balance
                    print(f"Closing balance: ${balance}")
                    print("Please remove card")
                    print("Transaction complete. Thank you")

                    exit()
                    
                elif transaction_type == 'W':
                    #Prompt for withdrawal amount
                    withdrawal_amount = float(input("Enter withdrawal amount: "))
                    
                    #Check if sufficient balance
                    if withdrawal_amount > balance:
                        #Insufficient balance
                        print("Insufficient funds in account. Transaction cancelled")
                        print("Please remove card")
                    else:
                        #Calculate balance
                        balance -= withdrawal_amount
                        
                        #Display closing balance
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
        
transaction.main()