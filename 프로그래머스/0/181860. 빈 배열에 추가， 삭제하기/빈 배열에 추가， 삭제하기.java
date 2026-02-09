import java.util.ArrayDeque;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < arr.length; i++) {
            int n = arr[i];

            if (flag[i]) {
                for (int j = 0; j < n * 2; j++) {
                    deque.addLast(n);
                }
            } else {
                for (int j = 0; j < n; j++) {
                    deque.pollLast();
                }
            }
        }

        int[] answer = new int[deque.size()];
        int idx = 0;
        for (int x : deque) {
            answer[idx++] = x;
        }

        return answer;
    }
}