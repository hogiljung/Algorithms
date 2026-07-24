import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        List<Integer>[] map = new ArrayList[n];
        int[] distance = new int[n];
        
        for (int i = 0; i < n; i++) {
            map[i] = new ArrayList<>();
        }
        
        Arrays.fill(distance, -1);
        
        for (int[] road : roads) {
            map[road[0] - 1].add(road[1] - 1);
            map[road[1] - 1].add(road[0] - 1);
        }
        
        bfs(map, distance, destination - 1);
        
        int[] answer = new int[sources.length];
        
        for (int i = 0; i < sources.length; i++) {
            int source = sources[i];
            answer[i] = distance[source - 1];
        }
        
        return answer;
    }
    
    private void bfs(List<Integer>[] map, int[] distance, int start) {
        Queue<Integer> queue = new ArrayDeque<>();
        distance[start] = 0;
        queue.offer(start);
        
        while (!queue.isEmpty()) {
            int s = queue.poll();
            
            for (int d : map[s]) {
                if (distance[d] != -1)
                    continue;
                
                distance[d] = distance[s] + 1;
                queue.offer(d);
            }
        }
    }
}