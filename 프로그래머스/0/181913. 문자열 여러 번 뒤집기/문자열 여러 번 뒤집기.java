class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] temp = my_string.toCharArray();
        for (int[] query : queries) {
            reverse(temp, query[0], query[1]);
        }
        return new String(temp);
    }
    
    private void reverse(char[] c, int i, int j) {
        while (i < j) {
            swap(c, i, j);
            i++;
            j--;
        }
    }
    
    private void swap(char[] c, int i, int j) {
        char t = c[i];
        c[i] = c[j];
        c[j] = t;
    }
}