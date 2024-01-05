package programmers.data_analy_250121;

import java.util.Arrays;
import java.util.Map;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> map = Map.of("code", 0, "date", 1, "maximum", 2, "remain", 3);
        return Arrays.stream(data).filter(d -> d[map.get(ext)] < val_ext).sorted((o1, o2) -> o1[map.get(sort_by)] - o2[map.get(sort_by)]).toArray(int[][]::new);
    }
}
