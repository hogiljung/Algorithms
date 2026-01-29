class Solution {
    public String solution(String my_string, String letter) {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<my_string.length(); i++) {
            String s = my_string.substring(i,i+1);
            if (s.compareTo(letter) == 0) {
                continue;
            }
            sb.append(s);
        }
        return sb.toString();
    }
}