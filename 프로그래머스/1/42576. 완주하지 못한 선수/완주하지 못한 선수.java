import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> pMap = new HashMap<>();
        for (String p : participant) {
            pMap.put(p, pMap.getOrDefault(p, 0) + 1);
        }
        
        for (String c : completion) {
            if (pMap.containsKey(c)) {
                int cnt = pMap.get(c);
                if (cnt == 1) {
                    pMap.remove(c);
                } else {
                    pMap.put(c, cnt - 1);
                }
            }
        }
        
        String answer = pMap.keySet().iterator().next();
        return answer;
    }
}