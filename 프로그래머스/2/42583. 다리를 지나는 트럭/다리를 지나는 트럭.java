import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Integer> bridge = new LinkedList<>();
        
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        
        int curWeight = 0;
        int curTime = 0;
        int truckIdx = 0;
        
        while (truckIdx < truck_weights.length) {
            curTime++;
            
            curWeight -= bridge.poll();
            
            if (curWeight + truck_weights[truckIdx] <= weight) {
                curWeight += truck_weights[truckIdx];
                bridge.offer(truck_weights[truckIdx++]);
            } else {
                bridge.offer(0);
            }
        }
        
        return curTime + bridge_length;
    }
}