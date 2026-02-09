import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = num_list.clone();
        
        Arrays.sort(answer);
        
        return Arrays.copyOfRange(answer, 5, answer.length);
    }
}