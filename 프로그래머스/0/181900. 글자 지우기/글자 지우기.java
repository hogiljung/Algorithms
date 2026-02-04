class Solution {
    public String solution(String my_string, int[] indices) {
        boolean[] t = new boolean[my_string.length()];
        for(int indice : indices) {
            t[indice] = true;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<my_string.length(); i++) {
            if (!t[i]) {
                sb.append(my_string.charAt(i));
            }
        }
        
        return sb.toString();
    }
}