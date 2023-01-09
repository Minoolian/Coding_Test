package baekjoon.roll_dice_14499;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static int n;
    private static int m;
    private static int x;
    private static int y;
    private static int[][] map;
    static int[] dice = new int[6];
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    /**
     * 2
     * 4 1 3
     * 5
     * 6
     */
    public static void dice(int dir) {
        int temp = dice[0];
        switch (dir) {
            case 1:
                dice[0] = dice[3];
                dice[3] = dice[5];
                dice[5] = dice[2];
                dice[2] = temp;
                break;

            case 2:
                dice[0] = dice[2];
                dice[2] = dice[5];
                dice[5] = dice[3];
                dice[3] = temp;
                break;

            case 3:
                dice[0] = dice[4];
                dice[4] = dice[5];
                dice[5] = dice[1];
                dice[1] = temp;
                break;

            case 4:
                dice[0] = dice[1];
                dice[1] = dice[5];
                dice[5] = dice[4];
                dice[4] = temp;
                break;

        }
    }

    public static void move(int dir) {
        if (0 <= x + dx[dir - 1] && x + dx[dir - 1] < n && 0 <= y + dy[dir - 1] && y + dy[dir - 1] < m) {
            dice(dir);

            x += dx[dir - 1];
            y += dy[dir - 1];

            if (map[x][y] == 0) map[x][y] = dice[5];
            else {
                dice[5] = map[x][y];
                map[x][y] = 0;
            }

            System.out.println(dice[0]);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int dir = Integer.parseInt(st.nextToken());
            move(dir);
        }
    }
}
