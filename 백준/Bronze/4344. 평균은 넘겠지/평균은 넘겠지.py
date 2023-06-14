for _ in range(int(input())):
    input_line = list(map(int, input().split()))
    n, scores = input_line[0], input_line[1:]
    avg = sum(scores)/n
    count = 0
    for score in scores:
        if avg < score:
            count += 1
    print(f'{count/n*100:.3f}%')