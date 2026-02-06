class Solution {
    public int[] solution(String myString) {
        boolean isLastX = myString.charAt(myString.length()-1) == 'x';
        String[] arr = myString.split("x");
        
        int[] answer = new int[arr.length + (isLastX ? 1 : 0)];
        for (int i=0; i<arr.length; i++) {
            answer[i] = arr[i].length();
        }
        return answer;
    }
}