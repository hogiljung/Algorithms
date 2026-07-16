import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        Set<String> set = new HashSet<>();
        
        int[] answer = new int[]{0, 0};
        char prev = ' ';
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if ((prev != ' ' && prev != word.charAt(0))
                || set.contains(word)) {
                int num = (i + 1) % n;
                if (num == 0) {
                    num = n;
                }
                answer[0] = num;
                
                answer[1] = i / n + 1;
                
                break;
            }
            set.add(word);
            prev = word.charAt(word.length() - 1);
        }
        
        return answer;
    }
}