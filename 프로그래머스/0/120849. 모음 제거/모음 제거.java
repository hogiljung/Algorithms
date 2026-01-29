import java.util.List;

class Solution {
    public String solution(String my_string) {
        char[] targets = "aeiou".toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : my_string.toCharArray()) {
            boolean isIn = false;
            for (char t : targets) {
                if (t == c) {
                    isIn = true;
                }
            }
            if (isIn) {
                continue;
            }
            sb.append(c);
        }
        return sb.toString();
    }
}