import java.util.*;

class Solution {
    public int solution(int k, int[][] dungeons) {
        List<List<Integer>> totalOrder = new ArrayList<>();
        boolean[] visited = new boolean[dungeons.length];
        
        makeOrder(totalOrder, visited, new ArrayList<>());
        
        int answer = 0;
        for (List<Integer> order: totalOrder) {
            int count = 0;
            int currentK = k;
            
            for (int idx: order) {
                if (currentK < dungeons[idx][0])
                    break;
                
                currentK -= dungeons[idx][1];
                count++;
            }
            
            answer = Math.max(answer, count);
        }
        
        return answer;
    }
    
    private void makeOrder(List<List<Integer>> totalOrder, boolean[] visited, List<Integer> orderList) {
        if (orderList.size() == visited.length) {
            totalOrder.add(new ArrayList<>(orderList));
            return;
        }
        
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                orderList.add(i);
                makeOrder(totalOrder, visited, orderList);
                visited[i] = false;
                orderList.remove(orderList.size() - 1);
            }
        }
    }
}