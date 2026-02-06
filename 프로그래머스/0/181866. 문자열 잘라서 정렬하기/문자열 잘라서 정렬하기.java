import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        String[] answer = myString.split("x+");
        if (answer[0].isEmpty()) {
            if (answer.length > 1) {
                answer = Arrays.copyOfRange(answer, 1, answer.length); 
            } else {
                answer = new String[0];
            }
        }
        Arrays.sort(answer);
        return answer;
    }
}