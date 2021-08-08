import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer=1;
        HashMap<String, Integer> comb = new HashMap<>();

        
        for (String[] c : clothes) {
            if (!comb.containsKey(c[1])) {
                comb.put(c[1], 1);
            } else {
                comb.put(c[1], comb.get(c[1]) + 1);
            }
        };
        

        for(int x : comb.values()){
            answer*=(x+1);

        }
        return answer-1;
    }

    public static void main(String[] args) {
        String[][] test={{"yellowhat", "headgear"}, {"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};

        Solution s=new Solution();
        System.out.println(s.solution(test));
    }
 }

/*  import java.util.*;
 import static java.util.stream.Collectors.*;

class Solution {
    public int solution(String[][] clothes) {
        return Arrays.stream(clothes)
        .collect(groupingBy(p->p[1], mapping(p->p[0], counting())))
        .values()
        .stream()
        .collect(reducing(1L, (x,y)-> x*(y+1))).intValue()-1;
        
    }

} */
