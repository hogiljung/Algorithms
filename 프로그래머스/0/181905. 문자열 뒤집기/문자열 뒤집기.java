class Solution {
    public String solution(String my_string, int s, int e) {
        char[] chars = my_string.toCharArray();
        while (s < e) {
            char t = chars[s];
            chars[s++] = chars[e];
            chars[e--] = t;
        }
        return new String(chars);
    }
}