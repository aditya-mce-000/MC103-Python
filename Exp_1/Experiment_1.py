# Write a program to create variables of numeric Data Types and perform Arithmetic Operations on them in Python. 

print("Program 1: Arithmetic Operations, Aditya Raj, 26/B04/019") # Experiment Name, Name and Roll No.

num_1 = int(input("Enter 1st no. : "))  # Prompt for 1st number and store in num_1 variable
num_2 = int(input("Enter 2nd no. : "))  # Prompt for 2nd number and store in num_2 variable

sum = num_1 + num_2             # Add numbers and store in the variable
Difference = num_1 - num_2      # Subtract numbers and store in the variable
Product = num_1 * num_2         # Multiply numbers and store in the variable
Power = num_1 ** num_2          # Power num_2 to the number num_1 and store in the variable
Mod = num_1 % num_2             # Remainder when num_1 os divided by num_2 and store in the variable
Division = num_1 / num_2        # Divsion Result(Float) when num_1 is divided by num_2  and store in the variable

print("Sum of",num_1,"and", num_2, "is ", sum)                    # Print Sum of two numbers

print("Difference of",num_1,"and", num_2, "is ", Difference)      # Print Difference of two numbers

print("Product of",num_1,"and", num_2, "is ", Product)            # Print Product of two numbers

print("Power of",num_1,"and", num_2, "is ", Power)                # Print Power num_2 to the number num_1 

print("Mod of",num_1,"and", num_2, "is ", Mod)                    # Print Modulus or Remainder when num_1 is divided by num_2

print("Division of",num_1,"and", num_2, "is ", Division)          # Print Divsion of two numbers

Answer = (num_1 ** 3) * (num_2 ** 7)  # Class Assignment
print(Answer)                         # Print Answer