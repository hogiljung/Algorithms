for _ in range(int(input())):
    line = input().split()
    student_cnt, scores = int(line[0]), list(map(int, line[1:]))
    avg = sum(scores) / student_cnt
    cnt = sum((1 for score in scores if score > avg))
    print(f"{cnt/student_cnt*100:.3f}%")