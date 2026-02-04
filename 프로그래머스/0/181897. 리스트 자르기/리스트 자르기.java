import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
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
        int[] answer = new int[(e-s)/g+1];
        for (int i=0; i*g+s<=e; i++) {
            answer[i] = num_list[i*g+s];
        }
        return answer;
    }
}