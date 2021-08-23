package Max_Num;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] numbers) {
        List<String> num=new ArrayList<>();

        for(int n:numbers){
            num.add(String.valueOf(n));
        }
        num.sort(new Comparator<String>(){
            @Override
            public int compare(String o1, String o2) {
                return o2.repeat(3).compareTo(o1.repeat(3));
            }            
        });
        String temp=num.stream().collect(Collectors.joining(""));
        return temp.charAt(0)=='0' ? "0":temp;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int[] n={90,908,89,898,10,101,1,8,9};
        System.out.println(s.solution(n));

    }
}