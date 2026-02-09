import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int[] solution(int[] arr, int k) {
        HashSet<Integer> t = new HashSet<>();
        
        int[] answer = new int[k];
        Arrays.fill(answer, -1);
        for (int i=0, j=0; i<arr.length && j<k; i++) {
            int n = arr[i];
            if (!t.contains(n)) {
                t.add(n);
                answer[j++] = n;
            }
        }
        return answer;
    }
}