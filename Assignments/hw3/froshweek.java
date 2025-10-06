package Assignments.hw3;

import java.util.*;

public class froshweek {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();   // number of students
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }

        long inversions = countInversions(arr);
        System.out.println(inversions);

        sc.close();
    }

    public static long countInversions(long[] arr) {
        long[] temp = new long[arr.length];
        return mergeSortAndCount(arr, temp, 0, arr.length - 1);
    }

    private static long mergeSortAndCount(long[] arr, long[] temp, int left, int right) {
        long invCount = 0;
        if (left < right) {
            int mid = (left + right) / 2;

            invCount += mergeSortAndCount(arr, temp, left, mid);
            invCount += mergeSortAndCount(arr, temp, mid + 1, right);
            invCount += mergeAndCount(arr, temp, left, mid, right);
        }
        return invCount;
    }

    private static long mergeAndCount(long[] arr, long[] temp, int left, int mid, int right) {
        int i = left;     // index for left subarray
        int j = mid + 1;  // index for right subarray
        int k = left;     // index for merged array
        long invCount = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                invCount += (mid - i + 1); // count inversions
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (i = left; i <= right; i++) {
            arr[i] = temp[i];
        }

        return invCount;
    }
}
