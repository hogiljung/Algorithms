import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        HashSet<Integer> map = new HashSet<>();
        for (int n : delete_list) {
            map.add(n);
        }
        ArrayList<Integer> answer = new ArrayList<>();
        for (int n : arr) {
            if (!map.contains(n)) {
                answer.add(n);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}