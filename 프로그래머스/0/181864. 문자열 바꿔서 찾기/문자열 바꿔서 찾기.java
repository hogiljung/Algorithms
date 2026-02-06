class Solution {
    public int solution(String myString, String pat) {
        StringBuilder sb = new StringBuilder();
        for (char c : myString.toCharArray()) {
            char cc = c;
            if (c == 'A') {
                cc = 'B';
            } else if (c == 'B') {
                cc = 'A';
            }
            sb.append(cc);
        }
        
        String s = sb.toString();
        
        int answer = s.contains(pat) ? 1 : 0;
        return answer;
    }
}