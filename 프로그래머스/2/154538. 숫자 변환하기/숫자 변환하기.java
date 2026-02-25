import java.util.Arrays;

class Solution {
    public int solution(int x, int y, int n) {
        int[] calTb = new int[y + 1];
        int MAX = Integer.MAX_VALUE;
        Arrays.fill(calTb, MAX);
        
        calTb[x] = 0;
        
        for (int i = x; i < y + 1; i++) {
            if (calTb[i] == MAX) {
                continue;
            }
            
            if (i + n <= y) {
                calTb[i + n] = Math.min(calTb[i + n], calTb[i] + 1);
            }
            if (i * 2 <= y) {
                calTb[i * 2] = Math.min(calTb[i * 2], calTb[i] + 1);
            }
            if (i * 3 <= y) {
                calTb[i * 3] = Math.min(calTb[i * 3], calTb[i] + 1);
            }
        }
        
        return calTb[y] == MAX ? -1 : calTb[y];
    }
}