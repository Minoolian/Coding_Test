package baekjoon.binary_graph_1707;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int[] visited;
    static ArrayList<Integer>[] adj;
    static int V;
    static int E;

    static boolean dfs(int cur) {
        for (Integer i : adj[cur]) {
            if (visited[i] != 0 && visited[i]==visited[cur]) return false;
            if (visited[i] == 0) {
                visited[i]=visited[cur]%2 + 1;
                if(!dfs(i)) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;


        for (int k=0; k<t; k++) {
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());

            adj = new ArrayList[V+1];
            for (int j=1; j<V+1; j++) {
                adj[j] = new ArrayList<Integer>();
            }

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int u=Integer.parseInt(st.nextToken());
                int v=Integer.parseInt(st.nextToken());

                adj[u].add(v);
                adj[v].add(u);
            }

            boolean result = true;
            visited = new int[V+1];
            for (int e = 1; e < V + 1; e++) {
                if(visited[e] != 0) continue;
                visited[e]=1;
                if (dfs(e) == false) {
                    result = false;
                    break;
                }
            }
            System.out.println(result ? "YES" : "NO");
        }
    }

}
