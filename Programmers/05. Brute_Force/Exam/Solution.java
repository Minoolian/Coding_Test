package Exam;
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[][] student={{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};
        int[] answer={0,0,0};

        for(int i=0; i<answers.length; i++){
            for(int j=0; j<3; j++){
                if(student[j][i%student[j].length]==answers[i]){
                    answer[j]+=1;
                }
            }
        }

        List<Integer> a=new ArrayList<>();
        int max=Math.max(answer[0],Math.max(answer[1],answer[2]));
        for(int i=1; i<answer.length+1; i++){
            if(max==answer[i-1]){
                a.add(i);
            }
        }

        return a.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] a={1,3,2,4,2};
        System.out.println(Arrays.toString(s.solution(a)));
    }
}