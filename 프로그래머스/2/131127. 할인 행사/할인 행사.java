import java.util.HashMap;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> wMap = new HashMap<>();
        for (int i=0; i<want.length; i++) {
            wMap.put(want[i], number[i]);
        }
        
        int answer = 0;
        for (int i = 0; i <= discount.length-10; i++) {
            HashMap<String, Integer> dMap = new HashMap<>();
            for (int j = i; j < i+10; j++) {
                String d = discount[j];
                dMap.put(d, dMap.getOrDefault(d, 0) + 1);
            }
            
            if (wMap.equals(dMap)) {
                answer++;
            }
        }
        
        return answer;
    }
}