import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int compareLength = Integer.compare(arr1.length, arr2.length);
        if (compareLength != 0) {
            return compareLength;
        }
        
        return Integer.compare(
            Arrays.stream(arr1).sum(),
            Arrays.stream(arr2).sum()
        );
    }
}