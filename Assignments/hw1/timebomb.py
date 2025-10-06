import sys

# I need to write a program that takes ascii numbers and outputs 
# BEER!! if the number is divisible by 6 and BOOM!! otherwise

# Canonical 3x5 patterns for digits 0..9 taken from the problem statement.
DIGIT_ROWS = [
    "***   * *** *** * * *** *** *** *** ***",
    "* *   *   *   * * * *   *     * * * * *",
    "* *   * *** *** *** *** ***   * *** ***",
    "* *   * *     *   *   * * *   * * *   *",
    "***   * *** ***   * *** ***   * *** ***"
]

# Build mapping pattern -> digit
digit_map = {}
for d in range(10):
    start = d * 4
    pattern = tuple(row[start:start+3] for row in DIGIT_ROWS)
    digit_map[pattern] = d

def process_block(block_lines):
    """
    block_lines: list of 5 strings (each includes spaces and '*' exactly as in input)
    returns "BEER!!" or "BOOM!!"
    """
    # Determine number of digits from width: width = 4*n - 1  =>  n = (width + 1) // 4
    width = len(block_lines[0])
    if any(len(r) != width for r in block_lines):
        # Malformed input (unequal widths) -> invalid
        return "BOOM!!"
    if (width + 1) % 4 != 0:
        return "BOOM!!"
    n = (width + 1) // 4
    digits = []
    for j in range(n):
        start = j * 4
        pattern = tuple(line[start:start+3] for line in block_lines)
        if pattern not in digit_map:
            return "BOOM!!"
        digits.append(digit_map[pattern])

    # Check divisible by 6: divisible by 2 (even) and by 3 (sum of digits % 3 == 0)
    if digits[-1] % 2 != 0:
        return "BOOM!!"
    if sum(digits) % 3 != 0:
        return "BOOM!!"
    # numeric value is positive by problem statement if representation valid
    return "BEER!!"

def main():
    raw_lines = sys.stdin.read().splitlines()
    # Remove completely empty lines (they are not part of blocks); keep lines that may contain spaces
    lines = [ln for ln in raw_lines if ln != ""]
    if not lines:
        return

    outputs = []
    i = 0
    while i + 4 < len(lines):
        block = lines[i:i+5]
        outputs.append(process_block(block))
        i += 5
    # If there are leftover lines not forming a full 5-line block, treat as invalid
    if i < len(lines):
        outputs.append("BOOM!!")

    print("\n".join(outputs))

if __name__ == "__main__":
    main()


