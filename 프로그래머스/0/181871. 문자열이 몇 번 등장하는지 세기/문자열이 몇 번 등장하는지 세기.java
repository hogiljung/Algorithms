class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        for (int i=0; i<myString.length(); i++) {
            answer += myString.startsWith(pat, i) ? 1 : 0;
        }
        return answer;
    }
}