package baekjoon.garrymandering_17779;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int n;
    private static int[][] map, fifthZone;
    private static int[] pop;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int answer = Integer.MAX_VALUE;
        n = Integer.parseInt(br.readLine());
        map = new int[n + 1][n + 1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i+1][j+1] = Integer.parseInt(st.nextToken());
            }
        }

        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= n; y++) {
                for (int d1 = 1; d1 <= n; d1++) {
                    for (int d2 = 1; d2 <= n; d2++) {
                        if (y - d1 <= 0 || x + d1 + d2 > n || y + d2 > n) continue;

                        population(x, y, d1, d2);

                        int max = Arrays.stream(pop).max().getAsInt();
                        int min = Arrays.stream(pop).min().getAsInt();
                        answer = Math.min(answer, max-min);
                    }
                }
            }
        }

        System.out.println(answer);
    }

    private static void population(int x, int y, int d1, int d2) {
        pop = new int[5];
        fifthZone = new int[n + 1][n + 1];

        int left = 0, right = 0;
        for (int r = x; r <= x + d1 + d2; r++) {
            for (int c = y - left; c <= y + right; c++) {
                fifthZone[r][c] = 5;
                pop[4]+=map[r][c];
            }

            if (r < x + d1) left++;
            else left--;

            if (r < x + d2) right++;
            else right--;
        }

        for (int r = 1; r <= n; r++) {
            for (int c = 1; c <= n; c++) {
                if(fifthZone[r][c]==5) continue;
                if(r<x+d1 && c<=y) pop[0]+=map[r][c];
                else if(r<=x+d2 && y<c) pop[1]+=map[r][c];
                else if(x+d1<=r && c<y-d1+d2) pop[2]+=map[r][c];
                else pop[3]+=map[r][c];
            }
        }
    }
}
