/*
1. 서브 컨테이너가 원하는 상자면 싣는다.
2. 아니면 메인에서 다음 상자를 보조 벨트로 싣는다.
3. 더 이상 가져올 상자가 없고 보조 벨트에서도 꺼낼 수 없으면 종료
*/

import java.util.*;

class Solution {
    public int solution(int[] order) {
        Deque<Integer> subBelt = new ArrayDeque<>();
        int nextBox = 1;
        int loadedCount = 0;
        
        while (loadedCount < order.length) {
            int targetBox = order[loadedCount];
            
            if (!subBelt.isEmpty() && targetBox == subBelt.peek()) {
                subBelt.pop();
                loadedCount++;
            } else if (nextBox <= order.length) {
                subBelt.push(nextBox++);                
            } else {
                break;
            }
        }
        
        return loadedCount;
    }
}