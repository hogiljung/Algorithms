score = int(input())
answer = ''
if score >= 90:
    answer = 'A'
elif score >= 80:
    answer = 'B'
elif score >= 70:
    answer = 'C'
elif score >= 60:
    answer = 'D'
else:
    answer = 'F'
print(answer)