class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        for (int i=0; i<3; i++) {
            int top = 101;
            int index = 0;
            for (int j=0; j<rank.length; j++) {
                if (attendance[j] && rank[j] < top) {
                    top = rank[j];
                    index = j;
                }
            }
            
            rank[index] = 101;
            
            answer += (int) Math.pow(100, 2-i) * index;
        }
        return answer;
    }
}