class Solution {
    public int[] solution(int[] num_list) {
        int numListLength = num_list.length;
        int[] answer = new int[numListLength + 1];
        
        for (int i=0; i<numListLength; i++) {
            answer[i] = num_list[i];
        }
        
        int lastIdxNum = answer[numListLength - 1];
        int secondLastIdxNum = answer[numListLength - 2];
        answer[numListLength] = lastIdxNum > secondLastIdxNum ?
            lastIdxNum - secondLastIdxNum : lastIdxNum * 2;
        
        return answer;
    }
}