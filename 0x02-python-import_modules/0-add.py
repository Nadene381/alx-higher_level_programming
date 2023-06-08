#!/usr/bin/python3
a = 1
b = 2
if __main_variable__ == "__main__":
    from add_0 import add
get_result = add(a, b)
print("{a} + {b} = {result}".format(a=a, b=b, result=get_result))
