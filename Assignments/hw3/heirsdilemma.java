package Assignments.hw3;

import java.util.*;

public class heirsdilemma {
    // check if a number meets all conditions
    static boolean check(int n) {
        String ns = Integer.toString(n);
        Set<Character> seen = new HashSet<>();

        for (char ch : ns.toCharArray()) {
            if (ch == '0') return false;  // no zeros allowed
            if (seen.contains(ch)) return false; // no repeats
            seen.add(ch);

            int digit = ch - '0';
            if (n % digit != 0) return false; // must divide evenly
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // read input range
        int low = sc.nextInt();
        int high = sc.nextInt();
        int count = 0;

        // check each number in range
        for (int i = low; i <= high; i++) {
            if (check(i)) count++;
        }

        System.out.println(count);
        sc.close();
    }
}
