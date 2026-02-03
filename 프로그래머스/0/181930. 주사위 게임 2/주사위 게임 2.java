class Solution {
    public int solution(int a, int b, int c) {
        int temp = a + b + c;
        
        if (a == b || b == c || a == c) {
            temp *= a * a + b * b + c * c;
        }
        
        if (a == b && b == c) {
            temp *= a * a * a + b * b * b + c * c * c;
        }
        
        int answer = temp;
        return answer;
    }
}