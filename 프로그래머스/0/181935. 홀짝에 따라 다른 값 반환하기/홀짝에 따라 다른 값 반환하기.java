class Solution {
    public int solution(int n) {
        int answer = 0;
        
        if (n % 2 == 0) {
            int k = n / 2;
            answer = 4 * k * (k + 1) * (2 * k + 1) / 6;
        } else {
            int k = (n + 1) / 2;
            answer = k * k;
        }
        
        return answer;
    }
}