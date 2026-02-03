class Solution {
    public String solution(String str1, String str2) {
        char[] s1Chars = str1.toCharArray();
        char[] s2Chars = str2.toCharArray();
        
        char[] answer = new char[s1Chars.length + s2Chars.length];
        for (int i=0; i<s1Chars.length; i++) {
            answer[i*2] = s1Chars[i];
            answer[i*2+1] = s2Chars[i];
        }
        
        return String.valueOf(answer);
    }
}