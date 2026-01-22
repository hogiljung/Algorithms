import java.util.HashMap;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String, Integer> wMap = new HashMap<>();
        for (int i=0; i<want.length; i++) {
            wMap.put(want[i], number[i]);
        }
        
        HashMap<String, Integer> dMap = new HashMap<>();
        for (int i=0; i<10; i++) {
            String d = discount[i];
            dMap.put(d, dMap.getOrDefault(d, 0) + 1);
        }
        
        int left = 0;
        int right = 9;
        int answer = 0;
        while (right < discount.length) {
            if (wMap.equals(dMap)) {
                answer++;
            }
            
            right++;
            if (right == discount.length) {
                break;
            }
            String d1 = discount[right];
            dMap.put(d1, dMap.getOrDefault(d1, 0) + 1);
            
            String d2 = discount[left];
            int cnt = dMap.get(d2);
            if (cnt == 1) {
                dMap.remove(d2);
            } else {
                dMap.put(d2, cnt-1);
            }
            left++;
        }
        return answer;
    }
}