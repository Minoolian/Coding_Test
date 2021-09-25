package Steal;
import java.util.*;

class Solution {
    public int solution(int[] money) {
        int[] dp=new int[money.length];

        dp[0]=money[0];
        dp[1]=Integer.max(dp[0], money[1]);

        for(int i=2; i<money.length-1; i++){
            dp[i]=Integer.max(dp[i-1], money[i]+dp[i-2]);
        }

        int[] dp2=new int[money.length];
        dp2[1]=money[1];

        for(int i=2; i<money.length; i++){
            dp2[i]=Integer.max(dp2[i-1], money[i]+dp2[i-2]);
        }

        return Integer.max(Arrays.stream(dp).max().getAsInt(), Arrays.stream(dp2).max().getAsInt());
    }
}