class Solution {
    public String solution(String s) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (String part : s.split(" ")) {
            int cur = Integer.parseInt(part);
            if (cur < min) min = cur;
            if (cur > max) max = cur;
        }
        
        return min + " " + max;
    }
}