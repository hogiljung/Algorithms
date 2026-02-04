class Solution {
    // my_strings를 순회
    // my_string substring
    // 이어붙임
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<my_strings.length; i++) {
            String s = my_strings[i];
            int[] part = parts[i];
            sb.append(s.substring(part[0], part[1]+1));
        }
        return sb.toString();
    }
}