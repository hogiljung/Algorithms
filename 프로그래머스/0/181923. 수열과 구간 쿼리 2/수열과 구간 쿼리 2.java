class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        
        for (int j=0; j<queries.length; j++) {
            int[] query = queries[j];
            int min = -1;
            for (int i=query[0]; i<=query[1]; i++) {
                if (query[2] < arr[i]) {
                    min = min == -1 ? arr[i] : Math.min(min, arr[i]);
                }
            }
            answer[j] = min;
        }
        
        return answer;
    }
}