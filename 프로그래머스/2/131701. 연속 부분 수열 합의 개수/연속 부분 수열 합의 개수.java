import java.util.*;

class Solution {
    public int solution(int[] elements) {
        Set<Integer> sumSet = new HashSet<>();
        
        for (int size = 1; size <= elements.length; size++) {
            int sum = 0;
            int left = 0;
            for (int right = 0; right < elements.length * 2; right++) {
                sum += elements[right % elements.length];
                
                if (right - left + 1 > size) {
                    sum -= elements[left % elements.length];
                    left++;
                }
                
                sumSet.add(sum);
            }
        }
        
        
        return sumSet.size();
    }
}