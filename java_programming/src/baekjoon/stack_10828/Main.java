package baekjoon.stack_10828;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer n = Integer.parseInt(br.readLine());

        List<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String cmd = br.readLine();
            String[] c = cmd.split(" ");

            switch (c[0]) {
                case "push":
                    result.add(c[1]);
                    break;
                case "pop":
                    if(result.isEmpty()) System.out.println(-1);
                    else System.out.println(result.remove(result.size()-1));
                    break;
                case "size":
                    System.out.println(result.size());
                    break;
                case "empty":
                    System.out.println(result.isEmpty() ? "1" : "0");
                    break;
                case "top":
                    if(result.isEmpty()) System.out.println(-1);
                    else System.out.println(result.get(result.size()-1));
            }
        }

    }
}
