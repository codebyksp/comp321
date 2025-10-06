import sys
sys.setrecursionlimit(10000)
from functools import lru_cache

INF = 10**15

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    N = next(it)
    fees = [0] + [next(it) for _ in range(N)]  # fees[1..N]

    @lru_cache(None)
    def dfs(pos, jump):
        """
        Minimum *additional* cost to reach N from (pos, jump),
        assuming the entry fee for 'pos' has already been paid.
        """
        if pos == N:
            return 0
        best = INF

        # forward: length = jump + 1
        fpos = pos + (jump + 1)
        if fpos <= N:
            best = min(best, fees[fpos] + dfs(fpos, jump + 1))

        # backward: length = jump (only if jump > 0)
        bpos = pos - jump
        if jump > 0 and bpos >= 1:
            best = min(best, fees[bpos] + dfs(bpos, jump))

        return best

    # Important: starting on square 1 does NOT count as "entering" it,
    # so we do NOT pay fees[1] initially.
    # The *first required* move is 1 -> 2 with jump length 1, so we pay fee[2],
    # then continue from state (2,1) assuming fee[2] already paid.
    total_cost = fees[2] + dfs(2, 1)
    print(total_cost)

if __name__ == "__main__":
    solve()
