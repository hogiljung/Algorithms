import java.util.*;

class Solution {
    int[] parent;
    
    public int solution(int n, int[][] computers) {
        parent = new int[n];
        
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i <= j || computers[i][j] == 0) continue;

                union(i, j);
            }
        }
        
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < n; i++) {
            set.add(findParent(i));
        }
        
        return set.size();
    }
    
    int findParent(int x) {
        if (parent[x] == x) {
            return x;
        }
        
        return parent[x] = findParent(parent[x]);
    }
    
    void union(int a, int b) {
        int rootA = findParent(a);
        int rootB = findParent(b);
        
        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}