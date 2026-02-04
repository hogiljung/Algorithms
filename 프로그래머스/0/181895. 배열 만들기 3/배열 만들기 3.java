class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        int answerLength = 0;
        for (int[] interval : intervals) {
            answerLength += interval[1] - interval[0] + 1;
        }
        
        int[] answer = new int[answerLength];
        int i=0;
        for (int[] interval : intervals) {
            for (int j=interval[0]; j<=interval[1]; j++) {
                answer[i++] = arr[j];
            }
        }
        
        return answer;
    }
}