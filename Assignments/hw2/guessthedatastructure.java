package Assignments.hw2;

import java.util.Scanner;
import java.util.Stack;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class guessthedatastructure {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()) {
            String line = sc.nextLine();
            int n = Integer.parseInt(line);
            Stack<Integer> stack = new Stack<>();
            Queue<Integer> queue = new LinkedList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
            boolean isStack = true;
            boolean isQueue = true;
            boolean isPQ = true;

            for (int i = 0; i < n; i++){
                String command = sc.nextLine();
                String[] parts = command.split(" ");
                int operation = Integer.parseInt(parts[0]);
                int value = Integer.parseInt(parts[1]);

                
                if (operation == 1) {
                    stack.push(value);
                    queue.add(value);
                    pq.add(value);
                } else if (operation == 2) {
                    // Stack check
                    if (stack.isEmpty() || stack.pop() != value) isStack = false;
                    
                    // Queue check
                    if (queue.isEmpty() || queue.remove() != value) isQueue = false;
                    
                    // Priority Queue check
                    if (pq.isEmpty() || pq.poll() != value) isPQ = false;
                }

            }

            int count = 0;
            if (isStack) count++;
            if (isQueue) count++;       
            if (isPQ) count++;

            if (count == 0) System.out.println("impossible");
            else if (count > 1) System.out.println("not sure");
            else {
                if (isStack) System.out.println("stack");
                else if (isQueue) System.out.println("queue");
                else if (isPQ) System.out.println("priority queue");
            }


        }
        sc.close();

    }

}
