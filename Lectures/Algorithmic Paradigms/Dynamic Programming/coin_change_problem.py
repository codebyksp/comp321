def count(coins, n, current_sum, amount, memo):
    # Check memo first
    if (n, current_sum) in memo:
        return memo[(n, current_sum)]

    # Base cases
    if current_sum == amount:
        return 1
    if current_sum > amount or n < 0:
        return 0

    # Include current coin
    include = count(coins, n, current_sum + coins[n], amount, memo)

    # Exclude current coin
    exclude = count(coins, n - 1, current_sum, amount, memo)

    # Save result in memo before returning
    memo[(n, current_sum)] = include + exclude
    return memo[(n, current_sum)]


if __name__ == "__main__":
    amount = 6
    coins = [1, 5, 10, 25]
    memo = {}
    ways = count(coins, len(coins) - 1, 0, amount, memo)
    print(f"Number of ways to make {amount}:", ways)
