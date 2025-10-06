# permutation_encryption.py
import sys

def encrypt_blockwise(key, msg):
    n = len(key)
    # pad with spaces
    if len(msg) % n != 0:
        msg += ' ' * (n - (len(msg) % n))
    out_chars = []
    for i in range(0, len(msg), n):
        block = msg[i:i+n]
        for k in key:
            out_chars.append(block[k-1])
    return ''.join(out_chars)

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        n = int(parts[0])
        if n == 0:
            break
        key = list(map(int, parts[1:1+n]))
        # read the message line (keep trailing spaces — remove only newline)
        msg = sys.stdin.readline().rstrip('\n')
        encrypted = encrypt_blockwise(key, msg)
        print(f"'{encrypted}'")

if __name__ == "__main__":
    main()
