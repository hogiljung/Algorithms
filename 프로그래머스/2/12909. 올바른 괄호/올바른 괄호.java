import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (Character c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else {
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        
        if (!stack.isEmpty()) {
            return false;
        }
        
        return true;
    }
}