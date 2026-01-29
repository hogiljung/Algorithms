class Solution {
    public int solution(int n) {
        int answer = 0;
        double nSqrt = Math.sqrt(n);
        for (int i=1; i<=nSqrt; i++) {
            if (n % i == 0) {
                answer++;
            }
        }
        
        answer *= 2;
        
        if (Double.compare(Math.ceil(nSqrt), Math.floor(nSqrt)) == 0) {
            answer--;
        }
        
        return answer;
    }
}