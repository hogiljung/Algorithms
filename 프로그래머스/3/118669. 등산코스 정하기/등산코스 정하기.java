import java.util.*;

class Solution {
    class Edge {
        int to;
        int weight;
        
        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }
    
    class Node implements Comparable<Node> {
        int number;
        int intensity;
        
        Node(int number, int intensity) {
            this.number = number;
            this.intensity = intensity;
        }
        
        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.intensity, other.intensity);
        }
    }
    
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        List<Edge>[] graph = new ArrayList[n+1];
        
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] path : paths) {
            int a = path[0];
            int b = path[1];
            int weight = path[2];

            graph[a].add(new Edge(b, weight));
            graph[b].add(new Edge(a, weight));
        }

        boolean[] isGate = new boolean[n + 1];
        boolean[] isSummit = new boolean[n + 1];

        for (int gate : gates) {
            isGate[gate] = true;
        }

        for (int summit : summits) {
            isSummit[summit] = true;
        }

        int[] intensity = new int[n + 1];
        Arrays.fill(intensity, Integer.MAX_VALUE);

        PriorityQueue<Node> pq = new PriorityQueue<>();

        for (int gate : gates) {
            intensity[gate] = 0;
            pq.offer(new Node(gate, 0));
        }
        
        while (!pq.isEmpty()) {
            Node current = pq.poll();
            
            int currentNumber = current.number;
            int currentIntensity = current.intensity;
            
            if (currentIntensity > intensity[currentNumber])
                continue;
            
            if (isSummit[currentNumber])
                continue;
            
            for (Edge edge: graph[currentNumber]) {
                int nextNode = edge.to;
                
                if (isGate[nextNode])
                    continue;
                
                int nextIntensity =
                        Math.max(currentIntensity, edge.weight);

                if (nextIntensity < intensity[nextNode]) {
                    intensity[nextNode] = nextIntensity;
                    pq.offer(new Node(nextNode, nextIntensity));
                }
            }
        }
        
        Arrays.sort(summits);
        
        int selectedSummit = 0;
        int minimumIntensity = Integer.MAX_VALUE;

        for (int summit : summits) {
            if (intensity[summit] < minimumIntensity) {
                selectedSummit = summit;
                minimumIntensity = intensity[summit];
            }
        }

        return new int[]{selectedSummit, minimumIntensity};
    }
}