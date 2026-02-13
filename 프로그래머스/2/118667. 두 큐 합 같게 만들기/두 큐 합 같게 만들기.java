import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Deque<Long> q1 = new LinkedList<>();
        Deque<Long> q2 = new LinkedList<>();
        long sum1 = 0, sum2 = 0;
        
        for (int i=0; i<queue1.length; i++) {
            long q1Item = queue1[i];
            long q2Item = queue2[i];
            q1.add(q1Item);
            q2.add(q2Item);
            sum1 += q1Item;
            sum2 += q2Item;
        }
        
        int answer = 0;
        while (sum1 != sum2) {
            if (sum1 < sum2) {
                long n = q2.poll();
                sum2 -= n;
                q1.add(n);
                sum1 += n;
                answer++;
            } else if (sum1 > sum2) {
                long n = q1.poll();
                sum1 -= n;
                q2.add(n);
                sum2 += n;
                answer++;
            }
            
            if (answer >= queue1.length * 4) {
                answer = -1;
                break;
            }
        }
        return answer;
    }
}