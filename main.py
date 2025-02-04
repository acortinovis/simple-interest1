# TASK: Create a program that calculates simple interest.

# Prompt the user to enter the principal amount

amount = float (input ("enter the principal amount ").strip())

# Prompt the user to enter the annual interest rate (in percentage)
perc = float (input ("enter annual interest rate in percentage ").strip())

# Prompt the user to enter the time period in years
time = float (input ("enter time in years ").strip())

# Calculate the simple interest using the formula
interest = (amount * perc * time )/100
# Display the calculated simple interest
print ("your simple interest is ", interest)