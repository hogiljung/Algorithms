class Solution {
    public String solution(String myString) {
        char[] arr = myString.toCharArray();
        for (int i=0; i<arr.length; i++) {
            char c = arr[i];
            if (c != 'A' && Character.isUpperCase(arr[i])) {
                arr[i] = Character.toLowerCase(c);
            } else if (c == 'a') {
                arr[i] = 'A';
            }
        }
        return new String(arr);
    }
}