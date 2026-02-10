class Solution {
    // picture의 길이의 k배의 배열이 필요
    // picture를 순회
    // 요소의 요소를 k개 담은 문자열 생성
    // 해당 문자열을 k번 넣는다
    public String[] solution(String[] picture, int k) {
        String[] answer = new String[picture.length * k];
        for (int i=0; i<picture.length; i++) {
            StringBuilder sb = new StringBuilder();
            for (char c : picture[i].toCharArray()) {
                sb.append(String.valueOf(c).repeat(k));
            }
            
            String s = sb.toString();
            for (int j=0; j<k; j++) {
                answer[i*k+j] = s;
            }
        }
        return answer;
    }
}