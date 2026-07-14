class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int n = queue1.length;
        int[] q = new int[n * 2];
    
        long sumQ1 = 0;
        long sumQ2 = 0;
        
        for (int i = 0; i < queue1.length; i++) {
            q[i] = queue1[i];
            q[i + n] = queue2[i];
            
            sumQ1 += queue1[i];
            sumQ2 += queue2[i];
        }
        
        long total = sumQ1 + sumQ2;

        if (total % 2 != 0) {
            return -1;
        }

        long target = total / 2;

        int left = 0;
        int right = n;
        int count = 0;
        
        int maxCount = n * 3;
        
        while (count <= maxCount) {
            if (sumQ1 == target) {
                return count;
            }
            
            if (sumQ1 < target) {
                sumQ1 += q[right % q.length];
                right++;
            } else {
                sumQ1 -= q[left % q.length];
                left++;
            }
            
            count++;
        }
        
        return -1;
    }
}