package baekjoon.deliver_chicken_15686;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static int n;
    private static int m;
    private static List<int[]> house;
    private static List<int[]> chicken;
    private static boolean[] visited;
    private static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        house = new ArrayList<>();
        chicken = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                if (s[j].equals("1")) house.add(new int[]{i, j});
                else if (s[j].equals("2")) chicken.add(new int[]{i, j});
            }
        }

        visited = new boolean[chicken.size()];
        dfs(0,0);
        System.out.println(ans);


    }

    public static void dfs(int cur, int count) {
        if (count == m) {
            int result = 0;
            for (int h = 0; h < house.size(); h++) {
                int temp = Integer.MAX_VALUE;
                for (int i = 0; i < visited.length; i++) {
                    if (visited[i]) {
                        temp = Math.min(temp, dist(h, i));
                    }
                }
                result+=temp;
            }

            ans = Math.min(ans, result);
        }

        for (int i = cur; i < chicken.size(); i++) {
            visited[i] = true;
            dfs(i+1, count + 1);
            visited[i] = false;
        }

    }

    private static int dist(int h, int i) {
        int[] ho = house.get(h);
        int[] ch = chicken.get(i);

        return Math.abs(ho[0]-ch[0]) + Math.abs(ho[1]-ch[1]);
    }
}
