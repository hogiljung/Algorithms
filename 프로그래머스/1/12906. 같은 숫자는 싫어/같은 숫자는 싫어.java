import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int prev = -1;
        List<Integer> answer = new ArrayList<>();
        
        for (int num : arr) {
            if (prev != num) {
                answer.add(num);
                prev = num;
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}