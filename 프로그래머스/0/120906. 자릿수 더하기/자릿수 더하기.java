class Solution {
    public int solution(int n) {
        if (n == 0) {
            return 0;
        }
        int answer = n % 10;
        return answer + solution(n/10);
    }
}