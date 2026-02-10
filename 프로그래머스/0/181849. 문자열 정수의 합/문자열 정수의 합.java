class Solution {
    public int solution(String num_str) {
        String[] numbers = num_str.split("");
        
        int answer = 0;
        for (String num : numbers) {
            answer += Integer.parseInt(num);
        }
        return answer;
    }
}