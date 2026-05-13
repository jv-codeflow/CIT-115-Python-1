# Name:         Jasmine Lee Vazquez
# Assignment:   Final Project
# Reflection:   I liked that this assignment brought together all of the topics we learned throughout the semester
#               into one complete program.  It helped me to better understand how functions, loops, validation, lists
#               and file handling all work together in a real program.
#           
#               I struggled the most with debugging errors, passing variables between functions, and making sure my
#               loops and validation logic worked correctly.  I also found formatting the final output writing the results
#               to a file challenging at first.  
#
#               This semester I learned how to create variables, use arithmetic calculations, build loops, write functions,
#               validate user input, and work with lists and files. Earlier assignements helped prepare me for this project
#               by teaching me how to break large problems into smaller steps and test my code piece by piece.  I also became
#               more comfortable reading error messages and troubleshooting my programs. This final project helped me to better
#               better understand how all the concepts we learned throughout the semester connect together to create a working
#               application.


# Create a Python Mini Banking System
# Variables: to store account balance, tranactions, and user data
# Conversions: handling numeric and string data inputs correctly
# Arithmetic statements: caculating deposits, withdrawals, and balances
# Logical Constructs: validating transactions and checking conditions
# Exception Handling: handling invalid numeric input and other exceptions
# Looping Constructs: handling continuous user input
# Functions: organizing code into reusable components
# Lists: storing transaction history
# String Methods: formatting outputs for better readability
# Files: Save the list to a file for saving and retrieval

#########################################################################################################################
# Function 1: Main
#             Welcome Message
#             Prompt for input, set variables, create lists, call functions, loop, if/elif/else
######################################################################################################################### 

def main():

    fBalanceJLV = 0.0
    sTransactionTypeJLV = []
    sTransactionAmountJLV = []

    while True:
        print("Hello and Welcome to Jasmine's Python Mini Banking System")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Calculate and Apply Interest")
        print("6. Exit")
        
        iSelectionJLV = PromptForMenuInputJLV("Choose an option (1-6): ")

        if iSelectionJLV == 1:
            fBalanceJLV = getDepositJLV(fBalanceJLV,sTransactionTypeJLV,sTransactionAmountJLV)
        
        elif iSelectionJLV == 2:
            fBalanceJLV = getWithdrawJLV(fBalanceJLV,sTransactionTypeJLV,sTransactionAmountJLV)

        elif iSelectionJLV == 3:
            getCheckBalanceJLV(fBalanceJLV)

        elif iSelectionJLV == 4:
            getTransactionHistoryJLV(sTransactionTypeJLV,sTransactionAmountJLV)

        elif iSelectionJLV == 5:
            fBalanceJLV = getInterestApplicationJLV(fBalanceJLV,sTransactionTypeJLV,sTransactionAmountJLV)
            
        else:
            getProduceStatementJLV(fBalanceJLV,sTransactionTypeJLV,sTransactionAmountJLV)
            break

#########################################################################################################################
# Function 2: Input validation - data type: integer
#########################################################################################################################
def PromptForMenuInputJLV(iPromptJLV):

    while True:
        try:
            iValueJLV = int(input(iPromptJLV))

            if iValueJLV >= 1 and iValueJLV <= 6:
                return iValueJLV
            else:
                print("Please enter a positive number from 1-6.")

        except ValueError:
            print("Please enter a numeric value.")
          
#########################################################################################################################
# Function 3: Input validation  data type: float
#########################################################################################################################

def PromptFloatInputJLV(fPromptJLV):

    while True:
        try:
            fValueJLV = float(input(fPromptJLV))

            if fValueJLV > 0:
                return fValueJLV
            else:
                print("Enter a number that is > 0")

        except ValueError:
            print("Enter a number that is > 0")
   
#########################################################################################################################
# Function 4: Deposits
#########################################################################################################################

def getDepositJLV(fBalanceJLV,sTransactionTypeJLV, sTransactionAmountJLV):

    fDepositAmountJLV = PromptFloatInputJLV("Enter deposit amount: ")

    fBalanceJLV = fBalanceJLV + fDepositAmountJLV

    sTransactionTypeJLV.append("Deposited")
    sTransactionAmountJLV.append(fDepositAmountJLV)

    print(f"Deposit successful! New balance: ${fBalanceJLV:,.2f}")

    return fBalanceJLV

#########################################################################################################################
# Function 5: Withdrawals
#########################################################################################################################

def getWithdrawJLV(fBalanceJLV, sTransactionTypeJLV, sTransactionAmountJLV):

    fWithdrawAmountJLV = PromptFloatInputJLV("Enter withdrawal amount: ")

    while fWithdrawAmountJLV > fBalanceJLV:
        print("Insufficient funds.")
        fWithdrawAmountJLV = PromptFloatInputJLV("Enter withdrawal amount: ")

    fBalanceJLV = fBalanceJLV - fWithdrawAmountJLV

    sTransactionTypeJLV.append("Withdrew")
    sTransactionAmountJLV.append(fWithdrawAmountJLV)

    print(f"Withdrawal successful! New balance: ${fBalanceJLV:,.2f}")

    return fBalanceJLV

#########################################################################################################################
# Function 6: Check balance
#########################################################################################################################

def getCheckBalanceJLV(fBalanceJLV):

    print(f"Your current balance is: ${fBalanceJLV:,.2f}")

#########################################################################################################################
# Function 7: Apply interest
#########################################################################################################################

def getInterestApplicationJLV(fBalanceJLV, sTransactionTypeJLV, sTransactionAmountJLV):

    if fBalanceJLV == 0:
        print("Balance is $0.00. No interest will be calculated.")
    else:
        fInterestRateJLV = PromptFloatInputJLV("Enter annual interest rate: ")

        fMonthlyInterestJLV = fBalanceJLV * (fInterestRateJLV / 100 / 12)

        fBalanceJLV = fBalanceJLV + fMonthlyInterestJLV

        sTransactionTypeJLV.append("Interest")
        sTransactionAmountJLV.append(fMonthlyInterestJLV)

        print(f"Interest applied: ${fMonthlyInterestJLV:,.2f} New balance: ${fBalanceJLV:,.2f}")
       
    return fBalanceJLV

#########################################################################################################################
# Function 8: Transaction history
#########################################################################################################################

def getTransactionHistoryJLV(sTransactionTypeJLV, sTransactionAmountJLV):

    print("\nTransaction History")
    print("+" + "-" * 42 + "+")

    if len(sTransactionTypeJLV) == 0:
        print("No transactions yet.")
    else:
        for iIndexJLV in range(len(sTransactionTypeJLV)):
            print(f"{sTransactionTypeJLV[iIndexJLV]:<20} ${sTransactionAmountJLV[iIndexJLV]:>10,.2f}")

    print("+" + "-" * 42 + "+")        

#########################################################################################################################
# Function 8: Produce final output - print to screen and file
#########################################################################################################################

def getProduceStatementJLV(fBalanceJLV,sTransactionTypeJLV,sTransactionAmountJLV):

    print("\nJasmine's Python Mini Banking System")
    print("Transaction History:")
    print("+" + "-" * 42 + "+")

    sOutputLinesJLV = ("Jasmine's Python Mini Banking System\n"
    "Transaction History:\n"
    "+" + "-" * 42 + "+\n")

    if len(sTransactionTypeJLV) == 0:
        print("No transactions were completed.")
        sOutputLinesJLV += "No transactions were completed.\n"
    else:
        for iIndexJLV in range(len(sTransactionTypeJLV)):
            sLineJLV = (f"{sTransactionTypeJLV[iIndexJLV]:<12}"
                f"$ {sTransactionAmountJLV[iIndexJLV]:>10,.2f}")

            print(sLineJLV)
            sOutputLinesJLV += sLineJLV + "\n"

    print("+" + "-" * 42 + "+")
    print(f"Number of transactions: {len(sTransactionTypeJLV)}")
    print(f"Ending Balance: ${fBalanceJLV:,.2f}")

    sOutputLinesJLV += "+" + "-" * 42 + "+\n"
    sOutputLinesJLV += (f"Number of transactions: "
        f"{len(sTransactionTypeJLV)}\n")

    sOutputLinesJLV += (f"Ending Balance: ${fBalanceJLV:,.2f}\n")

    with open("jlvBankStatements.txt", "w") as file:
        file.write(sOutputLinesJLV)

#########################################################################################################################
# Function 9: Call Main
#########################################################################################################################
main()        
