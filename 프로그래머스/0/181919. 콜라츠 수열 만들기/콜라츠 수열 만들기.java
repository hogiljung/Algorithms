import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        int temp = n;
        while (temp >= 1) {
            answer.add(temp);
            if (temp == 1) {
                break;
            } else if (temp % 2 == 0) {
                temp /= 2;
            } else {
                temp = 3 * temp + 1;
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}