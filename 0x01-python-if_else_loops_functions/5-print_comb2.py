#!/usr/bin/python3
output_text = ""
for n in range(100):
    output_text += "{:02d}".format(n)
    if n != 99:
        output_text += ', '
print(output_text)
