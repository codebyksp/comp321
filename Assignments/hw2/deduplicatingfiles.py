import sys
from collections import Counter, defaultdict

def file_hash(s: str) -> int:
    h = 0
    for ch in s:
        h ^= ord(ch)
    return h

def c2(x: int) -> int:
    return x * (x - 1) // 2

def main():
    inp = sys.stdin
    while True:
        header = inp.readline()
        if not header:
            break
        n = int(header.strip())
        if n == 0:
            break

        files = []
        for _ in range(n):
            # remove only newline/CR — preserve all spaces and periods
            s = inp.readline().rstrip('\r\n')
            files.append(s)

        unique_count = len(set(files))

        # buckets: hash -> Counter(mapping file_string -> count)
        buckets = defaultdict(Counter)
        for s in files:
            buckets[file_hash(s)][s] += 1

        collisions = 0
        for counter in buckets.values():
            k = sum(counter.values())          # total files with this hash
            collisions += c2(k)                # all same-hash pairs
            # subtract pairs that are identical files (should not be collisions)
            for m in counter.values():
                collisions -= c2(m)

        print(unique_count, collisions)

if __name__ == "__main__":
    main()
