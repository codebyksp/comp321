import sys

def solve():
    inp = sys.stdin
    case_num = 0
    while True:
        line = inp.readline()
        if not line:
            break
        n = int(line.strip())
        if n == 0:
            break
        case_num += 1
        pile1 = 0  # number of plates in pile 1
        pile2 = 0  # number of plates in pile 2

        outputs = []
        for _ in range(n):
            cmd, m_str = inp.readline().split()
            m = int(m_str)

            if cmd == "DROP":
                # always drop into pile 2
                pile2 += m
                outputs.append(f"DROP 2 {m}")

            elif cmd == "TAKE":
                to_take = m
                # take from pile1 first
                while to_take > 0:
                    if pile1 == 0:
                        # refill pile1 from pile2
                        outputs.append(f"MOVE 2->1 {pile2}")
                        pile1 += pile2
                        pile2 = 0
                    take_now = min(to_take, pile1)
                    outputs.append(f"TAKE 1 {take_now}")
                    pile1 -= take_now
                    to_take -= take_now

        print("\n".join(outputs))
        print()  # blank line between cases

if __name__ == "__main__":
    solve()
