import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> remaining = new HashMap<>();
        
        for (int i = 0; i < want.length; i++) {
            remaining.put(want[i], number[i]);
        }
        
        int satisfied = 0;
        int count = 0;
        
        for (int right = 0; right < discount.length; right++) {
            String added = discount[right];
            
            if (remaining.containsKey(added)) {
                int next = remaining.get(added) - 1;
                remaining.put(added, next);
                
                if (next == 0) {
                    satisfied++;
                } else if (next == -1) {
                    satisfied--;
                }
            }
            
            if (right >= 10) {
                String removed = discount[right - 10];
                
                if (remaining.containsKey(removed)) {
                    int next = remaining.get(removed) + 1;
                    remaining.put(removed, next);
                    
                    if (next == 0) {
                        satisfied++;
                    } else if (next == 1) {
                        satisfied--;
                    }
                }
            }
            
            if (right >= 9 && satisfied == want.length) {
                count++;
            }
        }
        
        return count;
    }
}