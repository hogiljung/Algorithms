class Solution {
    public int solution(int n, int[] cores) {
        int left = 1;
        int right = 50000;
        int time = 0;
        int worked = 0;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            
            for (int core : cores) {
                count += Math.ceil((double) mid / core);
            }
            
            if (count >= n) {
                right = mid - 1;
            } else {
                time = mid;
                worked = count;
                left = mid + 1;
            }
        }
        
        int answer = 0;
        while (worked < n) {
            for (int i = 0; i < cores.length; i++) {
                if (time % cores[i] == 0) {                    
                    if (++worked == n) {
                        answer = i + 1;
                    }
                }
            }
        }
        
        return answer;
    }
}