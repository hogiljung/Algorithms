import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String s : completion) {
            if (!map.containsKey(s)) {
                map.put(s, 1);
            } else {
                map.put(s, map.get(s)+1);
            }
        }
        
        String answer = "";
        for (String s : participant) {
            if (map.containsKey(s)) {
                int cnt = map.get(s);
                if (Integer.compare(cnt, 0) == 0) {
                    answer = s;
                    break;
                }
                map.put(s, cnt-1);
            } else {
                answer = s;
                break;
            }
        }
        
        return answer;
    }
}