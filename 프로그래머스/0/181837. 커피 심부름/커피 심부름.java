class Solution {
    // 주문 순회
    // 아메리카노가 있거나 아무거나면 4500원
    // 라떼가 있으면 5000원
    public int solution(String[] order) {
        int answer = 0;
        for (String menu : order) {
            if (menu.contains("americano") || menu.equals("anything")) {
                answer += 4500;
            } else {
                answer += 5000;
            }
        }
        return answer;
    }
}