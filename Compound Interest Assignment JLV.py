# Name:         Jasmine Lee Vazquez
# Assignment:   Compound Interest
# Reflection:   I really liked using comments throughout my code.  Writing comments helped me stay organized and not
#               lose my place when the formula started to feel complex. Breaking the compound interest formula into
#               smaller steps made it easier to understand what each line was doing.  The comments acted like
#               checkpoints for my thinking.

#               I struggled with the math, specifically towards the end on the exponent but once I figured it out, it
#               wasn't as hard as it seemed. I wish there was a way for me to insert a picture of the formula in python
#               so I could easily reference it as I built the code vs toggling between the pages on instructions.

#               The () is important because it controls the order of operations.  Without () the calculations will not
#               be accurate. You must always do it according to this order PEMDAS: Parenthesis, exponent, multiplication,
#               division, addition, subtraction.

#               1.  I learned how to correctly apply the compound interest formula in coded by breaking it into smaller
#                   steps.

#               2.  I strengthened my understanding of PEMDAS and why parentheses matter in the math

#               3.  I practiced using if/else statements and improved my confidence in formatting and calculating a
#                   future investment value.


#1. Prompt the user for all required inputs and convert to the appropriate numeric data type that can store decimals:

# (PV) Capture principle investment and convert to a float
fPrincipleInvestmentJLV = float(input("Enter the starting principal: "))

# (R) Capture interest rate and covert to a float
fInterestRateJLV = float(input("Enter the annual interest rate: "))

# (m) Capture Compounding and convert to a float
fCompoundingJLV = float(input("How many times per year is the interest compounded? "))

# (t) Capture number of periods and convert to a float
fNumberofPeriodsJLV = float (input("For how many years will the account earn interest? "))

#2. Calculate future value using formula

# Convert interest rate from a percent to decimal (r)
fInterestDecimalJLV = fInterestRateJLV / 100

# FV = PV (1 + r / m) ** mt

# Calculate interest rate per compounding period (r / m)
fCompoundInterestJLV = fInterestDecimalJLV / fCompoundingJLV

# Add 1 to the periodic interest rate (1 + r / m)
fParenthesisJLV = fCompoundInterestJLV + 1

# Calculate total number of times interest is applied (m * t)
fCompoundTotalYearsJLV = fCompoundingJLV * fNumberofPeriodsJLV

# Raise the base to the total number of periods (1 + r/m) ** (m*t)
fCompoundTotalPeriods = fParenthesisJLV ** fCompoundTotalYearsJLV

# Multiply by principal to get the final future value
fFutureValueJLV = fPrincipleInvestmentJLV * fCompoundTotalPeriods

#3. Output formatted as currency with conditional logic to display the number of periods in an int or float format

if fNumberofPeriodsJLV == int(fNumberofPeriodsJLV):
    print(f"At the end of {int(fNumberofPeriodsJLV)} years you will have $,{fFutureValueJLV:.2f}")
else:
    print(f"At the end of {float(fNumberofPeriodsJLV)} years you will have $,{fFutureValueJLV:.2f}")