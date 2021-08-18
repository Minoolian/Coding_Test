package Stock;
import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        List<Integer> answer=new ArrayList<>();
        
        Queue<Integer> q=new LinkedList<>();
        Arrays.stream(prices).forEach(q::offer);
        while(!q.isEmpty()){
            int result=0;
            Integer check=q.poll();

            for(Integer i:q){
                if(check<=i){
                    result+=1;
                }else{
                    result+=1;
                    break;
                }
            }
            answer.add(result);
            
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] p={1,2,3,2,3};
        int[] result=s.solution(p);
        System.out.println(Arrays.toString(result));
    }
}