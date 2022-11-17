package baekjoon.dragon_curve_15685;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static int[] dx = {0, -1, 0, 1};
    private static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        // 0 우, 1 상, 2 좌, 3 하

        // 1세대 0
        // 2세대 0 1
        // 3세대 0 1 2 1
        // 4세대 0 1 2 1 2 3 2 1
        // 5세대 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[101][101];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            Stack<Integer> dragon = new Stack<>();
            dragon.push(d);
            Stack<Integer> temp = new Stack<>();

            int nx = y + dx[d];
            int ny = x + dy[d];
            map[y][x] = 1;
            map[nx][ny] = 1;

            for (int j = 0; j < g; j++) {
                temp.addAll(dragon);

                while (!temp.isEmpty()) {
                    Integer dir = temp.pop();
                    int ndir = (dir + 1) % 4;
                    nx = nx + dx[ndir];
                    ny = ny + dy[ndir];
                    map[nx][ny] = 1;
                    dragon.push(ndir);
                }
            }
        }

        int result = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (map[i][j] == 1 && map[i + 1][j] == 1 && map[i][j + 1] == 1 && map[i + 1][j + 1] == 1) result++;
            }
        }

        System.out.println(result);


    }
}
