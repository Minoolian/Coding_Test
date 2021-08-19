package More_Spicy;
import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> q=new PriorityQueue<>();

        Arrays.stream(scoville).forEach(q::offer);

        int a=0;
        int b=0;
        while(true){
            a=q.poll();
            if(a>=K){
                return answer;
            }

            if(!q.isEmpty()){
                answer++;
                b=q.poll();
            }else{
                return -1;
            }

            int n=a+(b*2);
            q.offer(n);
            
        }

    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] sc={1,2,3,9,10,12};
        int k=7;

        System.out.println(s.solution(sc, k));
    }
}