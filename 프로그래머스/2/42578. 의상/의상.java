import java.util.*;

/*
종류별로 갯수를 세서 조합의 수를 구한다.
*/

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> cMap = new HashMap<>();
        
        for (String[] c : clothes) {
            cMap.put(c[1], cMap.getOrDefault(c[1], 0) + 1);
        }
        
        int answer = 1;
        
        for (Integer v : cMap.values()) {
            answer *= v + 1;
        }
        
        return answer - 1;
    }
}