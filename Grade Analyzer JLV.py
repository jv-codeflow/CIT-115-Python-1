# Name: Jasmine Lee Vazquez
# Assignment:   Grade Analyzer
# Reflection:   I liked that this assignment actually made me think instead of just typing code.
#               It felt more like solving a real problem, especially figuring out how to drop the lowest grade.
#               Using pycharm debugger also enhanced my problem-solving experience.

#               I struggled more with organizing everything to make sure all parts of the program worked together correctly.
#               I feel comfortable with if/elif/else statements, but I still rely on referencing past work to structure them properly.
#               It was more about putting all the logic together correctly and fixing small errors that came up along the way.
#
#               One decision I made in my program was to display all errors at once instead of stopping at the first one.
#               I did this by using a flag variable (bError) so the program could check all test scores before exiting. I chose
#               this approach based on past experience (correspondence configuration) where showing only one error at a time to
#               the end user was inefficient, and it was more helpful to identify everything that needed to be corrected at once.
#
#               To figure out how to drop the lowest grade, I started with the first test score and treated it like it was the lowest
#               then I compared it to the other test scores and updated it if I found a lower one. This is how I was able to accomplish
#               coding the average calculation one time for both scenarios.

#               Three things I learned on this assignment:
#               1. How to use if/elif/else statements to compare multiple values
#               2. How to calculate averages based on different conditions and format
#               3. How to stop the program using raise system exit



# 1. Get input:

sNameJLV = input("Name of the person that we are calculating the grades for: ")
iTest1JLV = int(input("Test 1: "))
iTest2JLV = int(input("Test 2: "))
iTest3JLV = int(input("Test 3: "))
iTest4JLV = int(input("Test 4: "))
sLowestGradeJLV = input("Do you wish to drop the lowest grade? (Y/N) ").upper()


# 2. Flag if any test scores < 0 and print error messages, stop program

bErrorJLV = False

if iTest1JLV < 0:
    print("Test score 1 must be greater than 0!")
    bErrorJLV = True
if iTest2JLV < 0:
    print("Test score 2 must be greater than 0!")
    bErrorJLV = True
if iTest3JLV < 0:
    print("Test score 3 must be greater than 0!")
    beErrorJLV = True
if iTest4JLV < 0:
    print("Test score 4 must be greater than 0!")
    bErrorJLV = True

if bErrorJLV == True:
    raise SystemExit


# 3. Validate input entered is Y or N, otherwise print error message and stop program

if sLowestGradeJLV != "Y" and sLowestGradeJLV != "N":
    print("Enter Y or N to Drop the Lowest Grade!" )
    raise SystemExit


# 4. Drop Lowest = Y: determine which of the 4 test scores is lowest and average the three remaining
#    Drop Lowest = N then average all 4 test scores
#    Average calculation coded 1 time in both scenarios for maximum points

if sLowestGradeJLV == 'Y':
    iLowestJLV = iTest1JLV

    if iTest2JLV < iLowestJLV:
        iLowestJLV = iTest2JLV

    if iTest3JLV < iLowestJLV:
        iLowestJLV = iTest3JLV

    if iTest4JLV < iLowestJLV:
        iLowestJLV = iTest4JLV

    fAverageJLV = float(iTest1JLV + iTest2JLV+ iTest3JLV + iTest4JLV - iLowestJLV) / 3

else:
    fAverageJLV = float(iTest1JLV + iTest2JLV + iTest3JLV + iTest4JLV) / 4

# 5. Determine the test average letter grade

if fAverageJLV >= 97.0:
    sGradeJLV = "A+"
elif fAverageJLV >= 94.0:
    sGradeJLV = "A"
elif fAverageJLV >= 90.0:
    sGradeJLV = "A-"
elif fAverageJLV >= 87.0:
    sGradeJLV = "B+"
elif fAverageJLV >= 84.0:
    sGradeJLV = "B"
elif fAverageJLV >= 80.0:
    sGradeJLV = "B-"
elif fAverageJLV >= 77.0:
    sGradeJLV = "C+"
elif fAverageJLV >= 74.0:
    sGradeJLV = "C"
elif fAverageJLV >= 70.0:
    sGradeJLV = "C-"
elif fAverageJLV >= 67.0:
    sGradeJLV = "D+"
elif fAverageJLV >= 64.0:
    sGradeJLV = "D"
elif fAverageJLV >= 60.0:
    sGradeJLV = "D-"
else:
    sGradeJLV = "F"

# Output

if sGradeJLV == 'A+' or sGradeJLV =='A' or sGradeJLV == 'A-':
    print("""-----------------------------------------WOW! Amazing Job!------------------------------------------------
                                                *                                                                    
                                               * *                                                                  
                                              * * *                                                                 
                                             * * * *                                                                
                                     * * * * * * * * * * * * *                                                   
                                        * * * * * * * * * *                                                         
                                           * * * * * * *                                                            
                                          * * * * * * * *                                                           
                                         * * * *   * * * *                                                          
                                        * * *         * * *                                                         
                                       * *               * *                                                        
                                      *                     *                                                       
    ------------------------------------------------------------------------------------------------------------""")

print(f"{sNameJLV}'s test average is: {fAverageJLV:.1f}")
print(f"Letter grade for this test is: {sGradeJLV}")