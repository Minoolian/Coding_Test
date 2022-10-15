package baekjoon.string_explosion_9935;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String st = br.readLine();
        String exp = br.readLine();

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < st.length(); i++) {
            stack.push(st.charAt(i));
            if(stack.size() < exp.length()) continue;

            boolean flag = true;
            for (int j = 0; j < exp.length(); j++) {
                if(stack.get(stack.size()-exp.length()+j) != exp.charAt(j)) {
                    flag = false;
                    break;
                }
            }

            if(flag){
                for (int j = 0; j < exp.length(); j++) {
                    stack.pop();
                }
            }

        }

        String result = stack.size() != 0 ? stack.stream().map(c -> c.toString()).collect(Collectors.joining()) : "FRULA";
        System.out.println(result);
    }
}
