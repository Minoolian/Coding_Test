package baekjoon.snake_3190;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int n;
    private static int k;

    static int[][] map;
    static Map<Integer, String> transform;

    static Deque<Node> snake;
    private static int l;

    static int[] dx = new int[]{0, 1, 0, -1};
    static int[] dy = new int[]{1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        map = new int[n][n];

        k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            map[x - 1][y - 1] = 1;
        }

        l = Integer.parseInt(br.readLine());
        transform = new HashMap<>();
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            int sec = Integer.parseInt(st.nextToken());
            String dir = st.nextToken();

            transform.put(sec, dir);
        }

        snake = new LinkedList<>();
        snake.add(new Node(0, 0, 0));
        int curSec = 0;
        while (true) {
            curSec++;

            Node peek = snake.peekLast();
            int nx = peek.x + dx[peek.dir];
            int ny = peek.y + dy[peek.dir];
            int ndir = peek.dir;

            if (0 > nx || nx >= n || 0 > ny || ny >= n) break;

            if (transform.containsKey(curSec)) {
                if (transform.get(curSec).equals("L")) ndir = (ndir + 3) % 4;
                else ndir = (ndir + 1) % 4;
            }

            Node nNode = new Node(nx, ny, ndir);
            if (snake.contains(nNode)) break;

            if (map[nx][ny] == 1) map[nx][ny] = 0;
            else snake.removeFirst();

            snake.add(nNode);
        }

        System.out.println(curSec);

    }

    static class Node {
        int x;
        int y;
        int dir;

        public Node(int x, int y, int dir) {
            this.x = x;
            this.y = y;
            this.dir = dir;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Node node = (Node) o;
            return x == node.x && y == node.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

}
