class Solution {
    public String[] solution(String[] str_list) {
        int l = -1, r = -1;
        for (int i=0; i<str_list.length; i++) {
            String s = str_list[i];
            if (s.equals("l")) {
                l = i;
                break;
            } else if (s.equals("r")) {
                r = i;
                break;
            }
        }
        
        String[] answer;
        if (l != -1) {
            answer = new String[l];
            for (int i=0; i<l; i++) {
                answer[i] = str_list[i];
            }
        } else if (r != -1) {
            answer = new String[str_list.length - r - 1];
            for (int i=0; i<str_list.length - r - 1; i++) {
                answer[i] = str_list[i+r+1];
            }
        } else {
            answer = new String[0];
        }
        return answer;
    }
}