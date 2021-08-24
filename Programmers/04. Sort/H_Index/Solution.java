package H_Index;
import java.util.*;
import java.util.stream.Stream;

class Solution {
    public int solution(int[] citations) {
        int answer = citations.length;
        Integer[] citation= Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(citation, Collections.reverseOrder());

        for(int i=0; i<citation.length; i++){
            if(citation[i]<i+1){
                answer=i;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] c={3,0,6,1,5};

        System.out.println(s.solution(c));
    }
}