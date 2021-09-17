package Triangle;
import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        int[][] dp=new int[triangle.length][triangle.length];
        dp[0][0]=triangle[0][0];

        for(int i=1; i<triangle.length; i++){
            for(int j=0; j<i+1; j++){
                if(j==0){
                    dp[i][j]=dp[i-1][0]+triangle[i][j];
                }else if(j==i){
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j];
                }else{
                    dp[i][j]=Math.max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]);
                }
            }
        }

        // System.out.println(Arrays.deepToString(dp));
        return Arrays.stream(dp[triangle.length-1]).max().getAsInt();
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[][] t={{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};

        s.solution(t);
    }
}