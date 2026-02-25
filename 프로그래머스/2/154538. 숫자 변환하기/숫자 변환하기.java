import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        boolean[] visit = new boolean[y + 1];
        Queue<int[]> queue = new LinkedList<>();
        
        visit[x] = true;
        queue.offer(new int[] { x, 0 });
        
        while (!queue.isEmpty()) {
            int[] data = queue.poll();
            int cur = data[0];
            int cnt = data[1];
            
            if (cur == y) {
                return cnt;
            }
            
            int[] nextArr = { cur + n, cur * 2, cur * 3 };
            for (int next : nextArr) {
                if (next <= y && !visit[next]) {
                    visit[next] = true;
                    queue.offer(new int[] { next, cnt + 1 });
                }
            }
        }
        return -1;
    }
}