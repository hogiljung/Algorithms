class Solution {
    public int solution(int a, int b) {
        String aStr = String.valueOf(a);
        String bStr = String.valueOf(b);
        
        int ab = Integer.parseInt(aStr + bStr);
        int ba = Integer.parseInt(bStr + aStr);
        
        int answer = Math.max(ab, ba);
        return answer;
    }
}