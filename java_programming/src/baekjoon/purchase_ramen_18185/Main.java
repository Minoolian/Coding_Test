package baekjoon.purchase_ramen_18185;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] cost = new int[]{2, 2, 3};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] temp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] factory = Arrays.copyOf(temp, temp.length + 2);

        int result = 0;
        for (int i = 0; i < n; i++) {
            if (factory[i + 1] > factory[i + 2]) {
                int count = Math.min(factory[i], factory[i + 1] - factory[i + 2]);
                result += count * 5;

                factory[i] -= count;
                factory[i + 1] -= count;

                int ncount = Math.min(factory[i], Math.min(factory[i + 1], factory[i + 2]));
                result += ncount * 7;

                factory[i] -= ncount;
                factory[i + 1] -= ncount;
                factory[i + 2] -= ncount;
            } else {
                int count = Math.min(factory[i], Math.min(factory[i + 1], factory[i + 2]));
                result += count * 7;

                factory[i] -= count;
                factory[i + 1] -= count;
                factory[i + 2] -= count;

                int ncount = Math.min(factory[i], factory[i + 1]);
                result += ncount * 5;

                factory[i] -= ncount;
                factory[i + 1] -= ncount;
            }

            result += factory[i] * 3;
            factory[i] = 0;
        }

        /*int result = 0;
        for (int i = 0; i < n; i++) {
            if (factory[i] == 0) continue;

            int cur = factory[i];
            factory[i] = 0;
            result += cur * 3;

            int state = 0;
            for (int j = i + 1; j < n; j++) {
                if (factory[j] == 0) break;

                int next = factory[j];
                if (cur >= next) cur = next;
                factory[j] -= cur;
                result += cur * cost[state];
                state = (state + 1) % 3;

                if (cur < next) break;

            }

        }*/

        System.out.println(result);


    }
}
