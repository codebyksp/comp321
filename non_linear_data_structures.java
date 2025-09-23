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
        // 3. Balanced BST (TreeMap / TreeSet)
        TreeMap<Integer, String> map = new TreeMap<>();
        map.put(1, "One");           // insert key-value
        map.get(1);                  // get value by key
        map.containsKey(1);          // check key existence
        map.remove(1);               // remove key-value
        map.firstKey();              // smallest key
        map.lastKey();               // largest key
        map.higherKey(1);            // smallest key > 1
        map.lowerKey(1);             // largest key < 1
        map.size();                  // number of entries
        map.isEmpty();

        // TreeSet: stores only keys
        TreeSet<Integer> set = new TreeSet<>();
        set.add(5);                  // insert key
        set.remove(5);               // remove key
        set.contains(5);             // check existence
        set.first();                 // smallest element
        set.last();                  // largest element
        set.higher(5);               // smallest > 5
        set.lower(5);                // largest < 5
        set.size();
        set.isEmpty();

        // 5. Heap vs BST
        // Heap (PriorityQueue): min-heap by default
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        minHeap.add(5);
        minHeap.poll();              // remove smallest
        minHeap.peek();              // view smallest

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
        // Heap vs BST: Heap = priority-based, BST = order-based.
        // HashMap vs Hashtable: HashMap is non-synchronized and allows nulls; Hashtable is synchronized and doesn’t allow nulls.
        // LinkedHashMap: predictable iteration order (useful for LRU cache etc.).
    }
}