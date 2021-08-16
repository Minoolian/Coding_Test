package Truck;
import java.util.*;


class Solution {
    class Cur{
        int weight;
        int move;

        public Cur(int weight){
            this.weight=weight;
            this.move=1;
        }

        public void plus(int number){
            this.move+=number;
        }
    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Queue<Integer> truck=new LinkedList<>();
        LinkedList<Cur> q=new LinkedList<>();
        for(int w:truck_weights){
            truck.offer(w);
        }

        int length=0;
        while(!truck.isEmpty()){
            if(weight>=truck.peek() && length!=bridge_length){
                weight-=truck.peek();
                q.forEach(s->s.plus(1));
                
                q.offer(new Cur(truck.poll()));
                length=q.peek().move;
                answer++;
            }else{
                Cur c=q.poll();
                int nt=bridge_length-c.move;
                weight+=c.weight;
                answer+=nt;

                q.forEach(s->s.plus(nt));
                if(!q.isEmpty()){
                    length=q.peek().move;
                }
            }
        }

        answer+=bridge_length-q.peekLast().move+1;

        return answer;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int b=5;
        int w=5;
        int[] t={2,2,2,2,1,1,1,1,1};
        System.out.println(s.solution(b, w, t));
    }
}