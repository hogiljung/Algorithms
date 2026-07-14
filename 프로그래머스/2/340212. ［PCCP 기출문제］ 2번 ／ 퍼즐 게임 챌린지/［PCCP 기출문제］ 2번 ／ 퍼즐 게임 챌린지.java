class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1;
        int right = 0;
        
        for (int diff : diffs) {
            right = Math.max(right, diff);
        }
        
        while (left <= right) {
            int level = left + (right - left) / 2;
            long totalTime = times[0];
            
            for (int i = 1; i < times.length; i++) {
                if (diffs[i] > level) {
                    int failCount = diffs[i] - level;

                    totalTime += (times[i - 1] + times[i]) * failCount;
                }
                
                totalTime += times[i];
                
                if (totalTime > limit) {
                    break;
                }
            }
            
            if (totalTime <= limit) {
                right = level - 1;
            } else {
                left = level + 1;
            }
        }
        
        return left;
    }
}