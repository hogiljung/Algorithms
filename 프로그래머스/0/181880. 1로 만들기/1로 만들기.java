class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for (int n : num_list) {
            answer += Integer.toBinaryString(n).length() - 1;
        }
        return answer;
    }
}