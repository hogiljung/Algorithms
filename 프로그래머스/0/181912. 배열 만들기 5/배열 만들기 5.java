import java.util.ArrayList;
import java.util.List;

class Solution {
    // intStrs를 순회
    // intStr에서 substring
    // int로 변환
    // k와 비교
    // 크다면 배열에 담는다
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        
        for (String intStr: intStrs) {
            String subS = intStr.substring(s, s+l);
            int intS = Integer.parseInt(subS);
            if (k < intS) {
                answer.add(intS);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}