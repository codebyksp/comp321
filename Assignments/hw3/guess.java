package Assignments.hw3;

import java.util.Scanner;

public class guess {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int low = 1;
        int high = 1000;

        while (low <= high) {
            int mid = (low + high) / 2;
            System.out.println(mid);   // print guess (auto-flush in println)

            String response = sc.nextLine(); // read response

            if (response.equals("correct")) {
                break;
            } else if (response.equals("lower")) {
                high = mid - 1;
            } else if (response.equals("higher")) {
                low = mid + 1;
            }
        }

        // Do NOT close sc here in interactive problems
        // sc.close();
    }
}
