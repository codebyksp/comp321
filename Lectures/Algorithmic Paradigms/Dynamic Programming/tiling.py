from functools import lru_cache

@lru_cache(maxsize=None)
def A(n):
    """Number of ways to tile 3 x n with one corner removed."""
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    # recurrence: A(n) = D(n-1) + A(n-2)
    return D(n - 1) + A(n - 2)

@lru_cache(maxsize=None)
def D(n):
    """Number of ways to tile 3 x n completely."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 0
    # recurrence: D(n) = D(n-2) + 2 * A(n-1)
    return D(n - 2) + 2 * A(n - 1)

def tile_3xn_recursive(n):
    """Public wrapper: returns number of tilings for 3 x n."""
    return D(n)

if __name__ == "__main__":
    for n in range(0, 13):
        print(f"n={n:2d} -> ways = {tile_3xn_recursive(n)}")
