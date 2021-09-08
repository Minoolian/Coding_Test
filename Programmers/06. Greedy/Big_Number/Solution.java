package Big_Number;
import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        char[] result = new char[number.length() - k];
        Stack<Character> stack = new Stack<>();

        for (int i=0; i<number.length(); i++) {
            char c = number.charAt(i);
            while (!stack.isEmpty() && stack.peek() < c && k-- > 0) {
                stack.pop();
            }
            stack.push(c);
        }
        for (int i=0; i<result.length; i++) {
            result[i] = stack.get(i);
        }
        return new String(result);
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        String n="1231234";
        int k=3;
        System.out.println(s.solution(n, k));
    }
}

// 시간초과
/* import java.util.*;

class Solution {
    public String solution(String number, int k) {
        String answer = "";
        int idx=0;

        for(int i=0; i<number.length()-k; i++){
            int max=0;
            for(int j=idx; j<i+k+1; j++){
                int num=(int)number.charAt(j);
                if(max<num){
                    idx=j+1;
                    max=num;

                    if(num==9){
                        break;
                    }
                }
            }

            answer+=(char)max;
        }
        return answer;
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        String n="1924";
        int k=2;
        System.out.println(s.solution(n, k));
    }
} */