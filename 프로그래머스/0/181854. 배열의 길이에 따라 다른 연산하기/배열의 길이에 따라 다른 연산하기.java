class Solution {
    public int[] solution(int[] arr, int n) {
        int[] answer = arr.clone();
        
        int i = 0;
        if (answer.length % 2 == 0) {
            i++;
        }
        
        while (i < answer.length) {
            answer[i] += n;
            i += 2;
        }
        
        return answer;
    }
}