class Solution {
    public String solution(String a, String b) {
        int carry = 0;
        int i = a.length()-1, j = b.length()-1;
        StringBuilder sb = new StringBuilder();
        while (i > -1 || j > -1 || carry > 0) {
            int sum = carry;
            
            if (i > -1) {
                sum += a.charAt(i--) - '0';
            }
            if (j > -1) {
                sum += b.charAt(j--) - '0';
            }
            
            sb.append(sum % 10);
            carry = sum / 10;
        }
        
        return sb.reverse().toString();
    }
}