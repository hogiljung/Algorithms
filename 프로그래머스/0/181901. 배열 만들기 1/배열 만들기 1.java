class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[n/k];
        for (int i=0; (i+1)*k<=n; i++) {
            answer[i] = (i+1)*k;
        }
        return answer;
    }
}