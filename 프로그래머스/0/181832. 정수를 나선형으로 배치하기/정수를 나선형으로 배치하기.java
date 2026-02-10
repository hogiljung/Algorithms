class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int num = 1, start = 0, end = n-1;
        
        while (num <= n * n) {
            for (int i=start; i<=end; i++) {
                answer[start][i] = num++;
            }
            for (int i=start+1; i<=end; i++) {
                answer[i][end] = num++;
            }
            for (int i=end-1; i>=start; i--) {
                answer[end][i] = num++;
            }
            for (int i=end-1; i>=start+1; i--) {
                answer[i][start] = num++;
            }
            start++;
            end--;
        }
        
        return answer;
    }
}