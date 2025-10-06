

import java.util.*;

public class MergeSortVariants {
    
    // ========================================================================
    // 1. STANDARD MERGE SORT - The Template You Should Memorize
    // ========================================================================
    
    /**
     * Standard merge sort implementation.
     * Time: O(n log n), Space: O(n)
     */
    public static void mergeSort(int[] arr) {
        if (arr.length <= 1) return;
        mergeSort(arr, 0, arr.length - 1);
    }
    
    private static void mergeSort(int[] arr, int left, int right) {
        if (left >= right) return; // Base case: 0 or 1 element
        
        int mid = left + (right - left) / 2; // Avoid overflow
        
        // Divide: Sort left and right halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        // Conquer: Merge the sorted halves
        merge(arr, left, mid, right);
    }
    
    private static void merge(int[] arr, int left, int mid, int right) {
        // Create temporary arrays
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int[] L = new int[n1];
        int[] R = new int[n2];
        
        // Copy data to temp arrays
        for (int i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }
        for (int i = 0; i < n2; i++) {
            R[i] = arr[mid + 1 + i];
        }
        
        // Merge the temp arrays back
        int i = 0, j = 0, k = left;
        
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }
        
        // Copy remaining elements
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
    
    // ========================================================================
    // 2. COUNTING INVERSIONS - Classic Interview/Competition Problem
    // ========================================================================
    
    /**
     * Count number of inversions (pairs where i < j but arr[i] > arr[j]).
     * This is a VERY common competitive programming problem!
     * 
     * Example: [2, 4, 1, 3, 5] has 3 inversions: (2,1), (4,1), (4,3)
     */
    public static long countInversions(int[] arr) {
        if (arr.length <= 1) return 0;
        return mergeSortAndCount(arr, 0, arr.length - 1);
    }
    
    private static long mergeSortAndCount(int[] arr, int left, int right) {
        if (left >= right) return 0;
        
        int mid = left + (right - left) / 2;
        
        long invCount = 0;
        
        // Count inversions in left half
        invCount += mergeSortAndCount(arr, left, mid);
        
        // Count inversions in right half
        invCount += mergeSortAndCount(arr, mid + 1, right);
        
        // Count split inversions (left element > right element)
        invCount += mergeAndCount(arr, left, mid, right);
        
        return invCount;
    }
    
    private static long mergeAndCount(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int[] L = new int[n1];
        int[] R = new int[n2];
        
        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];
        
        int i = 0, j = 0, k = left;
        long invCount = 0;
        
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k++] = L[i++];
            } else {
                // KEY DIFFERENCE: When we take from right, ALL remaining
                // elements in left are greater than this right element
                arr[k++] = R[j++];
                invCount += (n1 - i); // All remaining left elements form inversions
            }
        }
        
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
        
        return invCount;
    }
    
    // ========================================================================
    // 3. MERGE K SORTED ARRAYS - Using Merge Sort Concept
    // ========================================================================
    
    /**
     * Merge K sorted arrays into one sorted array.
     * Common in competitive programming and interviews.
     */
    public static int[] mergeKSortedArrays(int[][] arrays) {
        if (arrays.length == 0) return new int[0];
        return mergeKArrays(arrays, 0, arrays.length - 1);
    }
    
    private static int[] mergeKArrays(int[][] arrays, int left, int right) {
        if (left == right) {
            return arrays[left];
        }
        
        if (left + 1 == right) {
            return mergeTwoArrays(arrays[left], arrays[right]);
        }
        
        int mid = left + (right - left) / 2;
        int[] leftMerged = mergeKArrays(arrays, left, mid);
        int[] rightMerged = mergeKArrays(arrays, mid + 1, right);
        
        return mergeTwoArrays(leftMerged, rightMerged);
    }
    
    private static int[] mergeTwoArrays(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;
        
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                result[k++] = a[i++];
            } else {
                result[k++] = b[j++];
            }
        }
        
        while (i < a.length) result[k++] = a[i++];
        while (j < b.length) result[k++] = b[j++];
        
        return result;
    }
    
    // ========================================================================
    // 4. FINDING KTH SMALLEST ELEMENT (Modified Merge Sort)
    // ========================================================================
    
    /**
     * Find kth smallest element using merge sort approach.
     * Not the most efficient (quickselect is better), but shows merge sort variant.
     */
    public static int findKthSmallest(int[] arr, int k) {
        int[] sorted = arr.clone();
        mergeSort(sorted);
        return sorted[k - 1]; // k is 1-indexed
    }
    
    // ========================================================================
    // 5. EXTERNAL MERGE SORT CONCEPT
    // ========================================================================
    
    /**
     * Simulate external merge sort (used when data doesn't fit in memory).
     * Sorts chunks, then merges them.
     */
    public static int[] externalMergeSort(int[] arr, int chunkSize) {
        // Split into chunks
        ArrayList<int[]> chunks = new ArrayList<>();
        for (int i = 0; i < arr.length; i += chunkSize) {
            int end = Math.min(i + chunkSize, arr.length);
            int[] chunk = Arrays.copyOfRange(arr, i, end);
            mergeSort(chunk);
            chunks.add(chunk);
        }
        
        // Merge all chunks
        return mergeKSortedArrays(chunks.toArray(new int[0][]));
    }
    
    // ========================================================================
    // 6. MERGE SORT WITH CUSTOM COMPARATOR
    // ========================================================================
    
    /**
     * Merge sort for objects with custom comparator.
     * Useful when you need stable sorting with custom logic.
     */
    public static <T> void mergeSortGeneric(T[] arr, Comparator<T> comp) {
        if (arr.length <= 1) return;
        mergeSortGeneric(arr, 0, arr.length - 1, comp);
    }
    
    private static <T> void mergeSortGeneric(T[] arr, int left, int right, Comparator<T> comp) {
        if (left >= right) return;
        
        int mid = left + (right - left) / 2;
        mergeSortGeneric(arr, left, mid, comp);
        mergeSortGeneric(arr, mid + 1, right, comp);
        mergeGeneric(arr, left, mid, right, comp);
    }
    
    @SuppressWarnings("unchecked")
    private static <T> void mergeGeneric(T[] arr, int left, int mid, int right, Comparator<T> comp) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        T[] L = (T[]) new Object[n1];
        T[] R = (T[]) new Object[n2];
        
        for (int i = 0; i < n1; i++) L[i] = arr[left + i];
        for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];
        
        int i = 0, j = 0, k = left;
        
        while (i < n1 && j < n2) {
            if (comp.compare(L[i], R[j]) <= 0) {
                arr[k++] = L[i++];
            } else {
                arr[k++] = R[j++];
            }
        }
        
        while (i < n1) arr[k++] = L[i++];
        while (j < n2) arr[k++] = R[j++];
    }
    
    // ========================================================================
    // 7. IN-PLACE MERGE (Space Optimized - Harder to Implement)
    // ========================================================================
    
    /**
     * Merge sort with O(1) extra space (much harder!).
     * Rarely needed but good to know it exists.
     */
    public static void mergeSortInPlace(int[] arr) {
        mergeSortInPlace(arr, 0, arr.length - 1);
    }
    
    private static void mergeSortInPlace(int[] arr, int left, int right) {
        if (left >= right) return;
        
        int mid = left + (right - left) / 2;
        mergeSortInPlace(arr, left, mid);
        mergeSortInPlace(arr, mid + 1, right);
        mergeInPlace(arr, left, mid, right);
    }
    
    private static void mergeInPlace(int[] arr, int left, int mid, int right) {
        int start2 = mid + 1;
        
        // If already sorted
        if (arr[mid] <= arr[start2]) return;
        
        while (left <= mid && start2 <= right) {
            if (arr[left] <= arr[start2]) {
                left++;
            } else {
                int value = arr[start2];
                int index = start2;
                
                // Shift all elements between left and start2 right by 1
                while (index != left) {
                    arr[index] = arr[index - 1];
                    index--;
                }
                arr[left] = value;
                
                left++;
                mid++;
                start2++;
            }
        }
    }
    
    // ========================================================================
    // DEMONSTRATION AND TESTING
    // ========================================================================
    
    public static void main(String[] args) {
        System.out.println("=".repeat(70));
        System.out.println("MERGE SORT VARIANTS FOR COMPETITIVE PROGRAMMING");
        System.out.println("=".repeat(70));
        
        // Test 1: Standard merge sort
        System.out.println("\n1. Standard Merge Sort:");
        int[] arr1 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("   Before: " + Arrays.toString(arr1));
        mergeSort(arr1);
        System.out.println("   After:  " + Arrays.toString(arr1));
        
        // Test 2: Count inversions
        System.out.println("\n2. Counting Inversions:");
        int[] arr2 = {2, 4, 1, 3, 5};
        System.out.println("   Array: " + Arrays.toString(arr2));
        long inversions = countInversions(arr2);
        System.out.println("   Inversions: " + inversions);
        System.out.println("   Sorted: " + Arrays.toString(arr2));
        
        // Test 3: Merge K sorted arrays
        System.out.println("\n3. Merge K Sorted Arrays:");
        int[][] arrays = {
            {1, 5, 9},
            {2, 4, 8},
            {3, 6, 7}
        };
        System.out.println("   Input arrays:");
        for (int[] arr : arrays) {
            System.out.println("      " + Arrays.toString(arr));
        }
        int[] merged = mergeKSortedArrays(arrays);
        System.out.println("   Merged: " + Arrays.toString(merged));
        
        // Test 4: External merge sort simulation
        System.out.println("\n4. External Merge Sort (chunk size = 3):");
        int[] arr4 = {8, 3, 2, 9, 7, 1, 5, 4};
        System.out.println("   Before: " + Arrays.toString(arr4));
        int[] result = externalMergeSort(arr4, 3);
        System.out.println("   After:  " + Arrays.toString(result));
        
        // Test 5: Generic merge sort with comparator
        System.out.println("\n5. Generic Merge Sort (reverse order):");
        Integer[] arr5 = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("   Before: " + Arrays.toString(arr5));
        mergeSortGeneric(arr5, (a, b) -> b - a); // Reverse order
        System.out.println("   After:  " + Arrays.toString(arr5));
        
        System.out.println("\n" + "=".repeat(70));
        System.out.println("KEY TAKEAWAYS:");
        System.out.println("=".repeat(70));
        System.out.println("• Standard merge sort: Memorize this pattern!");
        System.out.println("• Counting inversions: Add counter during merge");
        System.out.println("• Merge K arrays: Apply merge sort recursively");
        System.out.println("• Custom comparator: Easy to adapt for objects");
        System.out.println("• Time complexity: Always O(n log n)");
        System.out.println("• Space complexity: O(n) for standard, O(1) for in-place");
    }
}

// ============================================================================
// QUICK REFERENCE TEMPLATE FOR COMPETITIONS
// ============================================================================

/*

MEMORIZE THIS STANDARD PATTERN:

void mergeSort(int[] arr, int left, int right) {
    if (left >= right) return;
    
    int mid = left + (right - left) / 2;
    
    mergeSort(arr, left, mid);           // Sort left half
    mergeSort(arr, mid + 1, right);      // Sort right half
    merge(arr, left, mid, right);        // Merge sorted halves
}

void merge(int[] arr, int left, int mid, int right) {
    // Create temp arrays
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int[] L = new int[n1];
    int[] R = new int[n2];
    
    // Copy data
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int i = 0; i < n2; i++) R[i] = arr[mid + 1 + i];
    
    // Merge back
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

COMMON MODIFICATIONS:
1. Add counter for inversions
2. Change comparison for custom ordering
3. Track additional info during merge
4. Apply to 2D arrays or objects

*/