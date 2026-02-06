import java.util.ArrayList;

class Solution {
    public String[] solution(String myStr) {
        String[] parts = myStr.split("[abc]+");
        
        ArrayList<String> list = new ArrayList<>();
        
        for (String part : parts) {
            if (!part.isEmpty()) {
                list.add(part);
            }
        }
        
        return list.isEmpty() ? new String[] {"EMPTY"} : list.toArray(String[]::new);
    }
}