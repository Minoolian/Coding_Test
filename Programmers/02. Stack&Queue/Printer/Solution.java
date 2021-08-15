package Printer;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;

        int idx=1;
        List<Paper> pool=new ArrayList<>();
        for(int j=0;j<priorities.length;j++){
            pool.add(new Paper(j,priorities[j]));
        }
        // Map<Integer,Integer> pool=Arrays.stream(priorities).collect(Collectors.toMap(, )
        // List<Map<Integer,Integer>> pool=Arrays.stream(priorities).boxed().collect(Collectors.groupingBy());
        while(!pool.isEmpty()){
            Paper p=pool.remove(0);

            if(pool.isEmpty()){
                answer=idx;
                break;
            }
            
            
            if(pool.stream().allMatch(s->p.priority>=s.priority)){
                if(p.index==location){
                    answer=idx;
                    break;
                }else{
                    idx++;
                }
            }else{
                pool.add(p);
            }
        }
        return answer;
    }

    class Paper{
        int index;
        int priority;

        public Paper(int index, int priority){
            this.index=index;
            this.priority=priority;
        }
        
    }


    public static void main(String[] args) {
        Solution s=new Solution();
        int[] p={3,3,4,2};
        int l=3;
        System.out.println(s.solution(p, l));
    
    }
}