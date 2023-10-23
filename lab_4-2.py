# Author: caleb moura

# Variable called school, and set equal to "Fairfield Prep"
school = "Fairfield Prep"

# Statement that splits "Fairfield" and stores it as first_half
# Similar statement that splits " Prep" and stores it as second_half
first_half = school.split(" ")[0]
second_half = school.split(" ")[1]

# Each half printed on its own line
print(first_half)
print(second_half)

# Two halves joined together with concatenation and printed
full_name = first_half + second_half
print(full_name)