class Solution {
    public int solution(String myString, String pat) {
        int i = -1;
        int answer = 0;
        while (i < myString.length()) {
            i = myString.indexOf(pat, i+1);
            if (i == -1) {
                break;
            }
            answer++;
        }
        return answer;
    }
}