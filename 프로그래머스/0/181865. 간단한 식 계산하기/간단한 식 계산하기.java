class Solution {
    public int solution(String binomial) {
        String[] s = binomial.split(" ");
        int a = Integer.parseInt(s[0]);
        int b = Integer.parseInt(s[2]);
        int answer = 0;
        switch (s[1]) {
            case "+" -> {answer = a + b;}
            case "-" -> {answer = a - b;}
            case "*" -> {answer = a * b;}
        }
        return answer;
    }
}