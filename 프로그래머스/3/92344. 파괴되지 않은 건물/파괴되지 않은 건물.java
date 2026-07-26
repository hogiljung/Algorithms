class Solution {
    public int solution(int[][] board, int[][] skill) {
        int w = board[0].length;
        int h = board.length;
        
        int[][] diff = new int[h+1][w+1];
        
        for (int[] s : skill) {
            int degree = s[0] == 1 ? -s[5] : s[5];
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            
            diff[r1][c1] += degree;
            diff[r1][c2+1] -= degree;
            diff[r2+1][c1] -= degree;
            diff[r2+1][c2+1] += degree;
        }
        
        for (int r = 0; r < h; r++) {
            int sum = 0;
                
            for (int c = 0; c < w; c++) {
                sum += diff[r][c];
                diff[r][c] = sum;
            }
        }
        
        for (int c = 0; c < w; c++) {
            int sum = 0;
                
            for (int r = 0; r < h; r++) {
                sum += diff[r][c];
                diff[r][c] = sum;
            }
        }
        
        int count = 0;
        for (int r = 0; r < h; r++) {
            for (int c = 0; c < w; c++) {
                if (board[r][c] + diff[r][c] > 0) {
                    count++;
                }
            }
        }
        
        return count;
    }
}