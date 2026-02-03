class Solution {
    public int solution(int n, String control) {
        int temp = n;
        
        for (char c : control.toCharArray()) {
            switch (c) {
                case 'w':
                    temp += 1;
                    break;
                case 's':
                    temp -= 1;
                    break;
                case 'd':
                    temp += 10;
                    break;
                case 'a':
                    temp -= 10;
                    break;
            }
        }
        
        int answer = temp;
        return answer;
    }
}