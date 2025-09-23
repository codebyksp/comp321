import sys; input = sys.stdin.readline

N = int(input()); print(N)
a, b, c = map(int, input().split()); print(a, b, c)
for _ in range(N):
    p, q, r, s = map(int, input().split());
    print(p, q, r, s)
# with this: ~0.36s
# without this: ~0.23s
for _ in range(N):
    x, y = input().strip().split()
    print(x, y)

input = sys.stdin.readline   # faster input
print = sys.stdout.write     # faster output

N = int(input())  
print(str(N) + '\n')         # must manually add '\n'

a, b, c = map(int, input().split())  
print(f'{a} {b} {c}\n')      # formatted output with newline

#💡 You could write the same thing without an f-string like: print(str(a) + " " + str(b) + " " + str(c) + "\n")


for _ in range(N):
    p, q, r, s = map(int, input().split())
    print(f'{p}{q}{r} {s}\n')   # notice they forgot a space between p,q,r here
                                # probably a bug

# performance test
for _ in range(N):
    x, y = input().strip().split()
    print(x + ' ' + y + '\n')   # manually add newline
