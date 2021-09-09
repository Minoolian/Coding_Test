package Boat;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        List<Integer> p=Arrays.stream(people).boxed().collect(Collectors.toList());
        p.sort(Comparator.reverseOrder());

        int left=0;
        int right=p.size()-1;

        while(left<=right){
            if(p.get(left)+p.get(right)<=limit){
                left++;
                right--;
            }else{
                left++;
            }

            answer++;
        }
        

        return answer;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] p={70, 50, 80, 50};
        int l=100;
        s.solution(p, l);
    }
}