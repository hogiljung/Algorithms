import java.util.Arrays;

class Solution {
    public int solution(String[] strArr) {
        int[] t = new int[31];
        for (String str : strArr) {
            t[str.length()]++;
        }
        
        return Arrays.stream(t).max().orElse(0);
    }
}