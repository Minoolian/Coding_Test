package baekjoon.crazy_arduino_8972;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int R, C;
    static char[][] map;

    static Queue<Node> me = new LinkedList<>();
    static Queue<Node> arduino = new LinkedList<>();

    static int[] dx = {0, 1, 1, 1, 0, 0, 0, -1, -1, -1};
    static int[] dy = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
                if (map[i][j] == 'I') me.offer(new Node(i, j));
                if (map[i][j] == 'R') arduino.offer(new Node(i, j));
            }
        }

        int count = 0;

        String cmd = br.readLine();
        for(String s : cmd.split("")){
            int dir = Integer.parseInt(s);

            if (!moveMe(dir)) {
                System.out.println("kraj " + (count+1));
                return;
            }
            if(!moveArduino()) {
                System.out.println("kraj " + (count+1));
                return;
            }

            map();
            count++;
        }

        for (char[] chars : map) {
            for (char c : chars) {
                System.out.print(c);
            }
            System.out.println();
        }
    }

    public static boolean moveMe(int dir) {
        Node node = me.poll();

        int nx = node.x + dx[dir];
        int ny = node.y + dy[dir];

        if (map[nx][ny] == 'R') return false;
        map[node.x][node.y] = '.';
        map[nx][ny] = 'I';
        me.offer(new Node(nx, ny));
        return true;
    }

    public static boolean moveArduino() {
        int[][] temp = new int[R][C];
        Node peek = me.peek();

        int me_x = peek.x;
        int me_y = peek.y;

        while (!arduino.isEmpty()) {
            Node node = arduino.poll();

            int min_dist = Integer.MAX_VALUE;
            int cur_dir = 0;
            for (int dir = 1; dir < 10; dir++) {
                int nx = node.x + dx[dir];
                int ny = node.y + dy[dir];

                if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;

                int dist = Math.abs(me_x - nx) + Math.abs(me_y - ny);

                if (dist < min_dist) {
                    min_dist = dist;
                    cur_dir = dir;
                }
            }

            int new_x = node.x + dx[cur_dir];
            int new_y = node.y + dy[cur_dir];

            if (map[new_x][new_y] == 'I') return false;

            temp[new_x][new_y]++;
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (temp[i][j] == 1) arduino.offer(new Node(i, j));
            }
        }

        return true;
    }

    public static void map() {
        for(int i=0;i<R;i++) Arrays.fill(map[i], '.');

        Node node = me.peek();

        map[node.x][node.y] = 'I';

        for(int i=0;i<arduino.size();i++) {
            Node ar = arduino.poll();
            map[ar.x][ar.y] = 'R';
            arduino.add(new Node(ar.x, ar.y));
        }
    }

    static class Node {
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
