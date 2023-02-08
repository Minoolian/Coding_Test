package baekjoon.bothSideScales_2629;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int n;
    private static int[] arr;
    private static boolean[][] dp;
    private static int m;
    private static int v;
    private static int max = 15000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        dp = new boolean[31][max + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        find_dp(0, 0);

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            v = Integer.parseInt(st.nextToken());
            if (v > 15000) sb.append("N ");
            else sb.append(dp[n][v] ? "Y " : "N ");
        }

        System.out.println(sb);
    }

    static void find_dp(int idx, int weight) {
        if (dp[idx][weight]) return;
        dp[idx][weight] = true;
        if (idx == n) return;

        find_dp(idx + 1, weight + arr[idx + 1]);
        find_dp(idx + 1, weight);
        find_dp(idx + 1, Math.abs(weight - arr[idx + 1]));
    }
}
