import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] rolls = {a, b, c, d};
        HashMap<Integer, Integer> rollCnt = new HashMap<>();
        for (int roll : rolls) {
            rollCnt.put(roll, rollCnt.getOrDefault(roll, 0) + 1);
        }
        
        ArrayList<Integer> distRolls = new ArrayList<>(rollCnt.keySet());
        int distRollCnt = rollCnt.size();
        int answer = 0;
        if (distRollCnt == 1) {
            answer = a * 1111;
        } else if (distRollCnt == 2) {
            int cnt = rollCnt.get(distRolls.get(0));
            if (cnt == 2) {
                int p = distRolls.get(0);
                int q = distRolls.get(1);
                answer = (p + q) * Math.abs(p - q);
            } else {
                int p = cnt == 3 ? distRolls.get(0) : distRolls.get(1);
                int q = cnt == 3 ? distRolls.get(1) : distRolls.get(0);
                answer = (10 * p + q) * (10 * p + q);
            }
        } else if (distRollCnt == 3) {
            answer = 1;
            for (int roll : distRolls) {
                if (rollCnt.get(roll) == 1) {
                    answer *= roll;
                }
            }
        } else {
            answer = distRolls.stream()
                .min(Integer::compareTo)
                .get();
        }
        
        return answer;
    }
}