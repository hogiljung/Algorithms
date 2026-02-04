class Solution {
    public int[] solution(int[] arr, int[] query) {
        int s = 0;
        int e = arr.length - 1;

        for (int i = 0; i < query.length; i++) {
            int q = query[i];

            if (i % 2 == 0) {
                // 짝수 인덱스 → 뒤를 자름 (q 포함)
                e = s + q;
            } else {
                // 홀수 인덱스 → 앞을 자름 (q 포함)
                s = s + q;
            }
        }

        int[] answer = new int[e - s + 1];
        for (int i = s; i <= e; i++) {
            answer[i - s] = arr[i];
        }
        return answer;
    }
}