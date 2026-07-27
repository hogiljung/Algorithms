import java.util.*;

class Solution {
    int[] parent;

    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;

        for (int removed = 0; removed < wires.length; removed++) {
            parent = new int[n + 1];

            for (int i = 1; i <= n; i++) {
                parent[i] = i;
            }

            // removed번째 전선만 제외하고 합치기
            for (int i = 0; i < wires.length; i++) {
                if (i == removed) {
                    continue;
                }

                union(wires[i][0], wires[i][1]);
            }

            // 1번 노드가 속한 컴포넌트 크기 계산
            int root = findParent(1);
            int count = 0;

            for (int i = 1; i <= n; i++) {
                if (findParent(i) == root) {
                    count++;
                }
            }

            int otherCount = n - count;
            answer = Math.min(answer, Math.abs(count - otherCount));
        }

        return answer;
    }

    int findParent(int x) {
        if (parent[x] == x) {
            return x;
        }

        return parent[x] = findParent(parent[x]);
    }

    void union(int a, int b) {
        int rootA = findParent(a);
        int rootB = findParent(b);

        if (rootA != rootB) {
            parent[rootB] = rootA;
        }
    }
}