package School;
import java.util.*;

class Solution {
    private int[][] dp;
    private int[] dx, dy;

    Solution(){
        this.dx=new int[]{0,1};
        this.dy=new int[]{1,0};
    }

    public int dfs(int x, int y, int[][] puddles, int m, int n){
        if(x==n-1 && y==m-1){
            return 1;
        }

        if(dp[x][y]==-1){
            dp[x][y]=0;

            for(int i=0; i<2; i++){
                int nx=x+dx[i];
                int ny=y+dy[i];

                if(0<=nx && nx<n && 0<=ny && ny<m){
                    if(Arrays.stream(puddles).allMatch(s->!Arrays.equals(s, new int[]{ny+1,nx+1}))){
                        dp[x][y]+=dfs(nx, ny, puddles, m, n);
                    }
                }
            }
        }

        return dp[x][y];

    }
    public int solution(int m, int n, int[][] puddles) {
        dp=new int[n][m];
        Arrays.stream(dp).forEach(s->Arrays.fill(s, -1));

        return dfs(0,0,puddles,m,n)%1000000007;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        System.out.println(s.solution(4, 3, new int[][]{{2,2}}));
    }
}