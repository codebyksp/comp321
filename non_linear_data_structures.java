package comp321;

import java.util.TreeMap;
import java.util.TreeSet;
import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;

public class non_linear_data_structures {
    public static void main(String[] args) {
        // 1. MAP
        // Declare a Map (interface) and use HashMap (implementation)
        Map<Integer, String> map = new HashMap<>();

        // Put key-value pairs
        map.put(1, "One");
        map.put(2, "Two");
        map.put(3, "Three");

        // Access values
        System.out.println(map.get(2));   // Output: Two

        // Check existence
        System.out.println(map.containsKey(3));   // true

        // Iterate over entries
        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());

        // NOTE: Yes — Java provides Red-Black Tree implementations
        // under the standard library:
        //  - java.util.TreeMap  -> a Map implemented as a Red-Black tree
        //  - java.util.TreeSet  -> a Set backed by a TreeMap (also Red-Black)
        // These classes guarantee O(log n) time for contains/insert/remove
        // because of the self-balancing Red-Black tree implementation.

        // 3. Balanced BST (TreeMap / TreeSet)
        TreeMap<Integer, String> map1 = new TreeMap<>();
        map1.put(1, "One");           // insert key-value (O(log n))
        map1.get(1);                  // get value by key (O(log n))
        map1.containsKey(1);          // check key existence (O(log n))
        map1.remove(1);               // remove key-value (O(log n))
        map1.firstKey();              // smallest key
        map1.lastKey();               // largest key
        map1.higherKey(1);            // smallest key > 1
        map1.lowerKey(1);             // largest key < 1
        map1.size();                  // number of entries
        map1.isEmpty();

        // TreeSet: stores only keys (backed by a TreeMap internally)
        TreeSet<Integer> set = new TreeSet<>();
        set.add(5);                  // insert key (O(log n))
        set.remove(5);               // remove key (O(log n))
        set.contains(5);             // check existence (O(log n))
        set.first();                 // smallest element
        set.last();                  // largest element
        set.higher(5);               // smallest > 5
        set.lower(5);                // largest < 5
        set.size();
        set.isEmpty();

        // Example: custom comparator -> still uses Red-Black tree under the hood
        TreeMap<String, Integer> custom = new TreeMap<>((a,b) -> b.compareTo(a)); // reverse order
        custom.put("a", 1);
        custom.put("z", 26);
        custom.firstKey(); // "z" because comparator reverses natural order

        // 5. Heap vs BST
        // Heap (PriorityQueue): min-heap by default
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(5);
        minHeap.poll();              // remove smallest
        minHeap.peek();              // view smallest
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        maxHeap.add(10);             // use maxHeap: add an element
        maxHeap.poll();              // use maxHeap: remove largest

        // 6. Hash Table (HashMap / HashSet / Hashtable)
        // HashMap: key -> value, non-synchronized, allows null keys/values
        HashMap<Integer, String> hashMap = new HashMap<>();
        hashMap.put(1, "One");
        hashMap.get(1);
        hashMap.containsKey(1);
        hashMap.remove(1);
        hashMap.size();
        hashMap.isEmpty();

        // HashSet: stores only keys, non-synchronized, allows null
        HashSet<Integer> hashSet = new HashSet<>();
        hashSet.add(5);
        hashSet.remove(5);
        hashSet.contains(5);
        hashSet.size();
        hashSet.isEmpty();

        // Hashtable: key -> value, synchronized, does NOT allow null key or null value
        Hashtable<Integer, String> table = new Hashtable<>();
        table.put(1, "One");
        table.get(1);
        table.containsKey(1);
        table.remove(1);
        table.size();
        table.isEmpty();

        // LinkedHashMap: predictable iteration order (insertion order)
        LinkedHashMap<Integer, String> lhm = new LinkedHashMap<>();
        lhm.put(1, "One");
        lhm.get(1);

        // Quick Notes / Tips:
        // Map vs Set:
        //   Map: key → value
        //   Set: only key (unique)
        // Balanced BSTs (TreeMap/TreeSet): O(log n) insertion/deletion/search.
        // TreeMap/TreeSet in Java are Red-Black tree implementations.
        // Heap vs BST: Heap = priority-based, BST = order-based.
        // HashMap vs Hashtable: HashMap is non-synchronized and allows nulls; Hashtable is synchronized and doesn’t allow nulls.
        // LinkedHashMap: predictable iteration order (useful for LRU cache etc.).
    }
}
}
