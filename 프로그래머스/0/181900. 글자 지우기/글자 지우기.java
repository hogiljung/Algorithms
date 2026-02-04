class Solution {
    public String solution(String my_string, int[] indices) {
        String[] tmp = my_string.split("");
        for(int i : indices) {
            tmp[i] = "";
        }
        return String.join("", tmp);
    }
}