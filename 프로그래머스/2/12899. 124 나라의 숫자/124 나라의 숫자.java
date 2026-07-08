import java.util.*;

/*
1 -> 0 .. 1 -> 1
2 -> 0 .. 2 -> 2
3 -> 1 .. 0 -> 4
4 -> 1 .. 1 -> 11
5 -> 1 .. 2 -> 12
6 -> 2 .. 0 -> 14
7 -> 2 .. 1 -> 21
8 -> 2 .. 2 -> 22
9 -> 3 .. 0 -> 24
10 -> 3 .. 1 -> 41
11 -> 3 .. 2 -> 42
12 -> 4 .. 0 -> 44
13 -> 4 .. 1 -> 111
14 -> 4 .. 2 -> 112
15 -> 5 .. 0 -> 114
16 -> 5 .. 1 -> 121
17 -> 5 .. 2 -> 122
18 -> 6 .. 0 -> 124

1. 3으로 나눈 나머지가 0 이면 일의 자리 4
2. 이전에 3으로 나눈 나머지가 0 이면 현재 몫에서 1 빼고 반복
*/

class Solution {
    public String solution(int n) {
        Deque<Integer> s = new ArrayDeque<>();
        
        while (n > 0) {
            int remainder = n % 3;
            boolean isZero = remainder == 0;
            int nOf124 = 0;
            int quotient = n / 3;
            if (isZero) {
                nOf124 = 4;
                quotient -= 1;
            } else {
                nOf124 = remainder;
            }
            
            s.push(nOf124);
            
            n = quotient;
        }
        
        StringBuilder sb = new StringBuilder();
        
        while (!s.isEmpty()) {
            sb.append(String.valueOf(s.pop()));
        }
        
        return sb.toString();
    }
}