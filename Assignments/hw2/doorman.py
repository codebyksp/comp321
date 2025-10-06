# Read input
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)
X = int(data[0])
s = list(data[1].strip()) if len(data) > 1 else []

diff = 0   # diff = #W - #M
count = 0

while s:
    # Try first person
    first = s[0]
    can_first = False
    if first == 'W':
        can_first = abs(diff + 1) <= X
    else:  # 'M'
        can_first = abs(diff - 1) <= X

    if can_first:
        if first == 'W':
            diff += 1
        else:
            diff -= 1
        s.pop(0)
        count += 1
        continue

    # Try second person if available
    if len(s) >= 2:
        second = s[1]
        can_second = False
        if second == 'W':
            can_second = abs(diff + 1) <= X
        else:
            can_second = abs(diff - 1) <= X

        if can_second:
            if second == 'W':
                diff += 1
            else:
                diff -= 1
            s.pop(1)
            count += 1
            continue

    # Neither first nor second can be admitted without exceeding X
    break

print(count)
