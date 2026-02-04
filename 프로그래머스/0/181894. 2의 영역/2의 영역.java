class Solution {
    public int[] solution(int[] arr) {
        int s=-1, e=-1;
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == 2) {
                if (s == -1) {
                    s = i;
                }
                e = i;
            }
        }
        
        int[] answer;
        if (s != -1) {
            answer = new int[e-s+1];
            
            for (int i=0, j=s; j<=e; j++) {
                answer[i++] = arr[j];
            }
        } else {
            answer = new int[]{-1};
        }
        return answer;
    }
}