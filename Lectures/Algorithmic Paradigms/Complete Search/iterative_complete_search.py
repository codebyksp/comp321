import itertools
import time

def has_all_unique_digits(num1, num2):
    """Check if two numbers together use all digits 0-9 exactly once."""
    # Pad numbers to 5 digits each
    s1 = str(num1).zfill(5)
    s2 = str(num2).zfill(5)
    combined = s1 + s2
    
    # Check if we have exactly 10 digits and all are unique
    if len(combined) != 10:
        return False
    
    # Check if all digits 0-9 are present
    return sorted(combined) == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution1_naive():
    """
    Naive solution: Generate all permutations of digits 0-9.
    Time complexity: O(10!) = ~3.6 million permutations
    """
    print("=== Solution 1: Naive (Permutation) ===")
    start_time = time.time()
    
    results = []
    count = 0
    
    # Generate all permutations of digits 0-9
    for perm in itertools.permutations('0123456789'):
        count += 1
        # Split into two 5-digit numbers
        num1 = int(''.join(perm[:5]))
        num2 = int(''.join(perm[5:]))
        
        # Check if num2 divides num1 evenly
        if num2 != 0 and num1 % num2 == 0:
            n = num1 // num2
            # Check if N is in valid range
            if 2 <= n <= 79:
                results.append((num1, num2, n))
    
    elapsed = time.time() - start_time
    
    print(f"Permutations checked: {count:,}")
    print(f"Solutions found: {len(results)}")
    print(f"Time: {elapsed:.3f} seconds")
    print(f"\nFirst 10 solutions:")
    for num1, num2, n in sorted(results)[:10]:
        print(f"  {num1:05d} / {num2:05d} = {n}")
    
    return results

def solution2_optimized():
    """
    Optimized solution: Iterate through divisors and calculate dividend.
    Time complexity: ~50K divisors × ~80 values of N = ~500K operations
    
    Key optimization: For each N, only check divisors where divisor * N <= 99999
    This means as N grows, we check fewer divisors!
    """
    print("\n=== Solution 2: Optimized (Calculate Dividend) ===")
    start_time = time.time()
    
    results = []
    checks = 0
    
    # For each N value
    for n in range(2, 80):  # 2 to 79
        # Calculate max divisor for this N (so dividend doesn't exceed 99999)
        max_divisor = min(98765, 99999 // n)
        
        # Iterate through valid divisors for this N
        for divisor in range(1234, max_divisor + 1):
            checks += 1
            
            # Calculate what the dividend must be
            dividend = divisor * n
            
            # Check if all 10 digits are unique
            if has_all_unique_digits(dividend, divisor):
                results.append((dividend, divisor, n))
    
    elapsed = time.time() - start_time
    
    print(f"Combinations checked: {checks:,}")
    print(f"Solutions found: {len(results)}")
    print(f"Time: {elapsed:.3f} seconds")
    print(f"\nFirst 10 solutions:")
    for dividend, divisor, n in sorted(results)[:10]:
        print(f"  {dividend:05d} / {divisor:05d} = {n}")
    
    return results

def verify_solutions(results1, results2):
    """Verify both solutions found the same results."""
    print("\n=== Verification ===")
    set1 = set(results1)
    set2 = set(results2)
    
    if set1 == set2:
        print(f"✓ Both solutions found identical {len(set1)} results!")
    else:
        print(f"✗ Solutions differ!")
        print(f"  Solution 1 found: {len(set1)}")
        print(f"  Solution 2 found: {len(set2)}")
        print(f"  Only in Solution 1: {len(set1 - set2)}")
        print(f"  Only in Solution 2: {len(set2 - set1)}")

# Run both solutions
if __name__ == "__main__":
    # Run optimized solution first (faster)
    results2 = solution2_optimized()
    
    # Run naive solution (slower)
    print("\n" + "="*50)
    results1 = solution1_naive()
    
    # Verify they match
    print("\n" + "="*50)
    verify_solutions(results1, results2)
    
    # Show speedup
    print(f"\n=== Performance Comparison ===")
    print(f"Solution 2 is much faster due to:")
    print(f"  • Calculating dividend instead of trying all permutations")
    print(f"  • Early termination when dividend exceeds 99999")
    print(f"  • Only ~500K checks vs ~3.6M permutations")