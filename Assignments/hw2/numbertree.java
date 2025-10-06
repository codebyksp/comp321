package Assignments.hw2;

import java.util.Scanner;


public class numbertree {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        String path = sc.hasNext() ? sc.next() : "";
        sc.close();

        // total nodes in a perfect binary tree of height h
        long N = (1L << (h + 1)) - 1;  // exact and safe up to h=30

        long index = 1; // 1-based heap index for the root
        for (char c : path.toCharArray()) {
            if (c == 'L') index = index * 2;
            else if (c == 'R') index = index * 2 + 1;
        }

        long label = N - index + 1;
        System.out.println(label);
    }
}

/*
2^4-1 = 15 
2^(h+1)-1 = n

Assuming a 1-based indexing scheme (root at index 1):
Left Child: The left child of a node at index i is located at 2*i.
Right Child: The right child of a node at index i is located at 2*i + 1.
2*1 = 2
2*1 + 1 = 3 
2*2 = 4
2*2 + 1 = 5
2*3 = 6
2*3 + 1 = 7

Now, root is n and indexing is done bottom up from right to left 
left child label: N-2*i + 1 
right child label: N-2*i + 1 + 1 
*/
