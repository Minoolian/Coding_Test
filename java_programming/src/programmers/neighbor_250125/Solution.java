package programmers.neighbor_250125;

class Solution {
    int[] dh = new int[]{0, 1, -1, 0};
    int[] dw = new int[]{1, 0, 0, -1};

    public int solution(String[][] board, int h, int w) {
        int count = 0;

        for(int i=0; i<4; i++){
            int nh = h + dh[i];
            int nw = w + dw[i];

            if(nh<0 || nh>=board.length || nw<0 || nw>=board[0].length) continue;
            count += board[nh][nw].equals(board[h][w]) ? 1 : 0;
        }

        return count;
    }
}