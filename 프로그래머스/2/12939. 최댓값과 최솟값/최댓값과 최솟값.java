import java.util.*;

class Solution {
    public String solution(String s) {
        TreeSet<Integer> tree = new TreeSet<>();
        for (String c : s.split(" ")) {
            tree.add(Integer.parseInt(c));
        }
        
        String answer = tree.first() + " " + tree.last();
        return answer;
    }
}