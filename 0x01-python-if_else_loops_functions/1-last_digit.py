#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_last_val = abs(number) % 10 * (-1 if number < 0 else 1)
output_message = f"Last digit of {number} is {number_last_val}"
if number_last_val == 0:
    output_message += " and is 0"
elif number_last_val > 5:
    output_message += " and is greater than 5"
else:
    output_message += f" and is less than 6 and not 0"
print(output_message)
