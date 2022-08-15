package baekjoon.chage_sequence_1551;

import java.util.Arrays;
import java.util.Scanner;

public class Main{
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), k = sc.nextInt();

        String[] seqArr = sc.next().split(",");
        int[] intArr = Arrays.stream(seqArr).mapToInt(Integer::parseInt).toArray();

        for (int i = 0; i < k; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                intArr[j]=intArr[j+1]-intArr[j];
            }
        }

        StringBuilder sb = new StringBuilder();
        Arrays.stream(intArr).limit(n-k).forEach(num -> sb.append(num + ","));

        String result = sb.toString();
        System.out.print(result.substring(0, result.length()-1));

    }
}
