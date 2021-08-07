import java.util.*;

public class Solution {
    public boolean solution(String[] phoneBook){
        HashSet<String> set=new HashSet<>();
        Arrays.stream(phoneBook).forEach(s->set.add(s));

        for(String str:set){
            for(int i=1; i<str.length(); i++){
                if(set.contains(str.substring(0, i))){
                    return false;
                }
            }
        }

        return true;
        
    }

    public static void main(String[] args) {
        String[] test={"119", "9754893","11923849"};
        Solution s=new Solution();
        System.out.println(s.solution(test));
    }
    
}



// 효율성초과
/* public class Solution {
    public boolean solution(String[] phoneBook){
        for(int i=0; i<phoneBook.length-1; i++)
        {
            for(int j=i+1; j<phoneBook.length; j++)
            {
                if(phoneBook[i].startsWith(phoneBook[j])){return false;}
                if(phoneBook[j].startsWith(phoneBook[i])){return false;}
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String[] test={"119", "9754893","11923849"};
        Solution s=new Solution();
        System.out.println(s.solution(test));
    }
    
} */
