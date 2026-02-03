import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=l; i<=r; i++) {
            String s = String.valueOf(i);
            s = s.replaceAll("0|5", "");
            if (s.isEmpty()) {
                answer.add(i);
            }
        }
        
        return answer.isEmpty()
            ? new int[]{-1}
            : answer.stream().mapToInt(Integer::intValue).toArray();
    }
}