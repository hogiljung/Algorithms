/*
각 심사관이 걸려도 되는 최소 시간을 구한다.
*/


class Solution {
    public long solution(int n, int[] times) {
        int minimumTime = 1_000_000_000;
        for (int time : times) {
            minimumTime = Math.min(minimumTime, time);
        }
        
        long left = 1;
        long right = (long) minimumTime * n;
        
        while (left < right) {
            long availableTime = left + (right - left) / 2;
            long total = 0;
            
            for (int time : times) {
                total += availableTime / time;
                
                if (total > n) {
                    break;
                }
            }
            
            if (total >= n) {
                right = availableTime;
            } else {
                left = availableTime + 1;
            }
        }
        
        return left;
    }
}