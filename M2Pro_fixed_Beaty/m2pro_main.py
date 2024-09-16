#import function file

import m2pro_functions as fn

#constants fro menu options


CALC_FV = 1
EXIT = 2

# main function
def main():

    # Local variables to hold user input
    presentValue = 0.0
    interestRate = 0.0
    months = 0
    futureValue = 0.0

    # Set menu option to None 

    choice = "None"

    # start loop

    while choice != EXIT:

        #display menu
        fn.menu()

        # ask for choice

        choice = int(input("Enter Choice: "))
        if choice == CALC_FV:

            # Get user input for specific values
            presentValue = float(input('\nEnter the present value of the account in dollars: '))
            
            interestRate = float(input('Enter the monthly interest rate as a  percentage: '))
            
            months = int(input('Enter the number of months: '))

            # Get expected future value of the account
            futureValue = fn.getFutureValue(presentValue, interestRate, months)

            print ('\nThe information for your account is:')
            print(f'Present value: ${presentValue:,.2f}')
            print('Interest Rate: %', interestRate, sep='')
            print('After ', months, ' months, the value of your account will be $', format(futureValue, ',.2f'), sep='')
            print()
            
        elif choice == EXIT:

            print("\nProgram Terminating....")

        else:

            print("\nINVALID ENTRY!!!")
            print("Enter a Valid menu option\n")
            print()

            




    
# Call the main function.
if __name__ == "__main__":
    
    main()


