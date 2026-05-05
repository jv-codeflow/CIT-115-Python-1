# Name: Jasmine Lee Vazquez
# Assignment:   Temp Converter
# Reflection:   I really enjoyed this assignment because the use of if, elif, else statements felt very similar to
#               the logic I have used in my work. I have configured workflow routing rules, letter configuration logic,
#               some SQL querying, and other reporting tools. I also have a lot of experience in process mapping, including
#               swim lane diagrams, which helped me understand the decision structure and flow of the code, as well as
#               the use of and, or, and not statements. Because of this experience, the assignment felt intuitive and
#               helped reinforce concepts I already use in a different way.
#
#               I don't really feel I struggled too much on this assignment. My first iteration of the code worked but
#               did have some redundancy. As I continued to revise and reorganize my conditions, I found that small
#               changes would impact other parts of the logic, which required me to think more carefully about structure
#               and flow. Through this process, I was able to see my code evolve into a cleaner and more efficient
#               version. By revisiting and improving my work, it helped me to better understand how to organize
#               conditional statements and reduce unnecessary repetition. Recognizing the improvements on my own helped
#               me build confidence.
#
#               An if/else statement is used when there are only two possible outcomes.
#               An if/elif/else statement is used when there are multiple conditions to evaluate. Each condition is
#               checked in the order written in the code and once a true condition is found it follows that path,
#               the rest is skipped. For my code, I used if/elif/else because I needed to evaluate multiple conditions
#               and build different logic paths for Fahrenheit vs Celsius.

#               Three things I learned on this assignment:
#               1. I learned how to correctly use and, or, and not when building conditional statements
#               2. I learned how if, and elif statements are evaluated in order and that the code stops once a
#                  true condition is found.
#               3. I learned the importance of structuring logic clearly and testing different scenarios to ensure the
#                  code behaves as expected.


# Prompt User for Input
print("Jasmine's Temp Converter: ")
fTemperatureJLV = float(input("Enter a temperature: "))
sMeasureJLV = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()

# Validate Input: ensure measurement is F or C
# Process Fahrenheit Input: validate max temperature and convert to Celsius
if sMeasureJLV == 'F':
    if fTemperatureJLV > 212:
        print("Temp cannot be > 212")
    else:
        fCelsiusJLV = (5.0 / 9) * (fTemperatureJLV - 32)
        print(f"The Celsius equivalent is {fCelsiusJLV:.1f}")
# Process Celsius Input: validate max temperature and convert to Fahrenheit
elif sMeasureJLV == 'C':
    if fTemperatureJLV > 100:
        print("Temp cannot be > 100")
    else:
        fFahrenheitJLV = ((9.0 / 5.0) * fTemperatureJLV + 32)
        print(f"The Fahrenheit equivalent is {fFahrenheitJLV:.1f}")
else:
    print("You must enter a F or C!")
