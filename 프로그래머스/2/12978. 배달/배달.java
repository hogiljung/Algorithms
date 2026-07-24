import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        List<Edge>[] graph = new ArrayList[N + 1];
        
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] r: road) {
            graph[r[0]].add(new Edge(r[1], r[2]));
            graph[r[1]].add(new Edge(r[0], r[2]));
        }
        
        int[] distance = dijkstra(graph, 1);
        
        int answer = 0;
        
        for (int d: distance) {
            if (d <= K) {
                answer++;
            }
        }

        return answer;
    }
    
    class Edge {
        int to;
        int cost;
        
        Edge(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }
    
    class Node {
        int vertex;
        int distance;
        
        Node(int vertex, int distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
    }
    
    private int[] dijkstra(List<Edge>[] graph, int start) {
        int n = graph.length;
        int[] distance = new int[n];
            
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        
        PriorityQueue<Node> queue = new PriorityQueue<>(
            Comparator.comparingInt(node -> node.distance)
        );
    
        queue.offer(new Node(start, 0));
        
        while (!queue.isEmpty()) {
            Node current = queue.poll();
            
            int currentVertex = current.vertex;
            int currentDistance = current.distance;
            
            if (currentDistance > distance[currentVertex])
                continue;
            
            for (Edge edge: graph[currentVertex]) {
                int next = edge.to;
                int newDistance = currentDistance + edge.cost;
                
                if (newDistance < distance[next]) {
                    distance[next] = newDistance;
                    queue.offer(new Node(next, newDistance));
                }
            }
        }
        
        return distance;
    }
}