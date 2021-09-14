package N;
import java.util.*;

class Solution {
    public int solution(int N, int number) {
        Set<Integer>[] dp=new Set[9];
        for(int i=0; i<dp.length; i++){
            dp[i]=new HashSet<>();
        }
        dp[1].add(N);

        if(N==number){
            return 1;
        }

        for(int i=2; i<9; i++){
            String temp=String.valueOf(N).repeat(i);
            dp[i].add(Integer.valueOf(temp));

            for(int j=1; j<(int)i/2+1; j++){
                for(int n:dp[j]){
                    for(int m:dp[i-j]){
                        dp[i].add(n+m);
                        dp[i].add(n-m);
                        dp[i].add(m-n);
                        dp[i].add(n*m);
                        if(m!=0) dp[i].add((int)n/m);
                        if(n!=0) dp[i].add((int)m/n);
                    }
                }
            }

            if(dp[i].contains(number)){
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int n=5;
        int num=31168;
        System.out.println(s.solution(n, num));
    }
}