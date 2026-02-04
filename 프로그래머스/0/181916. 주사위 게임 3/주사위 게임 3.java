import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] dices = {a, b, c, d};
        Arrays.sort(dices);
        int answer = 0;
        
        if (dices[0] == dices[3]) {
            answer = 1111 * dices[3];
        } else if (dices[0] == dices[2] || dices[1] == dices[3]) {
            answer = (int) Math.pow(dices[1] * 10 + (dices[0] + dices[3] - dices[1]), 2);
        } else if (dices[0] == dices[1] && dices[2] == dices[3]) {
            answer = (dices[0] + dices[2]) * Math.abs(dices[0] - dices[2]);
        } else if (dices[0] == dices[1]) {
            answer = dices[2] * dices[3];
        } else if (dices[1] == dices[2]) {
            answer = dices[0] * dices[3];
        } else if (dices[2] == dices[3]) {
            answer = dices[0] * dices[1];
        } else {
            answer = dices[0];
        }
        return answer;
    }
}