import java.util.*;

class Solution {
    private int n = 0;
    private int m = 0;
    private int[] dx = new int[]{1, 0, -1, 0};
    private int[] dy = new int[]{0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        n = maps[0].length;
        m = maps.length;
                
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        
        while (!queue.isEmpty()) {
            int[] data = queue.poll();
            int x = data[0];
            int y = data[1];
            
            int move = maps[y][x];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                
                if (maps[ny][nx] != 1) {
                    continue;
                }
                
                if (nx == n-1 && ny == m-1) {
                    return move + 1;
                }
                
                maps[ny][nx] = move + 1;
                queue.offer(new int[]{nx, ny});
            }
        }
        
        return -1;
    }
}