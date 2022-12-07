package baekjoon.Cubing_5373;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    private static char[][][] cube;
    private static char[] color = new char[]{'o', 'g', 'w', 'b', 'r', 'y'};

    private static Map<String, Integer> toInt = Map.of("B", 0, "L", 1, "U", 2, "R", 3, "F", 4, "D", 5);

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int test = 0; test < t; test++) {
            cube = new char[6][3][3];
            for (int i = 0; i < 6; i++) {
                for (int j = 0; j < 3; j++) {
                    for (int k = 0; k < 3; k++) {
                        cube[i][j][k] = color[i];
                    }
                }
            }
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());

            while (st.hasMoreTokens()) {
                String[] cmd = st.nextToken().split("");
                rotate(cmd[1], toInt.get(cmd[0]));
            }

            Arrays.stream(cube[2]).map(String::valueOf).forEach(System.out::println);
        }


    }

    public static void rotate(String dir, int side) {
        front(dir, side);
        side(dir, side);
    }

    private static void front(String dir, int side) {
        char temp = 0;
        if (dir.equals("+")) {
            temp = cube[side][0][0];
            cube[side][0][0] = cube[side][2][0];
            cube[side][2][0] = cube[side][2][2];
            cube[side][2][2] = cube[side][0][2];
            cube[side][0][2] = temp;

            temp = cube[side][0][1];
            cube[side][0][1] = cube[side][1][0];
            cube[side][1][0] = cube[side][2][1];
            cube[side][2][1] = cube[side][1][2];
            cube[side][1][2] = temp;
        } else if (dir.equals("-")) {
            temp = cube[side][0][2];
            cube[side][0][2] = cube[side][2][2];
            cube[side][2][2] = cube[side][2][0];
            cube[side][2][0] = cube[side][0][0];
            cube[side][0][0] = temp;

            temp = cube[side][1][2];
            cube[side][1][2] = cube[side][2][1];
            cube[side][2][1] = cube[side][1][0];
            cube[side][1][0] = cube[side][0][1];
            cube[side][0][1] = temp;
        }
    }

    private static void side(String dir, int side) {
        int count = 1;
        if (dir.equals("-")) count = 3;

        while(count>0) {
            char temp = 0;
            if (side == 0) {
                temp = cube[1][0][0];
                cube[1][0][0] = cube[2][0][0];
                cube[2][0][0] = cube[3][0][0];
                cube[3][0][0] = cube[5][2][2];
                cube[5][2][2] = temp;

                temp = cube[1][0][1];
                cube[1][0][1] = cube[2][0][1];
                cube[2][0][1] = cube[3][0][1];
                cube[3][0][1] = cube[5][2][1];
                cube[5][2][1] = temp;


                temp = cube[1][0][2];
                cube[1][0][2] = cube[2][0][2];
                cube[2][0][2] = cube[3][0][2];
                cube[3][0][2] = cube[5][2][0];
                cube[5][2][0] = temp;

            } else if (side == 4) {
                temp = cube[3][2][0];
                cube[3][2][0] = cube[2][2][0];
                cube[2][2][0] = cube[1][2][0];
                cube[1][2][0] = cube[5][0][2];
                cube[5][0][2] = temp;

                temp = cube[3][2][1];
                cube[3][2][1] = cube[2][2][1];
                cube[2][2][1] = cube[1][2][1];
                cube[1][2][1] = cube[5][0][1];
                cube[5][0][1] = temp;

                temp = cube[3][2][2];
                cube[3][2][2] = cube[2][2][2];
                cube[2][2][2] = cube[1][2][2];
                cube[1][2][2] = cube[5][0][0];
                cube[5][0][0] = temp;

            } else if (side == 3) {
                temp = cube[5][0][2];
                cube[5][0][2] = cube[0][0][2];
                cube[0][0][2] = cube[2][0][2];
                cube[2][0][2] = cube[4][0][2];
                cube[4][0][2] = temp;

                temp = cube[5][1][2];
                cube[5][1][2] = cube[0][1][2];
                cube[0][1][2] = cube[2][1][2];
                cube[2][1][2] = cube[4][1][2];
                cube[4][1][2] = temp;

                temp = cube[5][2][2];
                cube[5][2][2] = cube[0][2][2];
                cube[0][2][2] = cube[2][2][2];
                cube[2][2][2] = cube[4][2][2];
                cube[4][2][2] = temp;

            } else if (side == 1) {
                temp = cube[2][0][0];
                cube[2][0][0] = cube[0][0][0];
                cube[0][0][0] = cube[5][0][0];
                cube[5][0][0] = cube[4][0][0];
                cube[4][0][0] = temp;

                temp = cube[2][1][0];
                cube[2][1][0] = cube[0][1][0];
                cube[0][1][0] = cube[5][1][0];
                cube[5][1][0] = cube[4][1][0];
                cube[4][1][0] = temp;

                temp = cube[2][2][0];
                cube[2][2][0] = cube[0][2][0];
                cube[0][2][0] = cube[5][2][0];
                cube[5][2][0] = cube[4][2][0];
                cube[4][2][0] = temp;

            } else if (side == 2) {
                temp = cube[3][0][0];
                cube[3][0][0] = cube[0][2][0];
                cube[0][2][0] = cube[1][2][2];
                cube[1][2][2] = cube[4][0][2];
                cube[4][0][2] = temp;

                temp = cube[3][1][0];
                cube[3][1][0] = cube[0][2][1];
                cube[0][2][1] = cube[1][1][2];
                cube[1][1][2] = cube[4][0][1];
                cube[4][0][1] = temp;

                temp = cube[3][2][0];
                cube[3][2][0] = cube[0][2][2];
                cube[0][2][2] = cube[1][0][2];
                cube[1][0][2] = cube[4][0][0];
                cube[4][0][0] = temp;
            } else if (side == 5) {
                temp = cube[3][2][2];
                cube[3][2][2] = cube[4][2][0];
                cube[4][2][0] = cube[1][0][0];
                cube[1][0][0] = cube[0][0][2];
                cube[0][0][2] = temp;

                temp = cube[3][1][2];
                cube[3][1][2] = cube[4][2][1];
                cube[4][2][1] = cube[1][1][0];
                cube[1][1][0] = cube[0][0][1];
                cube[0][0][1] = temp;

                temp = cube[3][0][2];
                cube[3][0][2] = cube[4][2][2];
                cube[4][2][2] = cube[1][2][0];
                cube[1][2][0] = cube[0][0][0];
                cube[0][0][0] = temp;
            }
            count--;
        }
    }
}
