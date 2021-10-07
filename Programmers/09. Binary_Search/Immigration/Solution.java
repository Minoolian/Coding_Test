package Immigration;
import java.util.*;

class Solution {
    public long solution(int n, int[] times) {

        long left=0, right=(long)times[times.length-1]*n;

        while(left<right){
            long mid=(left+right)/2;
            long nn=Arrays.stream(times).mapToLong(s->mid/s).sum();

            if(nn>=n) right=mid;
            else left=mid+1;
        }
        return left;
    }
}