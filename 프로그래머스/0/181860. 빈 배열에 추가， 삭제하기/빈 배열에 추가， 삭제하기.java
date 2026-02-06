import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i=0; i<arr.length; i++) {
            int n = arr[i];
            if (flag[i]) {
                for (int j=0; j<n*2; j++) {
                    answer.add(n);
                }
            } else {
                for (int j=0; j<n; j++) {
                    answer.remove(answer.size()-1);
                }
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}