class Solution {
    public int[] solution(int[] num_list) {
        int N = num_list.length;
        int[] answer = new int[N];
        for (int i=0; i<N; i++) {
            answer[i] = num_list[N-1-i];
        }
        return answer;
    }
}