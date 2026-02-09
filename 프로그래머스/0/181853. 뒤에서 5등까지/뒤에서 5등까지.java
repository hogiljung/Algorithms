import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] temp = num_list.clone();
        
        Arrays.sort(temp);
        
        int[] answer = new int[5];
        for (int i=0; i<5; i++) {
            answer[i] = temp[i];
        }
        
        return answer;
    }
}