import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr) {
        int arrLength = arr.length;
        int newArrLength = 1;
        for (int i=0; i<=10; i++) {
            int pow = (int) Math.pow(2, i);
            if (arrLength <= pow) {
                newArrLength = pow;
                break;
            }
        }
        
        return IntStream.concat(
            Arrays.stream(arr), 
            IntStream.range(0, newArrLength - arrLength).map(i -> 0)
        ).toArray();
    }
}