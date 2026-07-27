import java.util.*;

class Solution {
    static class Edge implements Comparable<Edge> {
        int cost;
        int to;
        int from;
        
        Edge(int cost, int to, int from) {
            this.cost = cost;
            this.to = to;
            this.from = from;
        }
        
        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.cost, other.cost);
        }
    }
    
    private int[] parent;
    
    public int solution(int n, int[][] costs) {
        parent = new int[n];
        
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        PriorityQueue<Edge> pq = new PriorityQueue<>();
        
        for (int[] cost : costs) {
            pq.offer(new Edge(cost[2], cost[0], cost[1]));
        }
        
        int answer = 0;
        
        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            
            if (findParent(edge.to) != findParent(edge.from)) {
                union(edge.to, edge.from);
                answer += edge.cost;
            }
        }
        
        return answer;
    }
    
    private int findParent(int x) {
        if (parent[x] == x) {
            return x;
        }
        
        return parent[x] = findParent(parent[x]);
    }
    
    private void union(int a, int b) {
        int rootA = findParent(a);
        int rootB = findParent(b);
        
        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}