package programmers.drill_oil_250136;

import java.util.*;

class Solution {
    int[] dx = new int[]{0, -1, 0, 1};
    int[] dy = new int[]{1, 0, -1, 0};
    Map<Integer, Integer> map = new HashMap<>();
    Set<Integer> col;

    public int solution(int[][] land) {
        for (int j = 0; j < land[0].length; j++) {
            for (int i = 0; i < land.length; i++) {
                if(land[i][j] == 1){
                    int size = 0;

                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[]{i, j});
                    col = new HashSet<>();
                    land[i][j] = 0;
                    while(!q.isEmpty()){
                        int[] idx = q.poll();
                        size++;
                        col.add(idx[1]);

                        for(int k = 0; k < 4; k++){
                            int nx = idx[0] + dx[k];
                            int ny = idx[1] + dy[k];

                            if (valid(nx, ny, land)) {
                                q.offer(new int[]{nx, ny});
                                land[nx][ny] = 0;
                            }
                        }
                    }

                    for(int c : col){
                        map.put(c, size+map.getOrDefault(c, 0));
                    }
                }
            }
        }

        return map.values().stream().max(Integer::compareTo).get();

    }

    public boolean valid(int x, int y, int[][] land) {
        return x >= 0 && x < land.length && y >= 0 && y < land[0].length && land[x][y] == 1;
    }
}


/*import java.util.*;
// visited는 land로 대체
// 열 정보로 ㅇㅋㅇㅋ 예에쑤
class Solution {
    int[] dx = new int[]{0, 1, 0, -1};
    int[] dy = new int[]{1, 0, -1, 0};
    int[][] visited;
    int visitNum = 1;
    Map<Position, Integer> quantity = new HashMap<>();
    List<Position> link;

    public int solution(int[][] land) {
        visited = new int[land.length][land[0].length];
        int result = 0;

        for (int j = 0; j < land[0].length; j++) {
            int total = 0;
            Set<Integer> drilled = new HashSet<>(); // 아까숫자 1파먹었으면 다시 1 안파먹게 ㅇㅋ?
            for (int i = 0; i < land.length; i++) {
                if (land[i][j] == 1 && visited[i][j] == 0) {
                    link = new ArrayList<>(); // 오일의 x,y를 저장해
                    int oil = dfs(i, j, land); // 지금 dfs한 땅 크기
                    visitNum++; // 방금전 까진 1번땅 -> 다음 땅 찾을땐 2번땅

                    for (Position p : link) {
                        quantity.put(p, oil); // 재활용을 위해서 하는짓거리
                    }
                }

                if (visited[i][j] != 0 && !drilled.contains(visited[i][j])) {
                    total += quantity.get(new Position(i, j));
                    drilled.add(visited[i][j]); // 7번땅 이미 셌다. 2번땅 이미셌당
                }
            }

            result = Math.max(result, total);
        }

        return result;
    }

    public int dfs(int x, int y, int[][] land) {
        visited[x][y] = visitNum; // 땅번호로 visited에 저장
        link.add(new Position(x, y)); // 오일땅 좌표 저장

        int count = 1; // 땅 크기 반환용
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i]; // 새좌표 동서남북
            if (valid(nx, ny, land) && visited[nx][ny] == 0) {
                count += dfs(nx, ny, land);
            }
        }

        return count;
    }

    public boolean valid(int x, int y, int[][] land) {
        return x >= 0 && x < land.length && y >= 0 && y < land[0].length && land[x][y] == 1;
    }

    class Position {
        int x;
        int y;

        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Position position = (Position) o;
            return x == position.x && y == position.y;
        }

        public int hashCode() {
            return Objects.hash(x, y);
        }
    }
}*/

/*import java.util.*;

class Solution {
    int[] dx = new int[]{0, -1, 0, 1};
    int[] dy = new int[]{1, 0, -1, 0};
    Map<Integer, Integer> map = new HashMap<>();
    Set<Integer> col;
    Queue<int[]> q = new LinkedList<>();

    public int solution(int[][] land) {
        for (int j = 0; j < land[0].length; j++) {
            for (int i = 0; i < land.length; i++) {
                if (land[i][j] == 1) {
                    col = new HashSet<>();
                    int oil = dfs(i, j, land); // 지금 dfs한 땅 크기

                    for(Integer c : col){
                        map.put(c, oil + map.getOrDefault(c, 0));
                    }
                }
            }
        }

        return map.values().stream().max(Integer::compareTo).get();
        *//*int result = 0;
        for(int v : map.values()){
            result = Math.max(result, v);
        }

        return result;*//*
    }

    public int dfs(int x, int y, int[][] land) {
        land[x][y] = 0;
        col.add(y);

        int count = 1; // 땅 크기 반환용
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i]; // 새좌표 동서남북
            if (valid(nx, ny, land)) {
                count += dfs(nx, ny, land);
            }
        }

        return count;
    }

    public boolean valid(int x, int y, int[][] land) {
        return x >= 0 && x < land.length && y >= 0 && y < land[0].length && land[x][y] == 1;
    }
}*/
