import os
import math
cwd = os.getcwd()
print("Current working directory:", cwd)
num = int(input("Enter a number: "))
log_val = math.log2(num)
print(f"The logarithm 2 of {num} is: {log_val}")
print("floor:", math.floor(log_val))
print("ceiling:", math.ceil(log_val))