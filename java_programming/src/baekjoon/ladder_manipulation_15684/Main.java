package baekjoon.ladder_manipulation_15684;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static int n;
    private static int m;
    private static int h;

    private static int[][] map;

    private static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        map = new int[n + 1][h + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            map[b][a] = 1;
            map[b+1][a] = -1;
        }

        result=4;
        dfs(1, 1, 0);

        System.out.println(result!=4 ? result : -1);

    }

    public static void dfs(int cur_col, int cur_height, int depth) {
        // 1. 정답이 맞는지 확인
        if (goDown()) {
            result = Math.min(result, depth);
            return;
        }

        if(depth==3) return;

        for (int col = 1; col < n; col++) {
            for (int height = 1; height <= h; height++) {
                if(map[col][height]!=0 || map[col+1][height]!=0) continue;

                map[col][height] = 1;
                map[col+1][height] = -1;

                dfs(col, height, depth+1);

                map[col][height] = 0;
                map[col+1][height] = 0;

                if(depth >= result-1) return;
            }
        }
    }

    public static boolean goDown() {
        for (int i = 1; i <= n; i++) {
            int col = i;
            int height = 1;

            while (height <= h) {
                int dir = map[col][height];

                if (dir == 1) col++;
                else if (dir == -1) col--;
                height++;
            }

            if (col != i) return false;
        }
        return true;
    }
}
