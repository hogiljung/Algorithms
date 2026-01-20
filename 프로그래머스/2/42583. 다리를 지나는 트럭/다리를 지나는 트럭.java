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
    class Truck {
        int weight;
        int move;

        public Truck(int weight) {
            this.weight = weight;
        }

        public void moving() {
            move++;
        }
    }

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Truck> waitQ = new ArrayDeque<>();
        Queue<Truck> moveQ = new ArrayDeque<>();

        for (int tw : truck_weights) {
            waitQ.offer(new Truck(tw));
        }

        int answer = 0;
        int curWeight = 0;

        while (!waitQ.isEmpty() || !moveQ.isEmpty()) {
            answer++;
            for (Truck t : moveQ) {
                t.moving();
            }

            if (!moveQ.isEmpty() && moveQ.peek().move > bridge_length) {
                Truck t = moveQ.poll();
                curWeight -= t.weight;
            }

            // if (moveQ.isEmpty()) {
            // Truck t = waitQ.poll();
            // curWeight += t.weight;
            // moveQ.offer(t);
            // continue;
            // }

            if (!waitQ.isEmpty() && curWeight + waitQ.peek().weight <= weight) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                t.moving();
                moveQ.offer(t);
            }
        }

        return answer;
    }
}