import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        int count = 0;
        for (int left = 0, right = 0; right < discount.length; right++) {
            String d = discount[right];
            if (map.containsKey(d)) {
                map.put(d, map.get(d) - 1);
            }
            
            if (right - left + 1 > 10) {
                d = discount[left++];
                if (map.containsKey(d)) {
                    map.put(d, map.get(d) + 1);
                }
            }
            
            boolean isOk = true;
            for (int n : map.values()) {
                if (n > 0) {
                    isOk = false;
                    break;
                }
            }
            
            if (isOk) {
                count++;
            }
        }
        
        return count;
    }
}