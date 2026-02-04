class Solution {
    public String solution(int q, int r, String code) {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i*q+r<code.length(); i++) {
            sb.append(code.charAt(i*q+r));
        }
        return sb.toString();
    }
}