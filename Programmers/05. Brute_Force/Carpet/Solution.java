package Carpet;

class Solution {
    public int[] solution(int brown, int yellow) {
        int row=3;

        for(int col=(int)(brown/2)-1; col>2; col--){
            if(col*row-brown == yellow){
                return new int[]{col,row};
            }else{
                row++;
            }
        }

        return new int[0];
    }
}