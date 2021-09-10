package Island;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0, e=0;
        Arrays.sort(costs, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2) {
                // TODO Auto-generated method stub
                return o1[2]-o2[2];
            }
        });

        // Arrays.sort(costs, (a,b)->Integer.compare(a[2], b[2]));

        int[] parent=new int[n];
        for(int i=0; i<n; i++){
            parent[i]=i;
        }
        
        for(int[] temp: costs){
            if(find(parent,temp[0])!=find(parent,temp[1])){
                union(parent,temp[0],temp[1]);
                answer+=temp[2];
                e+=1;
            }

            if(e==n-1){
                break;
            }
        }
        
        return answer;
    }

    public int find(int[] parent, int x){
        if(parent[x]==x){
            return x;
        }

        return find(parent,parent[x]);
    }

    public void union(int[] parent, int x, int y){
        int a=find(parent,x);
        int b=find(parent,y);

        if(a!=b){
            parent[b]=a;
        }
    }

    public static void main(String[] args) {
        Solution s=new Solution();
        int n=4;
        int[][] c={{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};

        System.out.print(s.solution(n, c));
    }
}