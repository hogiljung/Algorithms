class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for (char c : my_string.replaceAll("[a-zA-Z]", "").toCharArray()) {
            answer += Integer.parseInt(String.valueOf(c));
        }
        return answer;
    }
}