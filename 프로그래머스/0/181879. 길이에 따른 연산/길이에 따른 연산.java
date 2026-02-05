class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        if (num_list.length >= 11) {
            int s = 0;
            for (int n : num_list) {
                s += n;
            }
            answer = s;
        } else {
            int m = 1;
            for (int n : num_list) {
                m *= n;
            }
            answer = m;
        }
        
        return answer;
    }
}