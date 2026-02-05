class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        for (int i=0; i<num_list.length; i++) {
            int j = i;
            if (i < n) {
                j += num_list.length - n;
            } else {
                j -= n;
            }
            answer[j] = num_list[i];
        }
        return answer;
    }
}