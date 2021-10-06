package Travel_route;
import java.util.*;

class Solution {
    Map<String, List<String>> tks=new HashMap<>();
    List<String> answer = new ArrayList<>();

    public String[] solution(String[][] tickets) {
        
        
        Arrays.sort(tickets, new Comparator<String[]>(){
            @Override
            public int compare(String[] o1, String[] o2) {
                if(o1[0].equals(o2[0]))
                    return o1[1].compareTo(o2[1]);
                else
                    return o1[0].compareTo(o2[0]);
            }
        });
        
        for(String[] tic:tickets){
            if(tks.containsKey(tic[0])){
                List<String> list = tks.get(tic[0]);
                list.add(tic[1]);
                tks.put(tic[0], list);
            }
            else{
                tks.put(tic[0], new ArrayList<String>(){
                    {
                        add(tic[1]);
                    }
                });
            }        
        }
    
        dfs("ICN");
        
        Collections.reverse(answer);
        return answer.toArray(new String[0]);
    }

    void dfs(String cur){
        while(tks.containsKey(cur)){
            if(tks.get(cur).isEmpty())
                break;
            List<String> temp = tks.get(cur);
            String remove = temp.remove(0);
            tks.put(cur, temp);
            dfs(remove);
        }

        answer.add(cur);
            
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        s.solution(new String[][]{{"ICN", "SFO"}, {"ICN", "ATL"}, {"SFO", "ATL"}, {"ATL", "ICN"}, {"ATL","SFO"}});
        s.solution(new String[][]{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
    }
}