import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int n : arr) {
            if (answer.isEmpty()) {
                answer.add(n);
            } else {
                if (answer.get(answer.size() - 1) == n) {
                    answer.remove(answer.size() - 1);
                } else {
                    answer.add(n);
                }
            }
        }
        
        return answer.isEmpty() ? new int[]{-1} : answer.stream().mapToInt(Integer::intValue).toArray();
    }
}