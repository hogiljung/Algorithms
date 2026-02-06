import java.util.Arrays;

class Solution {
    public String[] solution(String myStr) {
        String[] temp = Arrays.stream(myStr.split("[abc]+"))
            .filter(x -> !x.isEmpty())
            .toArray(String[]::new);
        
        return temp.length == 0 ? new String[] {"EMPTY"} : temp;
    }
}