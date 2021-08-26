package Find_Prime;
import java.util.*;

class Solution {
    public int solution(String numbers) {
        int answer = 0;
        boolean[] era=new boolean[10000000];
        HashSet<Integer> check=new HashSet<>();

        Arrays.fill(era, true);
        era[0]=false;
        era[1]=false;

        for(int i=2; i<(int)Math.sqrt(10000000)+1; i++){
            if(era[i]){
                for(int j=i+i; j<10000000; j+=i){
                    era[j]=false;
                }
            }
        }
        permutation("", numbers, check);
        Iterator<Integer> iterator = check.iterator();
        while(iterator.hasNext()){
            int a=iterator.next();
            if(era[a]) answer+=1;
        }
        
        return answer;
    }

    public void permutation(String prefix, String str, HashSet<Integer> check){
        if(!prefix.equals("")) check.add(Integer.valueOf(prefix));
        for(int i=0; i<str.length(); i++){
            permutation(prefix+str.charAt(i), str.substring(0, i)+str.substring(i+1, str.length()), check);
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        System.out.println(s.solution("17"));
    }
}