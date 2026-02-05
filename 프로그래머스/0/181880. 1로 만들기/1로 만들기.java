class Solution {
    public int solution(int[] num_list) {
        int[] t = new int[31];
        for (int i=2; i<t.length; i++) {
            if (i % 2 == 0) {
                t[i] = t[i/2] + 1;
            } else {
                t[i] = t[(i-1)/2] + 1;
            }
        }
        
        int answer = 0;
        for (int n : num_list) {
            answer += t[n];
        }
        return answer;
    }
}