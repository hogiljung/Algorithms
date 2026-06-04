import java.util.*;

class Solution {
    int[][] dirs = new int[][]{
        {0, 1}, {1, 0}, {0, -1}, {-1, 0}
    };
    
    public int[] solution(int m, int n, int[][] picture) {
        boolean[][] visited = new boolean[m][n];

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        for (int y = 0; y < m; y++) {
            for (int x = 0; x < n; x++) {
                if (picture[y][x] != 0 && !visited[y][x]) {
                    numberOfArea++;
                    int sizeOfOneArea = bfs(y, x, picture, visited);
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, sizeOfOneArea);
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    int bfs(int y, int x, int[][] picture, boolean[][] visited) {
        int cnt = 1;
        int value = picture[y][x];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{y, x});
        visited[y][x] = true;
        
        while (!q.isEmpty()) {
            int[] now = q.poll();
            
            for (int i = 0; i < dirs.length; i++) {
                int[] dir = dirs[i];
                int ny = now[0] + dir[0];
                int nx = now[1] + dir[1];

                if (ny < 0 || ny >= picture.length || nx < 0 || nx >= picture[0].length) {
                    continue;
                }
                
                if (picture[ny][nx] != value || visited[ny][nx]) {
                    continue;
                }

                q.offer(new int[]{ny, nx});
                visited[ny][nx] = true;
                cnt++;
            }
        }
        
        return cnt;
    }
}