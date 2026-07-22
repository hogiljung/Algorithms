import java.util.*;

class Solution {
    public int solution(int[] order) {
        Deque<Integer> stack = new ArrayDeque<>();
        int count = 0;
        
        for (int nextNum = 1; nextNum <= order.length; nextNum++) {
            if (nextNum == order[count]) {
                count++;
            } else {
                stack.push(nextNum);
            }
            
            while (!stack.isEmpty() && stack.peek() == order[count]) {
                stack.pop();
                count++;
            }
        }
        
        return count;
    }
}