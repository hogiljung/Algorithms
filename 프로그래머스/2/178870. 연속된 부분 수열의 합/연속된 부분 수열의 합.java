class Solution {
    public int[] solution(int[] sequence, int k) {
        int left = 0, right = 0;
        int minLength = sequence.length;
        int[] answer = new int[2];
        int sum = sequence[0];
        
        while (right < sequence.length) {
            int compare = Integer.compare(sum, k);
            if (compare < 0) {
                right++;
                if (right >= sequence.length) {
                    break;
                }
                sum += sequence[right];
            } else {
                if (compare == 0) {
                    int length = right - left;
                    if (length < minLength) {
                        minLength = length;
                        answer[0] = left;
                        answer[1] = right;
                    }
                }
                
                sum -= sequence[left++];
            }
        }
        
        return answer;
    }
}