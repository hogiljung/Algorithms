import sys
input = sys.stdin.readline

A, B = input().rsplit()
A, B = A[::-1], B[::-1]
print(A if int(A) > int(B) else B)