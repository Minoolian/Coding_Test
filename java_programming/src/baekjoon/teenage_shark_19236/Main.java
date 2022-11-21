package baekjoon.teenage_shark_19236;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
    static int[][] map = new int[4][4];

    static int maxSum = 0;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        List<Fish> fishes = new ArrayList<>();

        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                Fish f = new Fish(i, j, a, b-1, true);

                fishes.add(f);
                map[i][j] = a;
            }
        }

        Collections.sort(fishes);

        Fish f = fishes.get(map[0][0] - 1);
        Shark shark = new Shark(0, 0, f.dir, f.num);

        f.alive = false;
        map[0][0] = -1;

        solve(map, shark, fishes);
        System.out.println(maxSum);


    }

    static void solve(int[][] arr, Shark shark, List<Fish> fishes) {
        if(maxSum < shark.max) maxSum = shark.max;

        fishes.forEach(f -> moveFish(f, arr, fishes));

        for (int i = 1; i < 4; i++) {
            int nx = shark.x + dx[shark.dir] * i;
            int ny = shark.y + dy[shark.dir] * i;

            if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4 || arr[nx][ny] <= 0) continue;

            int[][] copiedArr = copyMap(arr);
            List<Fish> copiedFish = copyList(fishes);

            copiedArr[shark.x][shark.y] = 0;
            Fish f = copiedFish.get(arr[nx][ny] - 1);
            Shark nshark = new Shark(f.x, f.y, f.dir, shark.max + f.num);
            f.alive = false;
            copiedArr[f.x][f.y] = -1;

            solve(copiedArr, nshark, copiedFish);

        }
    }

    static int[][] copyMap(int[][] arr) {
        int[][] tmp = new int[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                tmp[i][j] = arr[i][j];
            }
        }

        return tmp;
    }

    static List<Fish> copyList(List<Fish> fishes) {
        List<Fish> tmp = new ArrayList<>();
        fishes.forEach(f -> tmp.add(new Fish(f.x, f.y, f.num, f.dir, f.alive)));

        return tmp;
    }

    static void moveFish(Fish fish, int[][] arr, List<Fish> fishes) {
        if (!fish.alive) return;

        for (int i = 0; i < 8; i++) {
            int ndir = (fish.dir + i) % 8;
            int nx = fish.x + dx[ndir];
            int ny = fish.y + dy[ndir];

            if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4 || arr[nx][ny] <= -1) continue;

            arr[fish.x][fish.y] = 0;

            if (arr[nx][ny] == 0) {
                fish.x = nx;
                fish.y = ny;
            } else {
                Fish tmp = fishes.get(arr[nx][ny] - 1);
                tmp.x = fish.x;
                tmp.y = fish.y;
                arr[fish.x][fish.y] = tmp.num;

                fish.x = nx;
                fish.y = ny;

            }

            arr[nx][ny] = fish.num;
            fish.dir = ndir;
            return;

        }
    }

    static class Fish implements Comparable<Fish> {
        int x;
        int y;

        int num;
        int dir;

        boolean alive = true;

        public Fish(int x, int y, int num, int dir, boolean alive) {
            this.x = x;
            this.y = y;
            this.num = num;
            this.dir = dir;
            this.alive = alive;
        }

        @Override
        public int compareTo(Fish o) {
            return num - o.num;
        }
    }

    static class Shark {

        int x;
        int y;
        int dir;
        int max;

        public Shark(int x, int y, int dir, int max) {
            this.x = x;
            this.y = y;
            this.dir = dir;
            this.max = max;
        }
    }

}
