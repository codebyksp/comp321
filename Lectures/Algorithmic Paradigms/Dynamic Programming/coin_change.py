def count_recur(coins, n, s, memo):
    # Base cases
    if s == 0:
        return 1
    if s < 0 or n == 0:
        return 0

    # Check memo (if already computed)
    if memo[n][s] != -1:
        return memo[n][s]

    # include the nth coin (coins[n-1]) or exclude it
    include = count_recur(coins, n, s - coins[n - 1], memo)
    exclude = count_recur(coins, n - 1, s, memo)

    memo[n][s] = include + exclude
    return memo[n][s]


def count_ways(coins, amount):
    n = len(coins)
    # memo dimensions: (n+1) x (amount+1), indexed by [0..n][0..amount]
    memo = [[-1] * (amount + 1) for _ in range(n + 1)]
    ways = count_recur(coins, n, amount, memo)
    return ways, memo


if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 6
    ways, memo = count_ways(coins, amount)
    print(f"Number of ways to make {amount}:", ways)

    # Optional: pretty-print the memo table rows for n=0..len(coins)
    print("\nMemo table (rows = n coins allowed, cols = sum 0..amount):")
    for i, row in enumerate(memo):
        print(f"n={i}:", row)



#iterative 

def count_ways_bottom_up_2d(coins, amount):
    n = len(coins)
    # dp dimensions: (n+1) x (amount+1)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]

    # base: one way to make sum 0 with any number of coins
    for i in range(n + 1):
        dp[i][0] = 1

    # fill table
    for i in range(1, n + 1):           # using first i coins
        coin = coins[i - 1]
        for s in range(0, amount + 1):
            # exclude coin i
            dp[i][s] = dp[i - 1][s]
            # include coin i (can reuse, so we look at dp[i][s - coin])
            if s - coin >= 0:
                dp[i][s] += dp[i][s - coin]

    return dp[n][amount], dp  # return answer and full table if you want to inspect it


if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 6
    ways, dp_table = count_ways_bottom_up_2d(coins, amount)
    print("Ways:", ways)
    print("\nDP table (rows i=0..n, cols s=0..amount):")
    for i, row in enumerate(dp_table):
        print(f"i={i}:", row)
