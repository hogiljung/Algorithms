class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(my_string);
        
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            
            for (int i=0; i<=(e-s)/2; i++) {
                int i1 = s+i;
                int i2 = e-i;
                char temp = sb.charAt(i1);
                sb.setCharAt(i1, sb.charAt(i2));
                sb.setCharAt(i2, temp);
            }
        }
        String answer = sb.toString();
        return answer;
    }
}