package baekjoon.Scale_2437;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] weight = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(weight);
        /*
        int min = weight[0];
        int max = Arrays.stream(weight).sum();
        */

        int sum=0;
        for (int i = 0; i < n; i++) {
            if(weight[i] > sum+1) break;
            sum+=weight[i];
        }

        System.out.println(sum+1);




    }
}
