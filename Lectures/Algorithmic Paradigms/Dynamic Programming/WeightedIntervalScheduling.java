
import java.util.*;

/**
 * Weighted Interval Scheduling Problem
 * 
 * Problem: Given n activities with start times, finish times, and weights,
 * select a subset of non-overlapping activities that maximizes total weight.
 * 
 * Based on lecture slide recurrence:
 * Case 1: OPT selects activity j
 *   - Add weight w_j
 *   - Cannot use incompatible activities
 *   - Must include optimal solution on remaining compatible activities {1,2,...,p(j)}
 * 
 * Case 2: OPT does not select activity j
 *   - Must include optimal solution on other activities {1,2,...,j-1}
 * 
 * Recurrence: OPT(j) = max(w_j + OPT(p(j)), OPT(j-1))
 * where p(j) = latest activity compatible with j
 */
public class WeightedIntervalScheduling {
    
    // Activity class
    static class Activity implements Comparable<Activity> {
        int id;
        int start;
        int finish;
        int weight;
        
        Activity(int id, int start, int finish, int weight) {
            this.id = id;
            this.start = start;
            this.finish = finish;
            this.weight = weight;
        }
        
        @Override
        public int compareTo(Activity other) {
            return this.finish - other.finish; // Sort by finish time
        }
        
        @Override
        public String toString() {
            return String.format("Activity %d: [%d, %d] weight=%d", 
                               id, start, finish, weight);
        }
    }
    
    Activity[] activities;
    int[] p; // p[j] = latest activity compatible with j
    Integer[] memo; // For memoization
    
    public WeightedIntervalScheduling(Activity[] activities) {
        // Sort activities by finish time (required for algorithm)
        Arrays.sort(activities);
        this.activities = activities;
        this.p = new int[activities.length];
        this.memo = new Integer[activities.length];
        
        // Compute p(j) for each activity
        computeCompatibility();
    }
    
    /**
     * Compute p(j) for each activity j.
     * p(j) = index of latest activity that finishes before j starts.
     * Returns -1 if no such activity exists.
     */
    private void computeCompatibility() {
        for (int j = 0; j < activities.length; j++) {
            p[j] = -1; // Default: no compatible activity
            
            // Find latest activity i where finish[i] <= start[j]
            for (int i = j - 1; i >= 0; i--) {
                if (activities[i].finish <= activities[j].start) {
                    p[j] = i;
                    break; // Found latest compatible activity
                }
            }
        }
    }
    
    // ========================================================================
    // SOLUTION 1: Recursive (matches lecture slide exactly)
    // ========================================================================
    
    /**
     * Recursive solution following the recurrence from lecture.
     * 
     * OPT(j) = max(w_j + OPT(p(j)), OPT(j-1))
     * 
     * Time: O(2^n) - exponential without memoization
     */
    public int solveRecursive(int j) {
        // Base case: no activities to consider
        if (j < 0) return 0;
        
        // ═══════════════════════════════════════════════════════════
        // Case 1: OPT selects activity j
        // ═══════════════════════════════════════════════════════════
        int includeJ = activities[j].weight + solveRecursive(p[j]);
        
        // ═══════════════════════════════════════════════════════════
        // Case 2: OPT does not select activity j
        // ═══════════════════════════════════════════════════════════
        int excludeJ = solveRecursive(j - 1);
        
        // Return maximum of two cases
        return Math.max(includeJ, excludeJ);
    }
    
    // ========================================================================
    // SOLUTION 2: Memoized Recursion (Top-Down DP)
    // ========================================================================
    
    /**
     * Memoized recursive solution.
     * Time: O(n^2) for computing p(j), then O(n) for DP
     * Space: O(n)
     */
    public int solveMemoized(int j) {
        // Base case
        if (j < 0) return 0;
        
        // Check if already computed
        if (memo[j] != null) {
            return memo[j];
        }
        
        // Case 1: Include activity j
        int includeJ = activities[j].weight + solveMemoized(p[j]);
        
        // Case 2: Exclude activity j
        int excludeJ = solveMemoized(j - 1);
        
        // Store and return result
        memo[j] = Math.max(includeJ, excludeJ);
        return memo[j];
    }
    
    // ========================================================================
    // SOLUTION 3: Bottom-Up DP (Iterative)
    // ========================================================================
    
    /**
     * Bottom-up dynamic programming solution.
     * Time: O(n^2) for computing p(j), then O(n) for DP
     * Space: O(n)
     */
    public int solveBottomUp() {
        int n = activities.length;
        int[] dp = new int[n + 1]; // dp[j] = OPT(j-1) in 0-indexed
        
        dp[0] = 0; // Base case: no activities
        
        for (int j = 1; j <= n; j++) {
            int activityIndex = j - 1; // Convert to 0-indexed
            
            // Case 1: Include activity j
            int pIndex = p[activityIndex]; // Latest compatible activity
            int includeJ = activities[activityIndex].weight;
            if (pIndex >= 0) {
                includeJ += dp[pIndex + 1];
            }
            
            // Case 2: Exclude activity j
            int excludeJ = dp[j - 1];
            
            dp[j] = Math.max(includeJ, excludeJ);
        }
        
        return dp[n];
    }
    
    // ========================================================================
    // SOLUTION 4: Bottom-Up DP with Solution Reconstruction
    // ========================================================================
    
    /**
     * Bottom-up DP that also returns which activities were selected.
     */
    public Result solveWithReconstruction() {
        int n = activities.length;
        int[] dp = new int[n + 1];
        
        dp[0] = 0;
        
        for (int j = 1; j <= n; j++) {
            int activityIndex = j - 1;
            
            int pIndex = p[activityIndex];
            int includeJ = activities[activityIndex].weight;
            if (pIndex >= 0) {
                includeJ += dp[pIndex + 1];
            }
            
            int excludeJ = dp[j - 1];
            
            dp[j] = Math.max(includeJ, excludeJ);
        }
        
        // Reconstruct solution
        ArrayList<Activity> selected = new ArrayList<>();
        int j = n;
        
        while (j > 0) {
            int activityIndex = j - 1;
            
            int pIndex = p[activityIndex];
            int includeJ = activities[activityIndex].weight;
            if (pIndex >= 0) {
                includeJ += dp[pIndex + 1];
            }
            
            int excludeJ = dp[j - 1];
            
            if (includeJ >= excludeJ) {
                // Activity j was included in optimal solution
                selected.add(activities[activityIndex]);
                j = pIndex + 1; // Jump to p(j)
            } else {
                // Activity j was not included
                j = j - 1;
            }
        }
        
        Collections.reverse(selected); // Reverse to get chronological order
        return new Result(dp[n], selected);
    }
    
    // Result class to hold weight and selected activities
    static class Result {
        int maxWeight;
        ArrayList<Activity> selected;
        
        Result(int maxWeight, ArrayList<Activity> selected) {
            this.maxWeight = maxWeight;
            this.selected = selected;
        }
    }
    
    // ========================================================================
    // HELPER: Print compatibility array p(j)
    // ========================================================================
    
    public void printCompatibility() {
        System.out.println("\nCompatibility Array p(j):");
        System.out.println("(p(j) = latest activity compatible with j)");
        for (int j = 0; j < activities.length; j++) {
            if (p[j] >= 0) {
                System.out.printf("p(%d) = %d  (Activity %d compatible with Activity %d)\n", 
                                j, p[j], j, p[j]);
            } else {
                System.out.printf("p(%d) = -1 (No compatible activities)\n", j);
            }
        }
    }
    
    // ========================================================================
    // DEMONSTRATION
    // ========================================================================
    
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("WEIGHTED INTERVAL SCHEDULING");
        System.out.println("=".repeat(70));
        
        // Example from textbook/lecture
        Activity[] activities = {
            new Activity(1, 0, 6, 60),
            new Activity(2, 1, 4, 50),
            new Activity(3, 5, 7, 30),
            new Activity(4, 3, 5, 20),
            new Activity(5, 3, 9, 70),
            new Activity(6, 5, 9, 40),
            new Activity(7, 6, 10, 30),
            new Activity(8, 8, 11, 20)
        };
        
        System.out.println("\nInput Activities:");
        for (Activity a : activities) {
            System.out.println("  " + a);
        }
        
        WeightedIntervalScheduling scheduler = new WeightedIntervalScheduling(activities);
        
        // Print sorted activities
        System.out.println("\nActivities sorted by finish time:");
        for (int i = 0; i < scheduler.activities.length; i++) {
            System.out.printf("  [%d] %s\n", i, scheduler.activities[i]);
        }
        
        // Print compatibility
        scheduler.printCompatibility();
        
        // Solution 1: Recursive (only for small inputs!)
        System.out.println("\n" + "=".repeat(70));
        System.out.println("SOLUTION 1: Recursive (Exponential Time)");
        System.out.println("=".repeat(70));
        int result1 = scheduler.solveRecursive(scheduler.activities.length - 1);
        System.out.println("Maximum weight: " + result1);
        System.out.println("Note: This is very slow for large n!");
        
        // Solution 2: Memoized
        System.out.println("\n" + "=".repeat(70));
        System.out.println("SOLUTION 2: Memoized Recursion (Top-Down DP)");
        System.out.println("=".repeat(70));
        int result2 = scheduler.solveMemoized(scheduler.activities.length - 1);
        System.out.println("Maximum weight: " + result2);
        
        // Solution 3: Bottom-up
        System.out.println("\n" + "=".repeat(70));
        System.out.println("SOLUTION 3: Bottom-Up DP (Iterative)");
        System.out.println("=".repeat(70));
        int result3 = scheduler.solveBottomUp();
        System.out.println("Maximum weight: " + result3);
        
        // Solution 4: With reconstruction
        System.out.println("\n" + "=".repeat(70));
        System.out.println("SOLUTION 4: Bottom-Up DP with Solution Reconstruction");
        System.out.println("=".repeat(70));
        Result result4 = scheduler.solveWithReconstruction();
        System.out.println("Maximum weight: " + result4.maxWeight);
        System.out.println("\nSelected activities:");
        for (Activity a : result4.selected) {
            System.out.println("  " + a);
        }
        
        System.out.println("\n" + "=".repeat(70));
        System.out.println("KEY CONCEPTS:");
        System.out.println("=".repeat(70));
        System.out.println("• Recurrence: OPT(j) = max(w_j + OPT(p(j)), OPT(j-1))");
        System.out.println("• Case 1: Include activity j → add weight, solve on compatible");
        System.out.println("• Case 2: Exclude activity j → solve on remaining activities");
        System.out.println("• p(j) = latest activity that doesn't overlap with j");
        System.out.println("• Time: O(n log n) sort + O(n²) compute p + O(n) DP = O(n²)");
        System.out.println("• Can optimize p(j) computation to O(n log n) with binary search");
    }
}

/*
=============================================================================
QUICK REFERENCE: The Recurrence from Lecture
=============================================================================

Step 2.1: What decision do I make at every step?

Case 1: OPT selects activity j
  • Add weight w_j
  • Cannot use incompatible activities
  • Must include optimal solution on remaining compatible activities {1,2,...,p(j)}
  
  → OPT(j) includes w_j + OPT(p(j))

Case 2: OPT does not select activity j
  • Must include optimal solution on other activities {1,2,...,j-1}
  
  → OPT(j) = OPT(j-1)

Final Recurrence:
  OPT(j) = max(w_j + OPT(p(j)), OPT(j-1))

Base Case:
  OPT(-1) = 0 (no activities to select)

=============================================================================
*/