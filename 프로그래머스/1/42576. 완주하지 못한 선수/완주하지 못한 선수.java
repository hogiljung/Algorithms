import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        for (String s : completion) {
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        
        String answer = "";
        for (String s : participant) {
            int cnt = map.getOrDefault(s, 0);
            if (Integer.compare(cnt, 0) == 0) {
                answer = s;
                break;
            }
            map.put(s, cnt - 1);
        }
        
        return answer;
    }
}