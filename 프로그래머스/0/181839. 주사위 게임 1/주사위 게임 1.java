class Solution {
    public int solution(int a, int b) {
        boolean isAEven = a % 2 == 0;
        boolean isBEven = b % 2 == 0;
        
        if (isAEven && isBEven) {
            return Math.abs(a - b);
        } else if (!isAEven && !isBEven) {
            return a * a + b * b;
        } else {
            return 2 * (a + b);
        }
    }
}