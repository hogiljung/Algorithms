class Solution {
    public long solution(int n, int[] times) {
        long maximumTime = times[0];
        for (int time: times) {
            maximumTime = Math.max(maximumTime, time);
        }
        
        long right = n * maximumTime;
        long left = 1;
        long answer = right;
        
        while (left <= right) {
            long count = 0;
            long mid = left + (right - left) / 2;
            
            for (int time: times) {
                count += mid / time;
                
                if (count >= n) break;
            }
            
            if (count >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return answer;
    }
}