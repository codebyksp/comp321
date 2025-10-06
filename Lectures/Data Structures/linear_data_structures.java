import java.util.ArrayList;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;
import java.util.PriorityQueue;

public class linear_data_structures {
    // ============================
    // 1. Static Array
    // ============================
    public void staticArrayExample() {
        int[] arr = new int[10];       // create array of size 10
        arr[0] = 5;                    // set value
        int val = arr[0];              // get value
        int len = arr.length;          // length of array
    }

    // ============================
    // 2. Resizable Array (ArrayList)
    // ============================
    public void arrayListExample() {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);                  // add element at end
        list.add(1, 20);               // add element at index 1
        list.get(0);                   // get element at index 0
        list.set(0, 15);               // set element at index 0
        list.remove(1);                // remove element at index 1
        list.size();                   // current size
        list.isEmpty();                // check if empty
        list.clear();                  // remove all elements
        list.contains(10);             // check if list contains 10
        list.indexOf(10);              // index of element
    }

    // ============================
    // 3. Stack
    // ============================
    public void stackExample() {
        Stack<Integer> stack = new Stack<>();
        stack.push(5);                 // push element
        stack.pop();                   // remove top element
        stack.peek();                  // view top element
        stack.isEmpty();               // check if empty
        stack.size();                  // number of elements
    }

// ============================
// 4. Queue
// ============================
public void queueExample() {
    Queue<Integer> queue = new LinkedList<>();
    queue.add(5);                   // add element (throws exception if full)
    queue.offer(10);                // add element (returns false if full)
    queue.remove();                 // remove head element
    queue.poll();                   // remove head or null if empty
    queue.peek();                   // view head element
    queue.isEmpty();                // check if empty
    queue.size();                   // number of elements
}

// ============================
// 5. Priority Queue
// ============================
public void priorityQueueExample() {
    PriorityQueue<Integer> pq = new PriorityQueue<>(); // min-heap by default -> log time 
    pq.add(5);                   // add element
    pq.offer(10);                // add element
    pq.poll();                   // remove smallest element
    pq.peek();                   // view smallest element
    pq.isEmpty();                // check if empty
    pq.size();                   // number of elements

    // For max-heap:
    PriorityQueue<Integer> maxPQ = new PriorityQueue<>((a,b)->b-a);
}

// ============================
// 6. Linked List
// ============================
public void linkedListExample() {
    LinkedList<Integer> ll = new LinkedList<>();
    ll.add(5);                   // add at end
    ll.addFirst(10);             // add at beginning
    ll.addLast(15);              // add at end
    ll.get(0);                   // get element at index
    ll.set(0, 20);               // set element at index
    ll.remove();                 // remove first element
    ll.removeFirst();            // remove first element
    ll.removeLast();             // remove last element
    ll.remove(1);                // remove at index
    ll.isEmpty();                // check if empty
    ll.size();                   // number of elements
    ll.contains(10);             // check if list contains element
    ll.indexOf(15);              // first index of element
    ll.lastIndexOf(15);          // last index of element
}

}
