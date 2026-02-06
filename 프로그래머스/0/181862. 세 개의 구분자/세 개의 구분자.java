import java.util.Arrays;

class Solution {
    public String[] solution(String myStr) {
        String[] temp = myStr.replaceAll("[abc]+", " ").split("\\s+");
        
        if (temp.length > 0) {
            if (temp[0].isEmpty()) {
                if (temp.length > 1) {
                    temp = Arrays.copyOfRange(temp, 1, temp.length);
                } else {
                    temp = new String[1];
                    temp[0] = "EMPTY";
                }
            }
        } else {
            temp = new String[1];
            temp[0] = "EMPTY";
        }
        
        String[] answer = temp;
        return answer;
    }
}