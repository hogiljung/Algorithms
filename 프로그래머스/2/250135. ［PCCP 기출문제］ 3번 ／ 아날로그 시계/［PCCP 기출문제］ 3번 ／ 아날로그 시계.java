/*
초침 -> 1초에 6도 -> 1도 1/6초
분침 -> 1분에 6도 -> 1초에 1/10도 -> 1도에 10초
시침 -> 1시간 30도 -> 1분에 1/2도 -> 1초에 1/120도 -> 1도에 2분
*/

class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int startTime = h1 * 3600 + m1 * 60 + s1;
        int endTime = h2 * 3600 + m2 * 60 + s2;
        
        long s = (startTime * 720L) % 43200;
        long m = (startTime * 12L) % 43200;
        long h = startTime % 43200;
        
        int answer = (s == m || s == h) ? 1 : 0;
        for (int t = startTime; t < endTime; t++) {
            long ns = s + 720;
            long nm = m + 12;
            long nh = h + 1;
            
            boolean passM = s < m && ns >= nm;
            boolean passH = s < h && ns >= nh;

            if (passM) answer++;
            if (passH) answer++;

            if (passM && passH && (t + 1) % 43200 == 0) {
                answer--;
            }

            s = ns % 43200;
            m = nm % 43200;
            h = nh % 43200;
        }
        
        return answer;
    }
}