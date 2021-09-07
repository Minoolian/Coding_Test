package Joystick;
import java.util.*;

class Solution {
    public int solution(String name) {
        int answer=0;
        boolean check=true;

        for(int i=0; i<name.length(); i++){
            int a=(int)name.charAt(i)-65;
            int b=91-(int)name.charAt(i);

            if(a>=b){
                answer+=b;
            }else{
                answer+=a;
            }

            if(check && name.charAt(i)=='A'){
                continue;
            }else{
                if(i!=0){
                    check=false;
                }
                if(i!=name.length()-1){
                    answer++;
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        System.out.println(s.solution("JEROEN"));
    }
}