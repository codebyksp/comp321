import sys

# Allow arbitrarily large integers from input
sys.set_int_max_str_digits(0)

a = int(input().strip())
b = int(input().strip())

print(a + b)
