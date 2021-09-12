package Camera;
import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        Arrays.sort(routes, (a,b)->Integer.compare(a[0], b[0]));
        int s=routes[0][0], e=routes[0][1];
        
        for(int[] a:Arrays.copyOfRange(routes, 1, routes.length)){
            if(e<a[0]){
                answer++;
                s=a[0]; 
                e=a[1];
                continue;
            }
            if(s<a[0]) s=a[0];
            if(e>a[1]) e=a[1];
        }
        return answer+1;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[][] r={{-20,15}, {-14,-5}, {-18,-13}, {-5,-3}};
        System.out.println(s.solution(r));
    }
}