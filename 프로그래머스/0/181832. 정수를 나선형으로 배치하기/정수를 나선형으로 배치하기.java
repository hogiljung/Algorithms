class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int d = 0;
        int x = 0, y = 0;
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        
        for (int i=1; i<=n*n; i++) {
            answer[y][x] = i;
            
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || answer[ny][nx] != 0) {
                d = (d + 1) % 4;
                nx = x + dx[d];
                ny = y + dy[d];
            }
            
            x = nx;
            y = ny;
        }
        
        
        return answer;
    }
}