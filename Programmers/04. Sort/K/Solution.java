package K;
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer=new ArrayList<>();

        Arrays.stream(commands).forEach(s->{
            int[] temp=Arrays.copyOfRange(array, s[0]-1, s[1]);
            Arrays.sort(temp);
            answer.add(temp[s[2]-1]);
        });
        
        return answer.stream().mapToInt(a->a).toArray();
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] a={1, 5, 2, 6, 3, 7, 4};
        int[][] c={{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

        System.out.println(s.solution(a, c));
    }
}