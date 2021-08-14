package Fuction_Develop;
import java.util.Arrays;

class Solution {

    public int[] solution(int[] progresses, int[] speeds){
        int[] day0fend=new int[100];
        int day=-1;

        for(int i=0; i<progresses.length; i++){
            while (progresses[i] + (day*speeds[i]) <100){
                day++;
            }

            day0fend[day]++;
        }

        return Arrays.stream(day0fend).filter(i -> i!=0).toArray();
    }

    public static void main(String[] args) {
        int[] progresses={93, 30, 55};
        int[] speeds={1, 30, 5};

        Solution s=new Solution();
        int[] answer=s.solution(progresses, speeds);

        System.out.println(Arrays.toString(answer));
    }
    
}
