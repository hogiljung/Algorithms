import java.util.*;

class Solution {
    int n = 0;
    int m = 0;
    int[] dx = new int[]{1, 0, -1, 0};
    int[] dy = new int[]{0, 1, 0, -1};
    
    public int solution(String[] maps) {
        int[] start = {};
        int[] lever = {};
        int[] end = {};
        
        n = maps[0].length();
        m = maps.length;
        
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                switch (maps[y].charAt(x)) {
                    case 'S' -> start = new int[]{x, y};
                    case 'L' -> lever = new int[]{x, y};
                    case 'E' -> end = new int[]{x, y};
                }
            }
        }
        
        int timeToLever = bfs(maps, start, lever);
        
        if (timeToLever == -1)
            return -1;
        
        int timeToEnd = bfs(maps, lever, end);
        
        if (timeToEnd == -1)
            return -1;
        
        return timeToLever + timeToEnd;
    }
    
    private int bfs(String[] maps, int[] start, int[] end) {
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        
        visited[start[1]][start[0]] = true;
        queue.offer(new int[]{start[0], start[1], 0});
        
        while (!queue.isEmpty()) {
            int[] data = queue.poll();
            
            int x = data[0];
            int y = data[1];
            int time = data[2];
            
            if (end[0] == x && end[1] == y) {
                return time; 
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                
                if (visited[ny][nx] || maps[ny].charAt(nx) == 'X')
                    continue;
                
                visited[ny][nx] = true;
                queue.offer(new int[]{nx, ny, time + 1});
            }
        }
        
        return -1;
    }
}