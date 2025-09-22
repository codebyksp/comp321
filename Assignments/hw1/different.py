import sys

for line in sys.stdin.readlines():
    x, y = list(map(int, line.split()))
    print(abs(x-y))

