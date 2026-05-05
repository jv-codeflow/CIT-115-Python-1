# Name:         Jasmine Lee Vazquez
# Assignment:   Paint Estimator
# Reflection:   I liked that this assignment helped me understand how everything connects together in a real program.
#               It was not just calculations, but also getting input, validating it, using functions, and creating
#               output to a file.  I also liked seeing how the program can actually produce something useful like a
#               cost estimate but my favorite part really was seeing the file generate.

#               I had the most difficulty with understanding how to properly use functions and pass values between them.
#               At first it was confusing knowing what variables belong inside a function vs outside. I also had some
#               difficulty with formatting the output and writing to a file without errors.

#               A function is a block of code that does a specific task. Functions are created using "def" + name + 
#               parameter(s). The function gets called, processes data, and returns the result to where it was called
#               from.

#               Two reasons why functions should be used:
#               1. Functions break the program into smaller pieces of code that can be coded by different programmers.
#               2. It saves time because you can reuse functions across programs instead of having to rewrite it.

########################################################################################################################
# Load contents of math module
########################################################################################################################

import math

########################################################################################################################
# Function 1: Main logic for the program - get input and call functions
########################################################################################################################

def main():

# Prompt for input (float) and call function which validates input as the prompts are answered:
    fSquareFeetJLV = getFloatInputJLV("Enter wall space in square feet: ")
    fPaintPriceJLV = getFloatInputJLV("Enter paint price per gallon: ")
    fFeetPerGallonJLV = getFloatInputJLV("Enter feet per gallon of paint: ")
    fLaborHoursPerGallonJLV = getFloatInputJLV("How many labor hours per gallon: ")
    fLaborChargeJLV = getFloatInputJLV("Labor charge per hour: ")

# Prompt for state (string) and convert to upper case:
    sStateJLV = input("Enter state (CT, MA, ME, NH, RI, VT): ").upper()

# Prompt for last name (string) and call function to validate input:
    sLastNameJLV = getFileInputJLV("Enter customer last name: ")
   
# Call functions and store results in variables:
    iGallonsJLV = getGallonsOfPaintJLV(fSquareFeetJLV, fFeetPerGallonJLV)
    fLaborHoursJLV = getLaborHoursJLV(fLaborHoursPerGallonJLV, iGallonsJLV)
    fLaborCostJLV = getLaborCostJLV(fLaborHoursJLV, fLaborChargeJLV)
    fPaintCostJLV = getPaintCostJLV(iGallonsJLV,fPaintPriceJLV)
    fTaxRateJLV = getSalesTaxJLV(sStateJLV)

    showCostEstimateJLV(iGallonsJLV, fLaborHoursJLV, fLaborCostJLV, fPaintCostJLV, fTaxRateJLV, sLastNameJLV)

########################################################################################################################
# Function 2: Get Float Input
########################################################################################################################

def getFloatInputJLV(sPromptJLV):
    while True:
        try:
            fValueJLV = float(input(sPromptJLV))
            if fValueJLV > 0:
                return fValueJLV
            else:
                print("Please enter a positive number. ")
        except ValueError:
            print("Please enter a numeric value. ")

########################################################################################################################
# Function 3: Get File Input
########################################################################################################################

def getFileInputJLV(sPromptJLV):
    while True:
        try:
            sValueJLV = input(sPromptJLV)
            if sValueJLV != "" and sValueJLV != " ":
                return sValueJLV
            else:            
                print("Please enter a valid last name. ")
        except ValueError:
            print("Please enter a valid last name. ")

########################################################################################################################
# Function 4: Gallons of Paint = Square Feet / Feet Per Gallon + Round Up
########################################################################################################################

def getGallonsOfPaintJLV(fSquareFeetJLV, fFeetPerGallonJLV):
    return math.ceil(fSquareFeetJLV / fFeetPerGallonJLV)

########################################################################################################################
# Function 5: Labor Hours = Gallons Needed * Labor Hours Per Gallon
########################################################################################################################

def getLaborHoursJLV(fLaborHoursPerGallonJLV, iGallonsJLV):
    return fLaborHoursPerGallonJLV * iGallonsJLV

########################################################################################################################
# Function 6: Labor Cost = Labor Hours * Labor Charge Per Hour
########################################################################################################################

def getLaborCostJLV(fLaborHoursJLV, fLaborChargeJLV):
    return fLaborHoursJLV * fLaborChargeJLV

########################################################################################################################
# Function 7: Paint Cost = Gallons Needed * Paint Price Per Gallon 
########################################################################################################################

def getPaintCostJLV(iGallonsJLV, fPaintPriceJLV):
    return iGallonsJLV * fPaintPriceJLV

########################################################################################################################
# Function 8: Tax Rate = depends on state
########################################################################################################################

def getSalesTaxJLV(sStateJLV):
    if sStateJLV == "CT":
        return 0.06
    elif sStateJLV == "MA":
        return 0.0625
    elif sStateJLV == "ME":
        return 0.085
    elif sStateJLV == "NH":
        return 0.0
    elif sStateJLV == "RI":
        return 0.07
    elif sStateJLV == "VT":
        return 0.06
    else:
        return 0.0
    
########################################################################################################################
# Function 9: Subtotal = Paint Cost + Labor Cost
#             Tax Amount = Subtotal * Tax Rate
#             Total Cost = Subtotal + Tax Amount
#             Format, print, and generate file with output
########################################################################################################################

def showCostEstimateJLV(iGallonsJLV, fLaborHoursJLV, fLaborCostJLV, fPaintCostJLV, fTaxRateJLV, sLastNameJLV):

    fSubTotalJLV = fLaborCostJLV + fPaintCostJLV
    fTaxAmountJLV = fSubTotalJLV * fTaxRateJLV
    fTotalCostJLV = fSubTotalJLV + fTaxAmountJLV

# Formatted output:
    sOutputLines = ('\n* Paint Job Estimate *\n'
    f'Gallons Needed: {iGallonsJLV}\n'
    f'Labor Hours: {fLaborHoursJLV:,.1F}\n'
    f'Paint Cost: ${fPaintCostJLV:,.2F}\n'
    f'Labor Cost: ${fLaborCostJLV:,.2F}\n'
    f'Tax: ${fTaxAmountJLV:,.2F}\n'
    f'Total Cost: ${fTotalCostJLV:,.2F}\n')

# Print to screen:
    print(sOutputLines)  

# Create file:
    sFileNameJLV = sLastNameJLV + "_PaintJobOutput.txt"

# Write the output lines to file:    
    with open (sFileNameJLV, "w") as file:
        file.write(sOutputLines)

# Confirm when file is created:
    print("File created:", sFileNameJLV)

########################################################################################################################
# Call our main squeeze: main function
########################################################################################################################

main()