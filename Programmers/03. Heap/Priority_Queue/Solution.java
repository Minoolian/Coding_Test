package Priority_Queue;
import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> min_q=new PriorityQueue<>();
        PriorityQueue<Integer> max_q=new PriorityQueue<>(Collections.reverseOrder());

        for(String o:operations){
            String[] cmd=o.split(" ");
            int value=Integer.valueOf(cmd[1]);

            if(cmd[0].equals("I")){
                min_q.offer(value);
                max_q.offer(value);
            }else if(cmd[0].equals("D") && !max_q.isEmpty()){
                if(value==1){
                    min_q.remove(max_q.poll());
                }else{
                    max_q.remove(min_q.poll());
                }
            }
        }

        return !max_q.isEmpty() ? new int[]{max_q.poll(),min_q.poll()} : new int[]{0,0};
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        String[] op={"I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"};
        System.out.println(Arrays.toString(s.solution(op)));
    }
}