while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    if max(A,B) % min(A,B) == 0:
        print('multiple') if A>B else print('factor')
    else:
        print('neither')
