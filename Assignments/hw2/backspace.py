s = input().strip()  # read the input string
result = []

for ch in s:
    if ch == '<':
        if result:      # only remove if there is something to remove
            result.pop()
    else:
        result.append(ch)

print(''.join(result))
