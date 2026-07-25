class Solution {
    public int solution(int[][] sizes) {
        int width = 0;
        int height = 0;
        
        for (int[] size: sizes) {
            int w = size[0];
            int h = size[1];
            
            if (w < h) {
                int temp = h;
                h = w;
                w = temp;
            }
            
            width = Math.max(width, w);
            height = Math.max(height, h);
        }
        
        return width * height;
    }
}