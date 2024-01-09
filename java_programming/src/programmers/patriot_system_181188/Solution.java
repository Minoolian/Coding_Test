package programmers.patriot_system_181188;

import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, (o1, o2) -> o1[1] - o2[1]);

        int pos = 0;
        int result = 0;
        for(int[] target : targets){
            if(pos < target[1] && pos <= target[0]) {
                result++;
                pos = target[1];
            }
        }

        return result;
    }
}
