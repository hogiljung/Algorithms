class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        for (int n : arr) {
            int cnt = 0;
            int curr = n;
            while (true) {
                if (curr >= 50 && curr % 2 == 0) {
                    curr /= 2;                
                    cnt++;
                } else if (curr < 50 && curr % 2 == 1) {
                    curr = curr * 2 + 1;                
                    cnt++;
                } else {
                    break;
                }
            }
            answer = Math.max(answer, cnt);
        }
        return answer;
    }
}