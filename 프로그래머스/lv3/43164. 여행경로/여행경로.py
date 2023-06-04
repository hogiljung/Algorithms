from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    
    # 이해가 가지 않아 내 마음대로 해석해봤다 나중에 다시 확인해보자
    # 1. 한 루트를 택해 끝까지 진입
    # 2. 모든 티켓을 사용했다면(= 모든 경로를 지났다면) 역으로 경로에 삽입
    # 3. 모든 티켓을 사용하지 못했다면 해당 경로는 나중에 진행해야 함. 따라서 다른 경로를 택해 다시 끝까지 진입.
    # 2~3 반복
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]