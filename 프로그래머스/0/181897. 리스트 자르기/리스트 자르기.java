import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        ArrayList<Integer> answer = new ArrayList<>();
        int s=slicer[0], e=slicer[1], g=1;
        switch (n) {
            case 1:
                s = 0;
                break;
            case 2:
                e = num_list.length-1;
                break;
            case 3:
                break;
            case 4:
                g = slicer[2];
                break;
        }
        for (int i=s; i<=e; i+=g) {
            answer.add(num_list[i]);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}