class Solution {
    public String solution(String a, String b) {
        int carry = 0;
        int i = a.length()-1, j = b.length()-1;
        StringBuilder sb = new StringBuilder();
        while (i > -1 || j > -1) {
            int aNum = 0, bNum = 0;
            if (i > -1) {
                aNum = Integer.parseInt((a.charAt(i--) - '0') + "");
            }
            if (j > -1) {
                bNum = Integer.parseInt((b.charAt(j--) - '0') + "");
            }
            int sum = aNum + bNum + carry;
            sb.append(String.valueOf(sum % 10));
            carry = sum / 10;
        }
        
        if (carry != 0) {
            sb.append(String.valueOf(carry));
        }
        
        return sb.reverse().toString();
    }
}