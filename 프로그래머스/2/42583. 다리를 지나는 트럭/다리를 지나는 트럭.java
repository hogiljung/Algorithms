import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Integer> bridge = new ArrayDeque<>();
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        
        int onBridgeWeight = 0;
        int time = 0;
        int truckIdx = 0;
        while (truckIdx < truck_weights.length) {
            onBridgeWeight -= bridge.poll();
            
            int truckWeight = truck_weights[truckIdx];
            while (!bridge.isEmpty() && onBridgeWeight + truckWeight > weight) {
                onBridgeWeight -= bridge.poll();
                bridge.offer(0);
                time++;
            }
            
            bridge.offer(truckWeight);
            onBridgeWeight += truckWeight;
            time++;
            truckIdx++;
        }
        
        while (!bridge.isEmpty()) {
            bridge.poll();
            time++;
        }
        
        return time;
    }
}