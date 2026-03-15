import os
import math
print("Current working directory:", os.getcwd())
num= int(input("Enter an integer: "))
log_val = math.log2(num)
print(f"log base 2 of {num} is: {log_val}")
print(f"floor:", math.floor(log_val))
print(f"ceiling:", math.ceil(log_val))