package Network;
import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        List<Integer> v=new ArrayList<>();
        Queue<Integer> q=new LinkedList<>();
        for(int i=0; i<n; i++) 
            v.add(i);

        while(!v.isEmpty()){
            q.offer(v.remove(v.size()-1));
            answer++;

            while(!q.isEmpty()){
                int u=q.poll();
                for(int i=0; i<computers[u].length; i++){
                    if(computers[u][i]==1 && v.contains(i)){
                        q.offer(i);
                        v.remove(Integer.valueOf(i));
                    }
                }
            }
        }
        
        
        return answer;
    }
}