import java.util.ArrayDeque;

class Solution {
    public int[] solution(int[] arr) {
        ArrayDeque<Integer> answer = new ArrayDeque<>();
        
        for (int n : arr) {
            if (!answer.isEmpty() && answer.peekLast() == n) {
                answer.pollLast();
            } else {
                answer.addLast(n);
            }
        }
        
        return answer.isEmpty() ? new int[]{-1} : answer.stream().mapToInt(Integer::intValue).toArray();
    }
}