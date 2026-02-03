class Solution {
    public String solution(String code) {
        StringBuilder sb = new StringBuilder();
        int mode = 0;
        for (int i=0; i<code.length(); i++) {
            char c = code.charAt(i);
            if (mode == 0) {
                if (c == '1') {
                    mode = 1;
                } else if (i % 2 == 0) {
                    sb.append(c);
                }
            } else if (mode == 1) {
                if (c == '1') {
                    mode = 0;
                } else if (i % 2 == 1) {
                    sb.append(c);
                }
            }
        }
        
        String answer = sb.length() == 0 ? "EMPTY" : sb.toString();
        return answer;
    }
}