package Translate;
import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {

        if(!Arrays.asList(words).contains(target))
            return 0;
        
        Map<String, Boolean> visit=new HashMap<>();
        for(String w:words)
            visit.put(w, true);
        
        List<Temp> q=new ArrayList<>();
        q.add(new Temp(0, begin));

        while(!q.isEmpty()){
            Temp t=q.remove(0);
            if(target.equals(t.word))
                return t.idx;
            
            for(String ww:words){
                if(visit.get(ww) && match(t.word, ww)==1){
                    visit.put(ww, false);
                    q.add(new Temp(t.idx+1, ww));
                }
            }
        }

        return 0;
    }

    public int match(String w, String ww){
        int answer=0;

        for(int i=0; i<w.length(); i++){
            if(w.charAt(i)!=ww.charAt(i))
                answer++;
        }

        return answer;
    }

    class Temp{
        int idx;
        String word;

        Temp(int idx, String word){
            this.idx=idx;
            this.word=word;
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();

        s.solution("hit", "cog", new String[]{"hot", "dot", "dog", "lot", "log", "cog"});
    }
}