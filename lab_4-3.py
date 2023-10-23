# Author: caleb moura

# Prompt user to input both strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Compare strings using conditional statements with greater than and less than values
if string1 == string2:
    print(f"The strings '{string1}' and '{string2}' are equal.")
elif string1 > string2:
    print(f"The string '{string1}' is greater than '{string2}'.")
else:
    print(f"The string '{string1}' is less than '{string2}'.")