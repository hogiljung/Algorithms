class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        String s = ineq + eq;
        boolean t = false;
        
        switch (s) {
            case ">=":
                t = n >= m;
                break;
            case ">!":
                t = n > m;
                break;
            case "<=":
                t = n <= m;
                break;
            case "<!":
                t = n < m;
                break;
        }
        
        return t ? 1 : 0;
    }
}