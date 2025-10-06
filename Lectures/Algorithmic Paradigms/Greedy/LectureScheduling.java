import java.io.*;
import java.util.*;

public class LectureScheduling {
    private static class Lecture {
        int start, end, idx;
        Lecture(int s, int e, int i) { start = s; end = e; idx = i; }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // Read number of test cases (use 1 if single case)
        int T = Integer.parseInt(br.readLine().trim());
        StringBuilder out = new StringBuilder();

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine().trim());
            Lecture[] lectures = new Lecture[n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int s = Integer.parseInt(st.nextToken());
                int e = Integer.parseInt(st.nextToken());
                lectures[i] = new Lecture(s, e, i);
            }

            // Sort by start time (ascending). Tie-break by end time.
            Arrays.sort(lectures, (a, b) -> {
                if (a.start != b.start) return Integer.compare(a.start, b.start);
                return Integer.compare(a.end, b.end);
            });

            // PQ holds int[]{endTime, roomId}, ordered by smallest endTime
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

            int[] assignment = new int[n]; // assignment[originalIndex] = roomId (1-based)
            int rooms = 0;

            for (Lecture lec : lectures) {
                if (!pq.isEmpty() && pq.peek()[0] <= lec.start) {
                    // reuse classroom
                    int[] top = pq.poll();
                    int roomId = top[1];
                    assignment[lec.idx] = roomId;
                    // push updated finish time for that room
                    pq.add(new int[]{lec.end, roomId});
                } else {
                    // allocate new classroom
                    rooms++;
                    assignment[lec.idx] = rooms;
                    pq.add(new int[]{lec.end, rooms});
                }
            }

            // Output: number of rooms, then room assignment for each lecture (in original order)
            out.append(rooms).append('\n');
            if (n > 0) {
                for (int i = 0; i < n; i++) {
                    out.append(assignment[i]);
                    if (i + 1 < n) out.append(' ');
                }
                out.append('\n');
            } else {
                out.append('\n');
            }
        }

        System.out.print(out.toString());
    }
}
