package baekjoon.escape_ball_13460;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int hole_x;
    private static int hole_y;
    private static int blue_x;
    private static int blue_y;
    private static int red_x;
    private static int red_y;
    private static boolean[][][][] visited;

    private static int[] dx = new int[]{0, 1, 0, -1};
    private static int[] dy = new int[]{1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        String[][] board = new String[n][];
        visited = new boolean[n][m][n][m];

        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                String e = board[i][j];

                if (e.equals("O")) {
                    hole_x = i;
                    hole_y = j;
                } else if (e.equals("B")) {
                    blue_x = i;
                    blue_y = j;
                } else if (e.equals("R")) {
                    red_x = i;
                    red_y = j;
                }
            }
        }

        Queue<Marble> q = new LinkedList<>();
        q.add(new Marble(red_x, red_y, blue_x, blue_y, 1));

        visited[red_x][red_y][blue_x][blue_y] = true;

        int result = -1;
        loop:
        while (!q.isEmpty()) {
            Marble mar = q.poll();

            int cur_red_x = mar.red_x;
            int cur_red_y = mar.red_y;
            int cur_blue_x = mar.blue_x;
            int cur_blue_y = mar.blue_y;
            int cur_n = mar.n;

            if (mar.n > 10) {
                break loop;
            }

            for (int i = 0; i < 4; i++) {
                int new_red_x = cur_red_x;
                int new_red_y = cur_red_y;
                int new_blue_x = cur_blue_x;
                int new_blue_y = cur_blue_y;

                boolean hole_in_red = false;
                boolean hole_in_blue = false;

                while (!board[new_red_x + dx[i]][new_red_y + dy[i]].equals("#")) {
                    new_red_x += dx[i];
                    new_red_y += dy[i];

                    if (new_red_x == hole_x && new_red_y == hole_y) {
                        hole_in_red = true;
                        break;
                    }
                }

                while (!board[new_blue_x + dx[i]][new_blue_y + dy[i]].equals("#")) {
                    new_blue_x += dx[i];
                    new_blue_y += dy[i];

                    if (new_blue_x == hole_x && new_blue_y == hole_y) {
                        hole_in_blue = true;
                        break;
                    }
                }

                if(hole_in_blue) continue;

                if (hole_in_red && !hole_in_blue) {
                    result = cur_n;
                    break loop;
                }

                if (new_red_x == new_blue_x && new_red_y == new_blue_y) {
                    if (i == 0) {
                        if(cur_red_y < cur_blue_y) new_red_y -= 1;
                        else new_blue_y -= 1;
                    } else if (i==1) {
                        if(cur_red_x < cur_blue_x) new_red_x -= 1;
                        else new_blue_x -= 1;
                    } else if (i == 2) {
                        if(cur_red_y > cur_blue_y) new_red_y += 1;
                        else new_blue_y += 1;
                    } else {
                        if(cur_red_x > cur_blue_x) new_red_x += 1;
                        else new_blue_x += 1;
                    }
                }

                if (!visited[new_red_x][new_red_y][new_blue_x][new_blue_y]) {
                    visited[new_red_x][new_red_y][new_blue_x][new_blue_y] = true;
                    q.add(new Marble(new_red_x, new_red_y, new_blue_x, new_blue_y, cur_n + 1));
                }
            }
        }

        System.out.println(result);
    }
}

class Marble {
    int red_x;
    int red_y;
    int blue_x;
    int blue_y;
    int n;

    public Marble(int red_x, int red_y, int blue_x, int blue_y, int n) {
        this.red_x = red_x;
        this.red_y = red_y;
        this.blue_x = blue_x;
        this.blue_y = blue_y;
        this.n = n;
    }
}
