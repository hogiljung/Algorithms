import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Process> q = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            q.offer(new Process(i, priorities[i]));
        }
        
        int answer = 0;
        while (!q.isEmpty()) {
            answer++;

            int maximum = 0;
            int idx = 0;
            int maxIdx = 0;
            
            for (Process p : q) {
                if (maximum < p.priority) {
                    maximum = p.priority;
                    maxIdx = idx; 
                }
                idx++;
            }
            
            for (int i = 0; i < maxIdx; i++) {
                q.offer(q.poll());
            }
            
            Process p = q.poll();
            if (p.id == location) {
                break;
            }
        }
        
        return answer;
    }
    
    class Process {
        int id;
        int priority;
        
        Process (int id, int priority) {
            this.id = id;
            this.priority = priority;
        }
    }
}