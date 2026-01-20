import java.util.*;

// 현재 다리에 있는 트럭 무게와 다음에 올 트럭의 무게의 합과 가능한 무게를 비교한다.
// 들어올 수 있을만큼 트럭을 보내고 해당 시간만큼 늘린다.
// 트럭을 다리에 올리고 시간을 1초 늘린다.
// 이를 반복한다.
// 다음에 올 트럭이 없다면 다리 길이만큼 시간을 늘린다.

// 현재 시간을 갱신한다.
// 들어가는 차량에 들어간 시간을 부여하고,
// 빠져나올 때 걸린 시간을 파악한다.
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        ArrayDeque<int[]> q = new ArrayDeque<>();
        int on_board_weight = 0;
        for (int tw : truck_weights) {
            time += 1;
            if (!q.isEmpty()) {
                int[] info = q.peek();
                if (info[1] + bridge_length <= time) {
                    q.pop();
                    on_board_weight -= info[0];
                }
            }

            on_board_weight += tw;
            while (on_board_weight > weight) {
                int[] info = q.poll();
                on_board_weight -= info[0];
                time += bridge_length - (time - info[1]);
            }
            q.add(new int[] { tw, time });
        }

        while (!q.isEmpty()) {
            int[] info = q.poll();
            on_board_weight -= info[0];
            time += bridge_length - (time - info[1]);
        }

        return time;
    }
}