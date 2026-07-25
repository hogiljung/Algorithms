import java.util.*;

class Solution {
    String[] alpha = new String[]{"A", "E", "I", "O", "U"};
    Map<String, Integer> dict = new HashMap<>();
    
    public int solution(String word) {
        addWord(new StringBuilder());
        
        int answer = dict.get(word);
        return answer;
    }
    
    private void addWord(StringBuilder sb) {
        if (sb.length() == 5)
            return;
        
        for (int i = 0; i < 5; i++) {
            sb.append(alpha[i]);
            dict.put(sb.toString(), dict.size() + 1);
            addWord(sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}