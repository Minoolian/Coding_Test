package Best_Album;

import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(String[] genres, int[] plays) {

        HashMap<String,Integer> gen=new HashMap<>();
        HashMap<String,Object> play=new HashMap<>();

        for(int i=0; i<genres.length; i++){
            String key=genres[i];
            HashMap<Integer, Integer> infoMap;

            if(play.containsKey(key)){
                infoMap=(HashMap<Integer,Integer>)play.get(key);
            }
            else{
                infoMap=new HashMap<>();
            }

            infoMap.put(i,plays[i]);
            play.put(key, infoMap);

            if(gen.containsKey(key)){
                gen.put(key, gen.get(key)+plays[i]);
            }else{
                gen.put(key,plays[i]);
            }
        }
        
        List<String> keyList=new ArrayList<>(gen.keySet());
        Collections.sort(keyList,new Comparator<String>(){
            @Override
            public int compare(String o1, String o2) {
                 int v1=gen.get(o1);
                 int v2=gen.get(o2);

                 return v2-v1;
            }
        });

        System.out.println(keyList.toString());
        List<Integer> temp=new ArrayList<>();
        for(String g:keyList){
            HashMap<Integer, Integer> p=(HashMap<Integer, Integer>)play.get(g);
            List<Integer> key=new ArrayList<>(p.keySet());
            Collections.sort(key,new Comparator<Integer>(){
                @Override
                public int compare(Integer o1, Integer o2) {
                     int v1=p.get(o1);
                     int v2=p.get(o2);
    
                     if(v2>v1){
                         return 1;
                     }else if(v2==v1){
                         return o1-o2;
                     }else{
                         return -1;
                     }
                }
            });

            temp.addAll(key.stream().limit(2).collect(Collectors.toList()));
            
        }
        System.out.println(temp.toString());
        
        return temp.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        String[] g={"classic", "pop", "classic", "classic", "pop"};
        int[] p={500, 600, 150, 800, 2500}; 

        s.solution(g,p);
    }
}