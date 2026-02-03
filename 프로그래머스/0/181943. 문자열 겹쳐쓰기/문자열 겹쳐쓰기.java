class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        char[] m_chars = my_string.toCharArray();
        char[] o_chars = overwrite_string.toCharArray();
        
        for (int i=0; i<o_chars.length; i++) {
            m_chars[s+i] = o_chars[i];
        }
        
        return String.valueOf(m_chars);
    }
}