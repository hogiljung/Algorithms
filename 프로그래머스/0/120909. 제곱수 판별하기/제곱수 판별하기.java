class Solution {
    public int solution(int n) {
        double nSqrt = Math.sqrt(n);
        return Double.compare(Math.ceil(nSqrt), Math.floor(nSqrt)) == 0 ? 1 : 2;
    }
}