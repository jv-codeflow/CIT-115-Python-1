# Name:         Jasmine Lee Vazquez
# Assignment:   Compound Interest Loops
# Reflection:   What I liked:
#               I liked learning how to code a difficult math equation.
#               This assignment helped me understand how compound interest works step by step.
#               I also liked seeing the results printed month by month because it made the growth easier to follow.

#               What I struggled with:
#               I struggled with understanding how to connect the math logic into my code, especially within loops.
#               It took some time to see how the calculations were being applied step by step.

#               while and for loops both repeat code until a condition is met.
#               The difference is:
#                  - a for loop runs a set number of times using defined parameters (start, stop,step)
#                  - a while loop continues running until a specific condition is met such as input validation
#
#               Loops used in this assignment: for and while
#                  - I used a for loop when there was a fixed number of months to calculate the amount balance.
#                  - I used while loops to validate user input and determine how many months it would take to reach the
#                    goal amount.

#               Top 3 things I learned:
#                 1. How to calculate compound interest using loops instead of only a formula.
#                 2. How to use while True loop with break to validate input and ensure only positive values are
#                    accepted.
#                 3. That if I forget include a break statement in a while loop, the loop will run indefinitely and
#                    the rest of the program won't run.



#=======================================================================================================================
# Deposit - Prompt user and perform error handling (Data Type: Float)
#=======================================================================================================================

while True:
    try:
        fOriginalDepositJLV = float(input("What is the Original Deposit amount (positive value) "))
        if fOriginalDepositJLV > 0:
            break

        print("Input must be a positive value and not zero")

    except ValueError:
        print("Input must be a numeric value")

#=======================================================================================================================
# Interest Rate - Prompt user and perform error handling (Data Type: Float)
#=======================================================================================================================

while True:
    try:
        fInterestRateJLV = float(input("What is the Interest Rate (positive value) "))
        if fInterestRateJLV > 0:
            break

        print("Input must be a positive value and not zero")

    except ValueError:
        print("Input must be a numeric value")

#=======================================================================================================================
# Months - Prompt user and perform error handling (Data Type: Integer)
#=======================================================================================================================

while True:
    try:
        iMonthsJLV = int(input("What is the Number of Months (positive value) "))
        if iMonthsJLV > 0:
            break

        print("Input must be a positive value and not zero")

    except ValueError:
            print("Input must be a numeric value")

#=======================================================================================================================
# Goal - Prompt the user and perform error handling (Data Type: Float)
#=======================================================================================================================

while True:
    try:
        fGoalJLV = int(input("What is the goal amount? "))
        if fGoalJLV >= 0:
          break

        print("Input must be a positive value")

    except ValueError:
        print("Input must be a numeric value")

#=======================================================================================================================
# Monthly Interest Rate: Convert inputted value to a decimal and divide by 12 (Data Type: Float)
# Set account balance to the starting deposit amount (Data Type: Float)
#=======================================================================================================================

fMonthlyInterestRateJLV = (fInterestRateJLV / 100) / 12
fAccountBalanceJLV = fOriginalDepositJLV

#=======================================================================================================================
# Loop through each month (Start: 1, Stop: total months + 1, Step: 1) (Data Type: Integer)
#    - Calculate interest for current month (Data Type: Float)
#    - Add the calculated interest to the account balance (Data Type: Float)
#    - Output the current month and account balances for each month and format to two decimal points
#=======================================================================================================================

for iMonthJLV in range(1, iMonthsJLV + 1, 1):
    fInterest = fAccountBalanceJLV * fMonthlyInterestRateJLV
    fAccountBalanceJLV = fAccountBalanceJLV + fInterest
    print(f"Month {iMonthJLV}: Account Balance is ${fAccountBalanceJLV:.2f}")

#=======================================================================================================================
# Set balance (Data Type: Float) and month counter (Data Type: Integer)
#=======================================================================================================================

fBalanceJLV = fOriginalDepositJLV
iMonthCounterJLV = 0

#=======================================================================================================================
# Loop until account balance reaches the goal amount
#     - Calculate monthly compounded interest (Data Type: Float)
#     - Add calculated interest to account balance (Data Type: Float)
#     - Increment month counter to track number of months (Data Type: Integer)
#=======================================================================================================================

while fBalanceJLV < fGoalJLV:
    fMonthlyCompoundedAmtJLV = fBalanceJLV * fMonthlyInterestRateJLV
    fBalanceJLV = fBalanceJLV + fMonthlyCompoundedAmtJLV
    iMonthCounterJLV = iMonthCounterJLV + 1

#=======================================================================================================================
# Output number of months it will take to reach goal and format
#=======================================================================================================================

if fGoalJLV > fOriginalDepositJLV:
    print(f"It will take {iMonthCounterJLV:,} months to reach your goal of {fGoalJLV:.2f}.")


