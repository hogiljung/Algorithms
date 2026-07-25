import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        
        for (int i = 0; i < wires.length; i++) {
            List<Integer>[] graph = new ArrayList[n+1];
            
            for (int j = 0; j <= n; j++) {
                graph[j] = new ArrayList<>();
            }
            
            for (int j = 0; j < wires.length; j++) {
                if (i == j) continue;
                
                int[] wire = wires[j];
                graph[wire[0]].add(wire[1]);
                graph[wire[1]].add(wire[0]);
            }
            
            boolean[] visited = new boolean[n+1];
            
            int count = 0;
            
            for (int j = 1; j <= n; j++) {
                if (visited[j]) continue;
                
                count = dfs(graph, visited, j);
            }
            
            answer = Math.min(answer, Math.abs(count - (n - count)));
        }

        return answer;
    }
    
    private int dfs(List<Integer>[] graph, boolean[] visited, int start) {
        visited[start] = true;
        int count = 1;
        
        for (int node: graph[start]) {
            if (visited[node]) continue;
            
            count += dfs(graph, visited, node);
        }
        
        return count;
    }
}