class Solution {
    public int solution(String s) {
        int n = s.length();
        int answer = n;
        
        for (int l = 1; l <= n / 2; l++) {
            StringBuilder compressed = new StringBuilder();
            String prev = s.substring(0, l);
            int cnt = 1;
            for (int i = l; i < n; i += l) {
                String cur = s.substring(i, Math.min(i + l, n));
                if (cur.equals(prev)) {
                    cnt++;
                    continue;
                }
                if (cnt > 1) {
                    compressed.append(cnt);
                }
                compressed.append(prev);
                prev = cur;
                cnt = 1;
            }
            if (cnt > 1) {
                compressed.append(cnt);
            }
            compressed.append(prev);
            answer = Math.min(answer, compressed.length());
        }
        return answer;
    }
}