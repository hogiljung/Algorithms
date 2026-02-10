import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(
            (a, b) -> rank[a] - rank[b]
        );
        
        for (int i=0; i<rank.length; i++) {
            if (attendance[i]) {
                queue.add(i);
            }
        }
        
        int answer = 0;
        int i = 0;
        while (i < 3) {
            int n = queue.poll();
            answer = answer * 100 + n;
            i++;
        }
        
        return answer;
    }
    
    class Attended {
        int rank;
        
        Attended(int rank) {
            this.rank = rank;
        }
    }
}