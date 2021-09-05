package Cloth;
import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        List<Integer> l=Arrays.stream(lost).boxed().collect(Collectors.toList());
        List<Integer> r=Arrays.stream(reserve).boxed().collect(Collectors.toList());
        for(int i=1; i<n+1; i++){
            if(l.contains(i) && r.contains(i)){
                l.remove(Integer.valueOf(i));
                r.remove(Integer.valueOf(i));
            }
        }

        List<Integer> student=new ArrayList<>();
        student.add(0);
        for(int i=1; i<n+1; i++){
            if(r.contains(i)){
                student.add(2);
            }else{
                student.add(1);
            }
        }
        student.add(0);

        for(int idx:l){
            student.set(idx, student.get(idx)-1);
            if(student.get(idx-1)==2){
                student.set(idx, student.get(idx)+1);
                student.set(idx-1, student.get(idx-1)-1);
            }
            if(student.get(idx+1)==2){
                student.set(idx, student.get(idx)+1);
                student.set(idx+1, student.get(idx+1)-1);
            }
        }


        return Collections.frequency(student, 1)+Collections.frequency(student, 2);
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int n=5;
        int[] r={2,4};
        int[] l={1,3,5};
        System.out.println(s.solution(n, l, r));
    }
}