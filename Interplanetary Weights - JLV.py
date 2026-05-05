# Name: Jasmine Vazquez
# Assignment:   Planetary Weights
# Reflection:   What I really liked about this assignment was the opportunity to
#               experiment with formatting options and see how changing the numbers
#               in the code affected the alignment and appearance of the output.

#               I struggled with figuring out how to properly use the left alignment
#               position in my formatting for step 4.  I had to go back and review the
#               class documentation to better understand how the alignment specifiers worked.
#               It made me feel really good to figure it out.

#               I used the Python formatting options with fast strings to align the output into columns.
#               I reserved 21 character positions for the planet names using :21s, which
#               left-aligns the string and ensures there is enough space for the planet names.
#               I reserved 10 character positions for calculated weights using :10,.2f, which
#               right-aligns the numeric values and formats them to two decimal places.

#               1.  I learned how to use named constants to improve readability in my code by defining
#                   the surface gravity weight of each planet and mapping them to constant names, which
#                   allowed me to reference them by name instead of repeating numeric values throughout
#                   the code.

#               2.  I learned how to convert user input from a string to a float in one step so that I
#                   could perform calculations with the value entered by the user.

#               3.  I learned how to do formatting to align my output and control how the calculated values
#                   are displayed.


#1. Declare Named Constants
MERCURY = .38
VENUS = .91
MOON = .165
MARS = .38
JUPITOR = 2.34
SATURN = .93
URANUS = .92
NEPTUNE = 1.12
PLUTO = .066

#2. Prompt the user for a Name and Earth Weight:
sNameJLV = input("What is your name: ")
fWeightJLV = float(input("What is your weight: "))

#3. Multiply the Earth Weight by each of the planet's Surface Gravity Factor:
fMercuryWtJLV = fWeightJLV * MERCURY
fVenusWtJLV = fWeightJLV * VENUS
fMoonWtJLV = fWeightJLV * MOON
fMarsWtJLV = fWeightJLV * MARS
fJupitorWtJLV = fWeightJLV * JUPITOR
fSaturnWtJLV = fWeightJLV * SATURN
fUranusWtJLV = fWeightJLV * URANUS
fNeptuneWtJLV = fWeightJLV * NEPTUNE
fPlutoWtJLV = fWeightJLV * PLUTO

#4. Output:
print("Moose here are your weights on our Solar System's planets:")
print(f"{'Weight on Mercury:':21s} {fMercuryWtJLV:10,.2f}")
print(f"{'Weight on Venus:':21s} {fVenusWtJLV:10,.2f}")
print(f"{'Weight on our Moon:':21s} {fMoonWtJLV:10,.2f}")
print(f"{'Weight on Mars:':21s} {fMarsWtJLV:10,.2f}")
print(f"{'Weight on Jupitor:':21s} {fJupitorWtJLV:10,.2f}")
print(f"{'Weight on Saturn:':21s} {fSaturnWtJLV:10,.2f}")
print(f"{'Weight on Uranus:':21s} {fUranusWtJLV:10,.2f}")
print(f"{'Weight on Neptune:':21s} {fNeptuneWtJLV:10,.2f}")
print(f"{'Weight on Pluto:':21s} {fPlutoWtJLV:10,.2f}")

