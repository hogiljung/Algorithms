import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
        int answer = 0;
        
        for (int e : enemy) {
            n -= e;
            heap.offer(e);
            if (n < 0 && k > 0) {
                n += heap.poll();
                k--;
            }
            
            if (n < 0) {
                break;
            } else {
                answer++;
            }
        }
        
        return answer;
    }
}