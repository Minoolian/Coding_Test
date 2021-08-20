package Disk_Controller;
import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        
        PriorityQueue<int[]> t_jobs=new PriorityQueue<>(
            new Comparator<int[]>(){
                public int compare(int[] o1, int[] o2) {
                    return o1[1]-o2[1];
                }
            }
        );

        Arrays.sort(jobs, new Comparator<int[]>(){
            public int compare(int[] o1, int[] o2) {
                return o1[0]-o2[0];
            }
        }
        );

        int time=0;
        int cur=0;

        while(true){
            while(cur < jobs.length && jobs[cur][0]<=time){
                t_jobs.offer(jobs[cur]);
                cur++;
            }
            if(t_jobs.size()==0){
                time=jobs[cur][0];
                continue;
            }

            int[] job=t_jobs.poll();
            time+=job[1];
            answer+=time-job[0];

            if(cur==jobs.length && t_jobs.size()==0){
                break;
            }

        }

        answer/=jobs.length;

        return answer;
    }
}