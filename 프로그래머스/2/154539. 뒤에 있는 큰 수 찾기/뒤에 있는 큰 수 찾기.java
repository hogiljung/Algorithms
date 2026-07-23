import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] answer = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty()) {
                if (stack.peek() > numbers[i]) {
                    answer[i] = stack.peek();
                    stack.push(numbers[i]);
                    break;
                } else {
                    stack.pop();
                }
            }
            
            if (stack.isEmpty()) {
                answer[i] = -1;
                stack.push(numbers[i]);
            }
        }
        
        return answer;
    }
}