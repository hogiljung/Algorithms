import java.util.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        return dfs(k, dungeons);
    }
    
    private int dfs(int k, int[][] dungeons) {
        int count = 0;
        
        for (int[] dungeon: dungeons) {
            int required = dungeon[0];
            if (k >= dungeon[0]) {
                dungeon[0] = 5001;
                count = Math.max(dfs(k - dungeon[1], dungeons) + 1, count);
                dungeon[0] = required;
            }
        }
        
        return count;
    }
}