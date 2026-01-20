import java.util.ArrayDeque;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i=0; i<progresses.length; i++) {
            q.add(i);
        }
        
        ArrayList<Integer> answer = new ArrayList<>();
        while (!q.isEmpty()) {
            int cnt = 1;
            int i = q.poll();
            int progress = progresses[i];
            int progressedDays = (int) Math.ceil((double) (100 - progress) / speeds[i]);

            while (!q.isEmpty()) {
                int j = q.getFirst();
                if (progresses[j] + speeds[j] * progressedDays >= 100) {
                    q.poll();
                    cnt++;
                } else {
                    break;
                }
            }
            answer.add(cnt);
        }

        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}