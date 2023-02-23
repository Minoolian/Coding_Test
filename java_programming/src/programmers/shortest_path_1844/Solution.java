package programmers.shortest_path_1844;

import java.util.LinkedList;
import java.util.Queue;

class Solution {

    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    boolean[][] visited;

    public int solution(int[][] maps) {

        visited = new boolean[maps.length][maps[0].length];

        Queue<int[]> q = new LinkedList<>();

        q.offer(new int[]{0, 0, 1});
        visited[0][0] = true;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int dist = cur[2];

            if (x == maps.length-1 && y == maps[0].length-1) return dist;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (isValid(nx, ny) && !visited[nx][ny] && maps[nx][ny] == 1) {
                    q.offer(new int[]{nx, ny, dist + 1});
                    visited[nx][ny] = true;
                }
            }
        }

        return -1;
    }

    public boolean isValid(int x, int y) {
        return x >= 0 && x < visited.length && y >= 0 && y < visited[0].length;
    }


    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(new int[][]{{1, 0, 1, 1, 1}, {1, 0, 1, 0, 1}, {1, 0, 1, 1, 1}, {1, 1, 1, 0, 1}, {0, 0, 0, 0, 1}});
    }
}