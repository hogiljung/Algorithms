import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int[] sortedNumbers = Arrays.stream(numbers).sorted().toArray();
        int N = sortedNumbers.length;
        return sortedNumbers[N-1] * sortedNumbers[N-2];
    }
}