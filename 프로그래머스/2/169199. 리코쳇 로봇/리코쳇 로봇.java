import java.util.*;

class Solution {
    int[][] dirs = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    
    public int solution(String[] board) {
        int n = board[0].length();
        int m = board.length;
        
        int startX = 0;
        int startY = 0;
        
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (board[y].charAt(x) == 'R') {
                    startX = x;
                    startY = y;
                    break;
                }
            }
        }
        
        int[][] distance = new int[m][n];
        for (int[] row : distance) {
            Arrays.fill(row, -1);
        }
        
        Queue<int[]> queue = new ArrayDeque<>();
        
        distance[startY][startX] = 0;
        queue.offer(new int[]{startX, startY});
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0];
            int y = cur[1];
            
            if (board[y].charAt(x) == 'G')
                return distance[y][x];
            
            for (int[] dir : dirs) {
                int nx = x;
                int ny = y;
                
                while (true) {
                    int nextX = nx + dir[0];
                    int nextY = ny + dir[1];
                    
                    if (!isMovable(board, nextX, nextY)) 
                        break;
                    
                    nx = nextX;
                    ny = nextY;
                }
                
                if (x == nx && y == ny) 
                    continue;
                
                if (distance[ny][nx] != -1)
                    continue;
                
                distance[ny][nx] = distance[y][x] + 1;
                queue.offer(new int[]{nx, ny});
            }
        }
        
        return -1;
    }
    
    private boolean isMovable(String[] board, int x, int y) {
        return x >= 0
            && x < board[0].length()
            && y >= 0
            && y < board.length
            && board[y].charAt(x) != 'D';
    }
}