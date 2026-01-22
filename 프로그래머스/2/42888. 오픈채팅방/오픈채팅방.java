import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] record) {
        HashMap<String, String> nameMap = new HashMap<>();
        ArrayList<String[]> temp = new ArrayList<>();
        
        for (String r : record) {
            String[] data = r.split(" ");
            String uid = data[1];
            switch (data[0]) {
                case "Enter":
                    temp.add(new String[]{uid, "님이 들어왔습니다."});
                    nameMap.put(uid, data[2]);
                    break;
                case "Leave":
                    temp.add(new String[]{uid, "님이 나갔습니다."});
                    break;
                case "Change":
                    nameMap.put(uid, data[2]);
                    break;
            }
        }
        
        int n = temp.size();
        String[] answer = new String[n];
        for (int i=0; i<n; i++) {
            String[] t = temp.get(i);
            answer[i] = nameMap.get(t[0]) + t[1];
        }
        return answer;
    }
}