package Assignments.hw4;

import java.util.*;
public class batchetsgame {
    public static void main(String[] args) {
        //Implementation using DP
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            int stones = sc.nextInt();
            int set_size = sc.nextInt();
            int[] moves = new int[set_size];

            for(int i = 0; i < set_size; i++){
                moves[i] = sc.nextInt();
            }

            boolean[] dp = new boolean[stones + 1];
            dp[0] = false;

            for(int i = 1; i <= stones; i++){
                for(int move : moves){
                    if(i - move >= 0 && !dp[i - move]){
                        dp[i] = true;
                        break;
                    }
                }
            }

            if(dp[stones]){
                System.out.println("Stan wins");
            } else {
                System.out.println("Ollie wins");
            }
        }
        sc.close();
    }
    
}