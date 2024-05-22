from collections import deque
from math import ceil


def solution(progresses, speeds):
    answer = []
    SUCCESS = 100
    
    # 필요 진행 일수를 계산한다.
    q = deque(\
      [ceil((SUCCESS - progress) / speed)\
       for progress, speed in zip(progresses, speeds)]
    )
    
    current_maximum_required = 0
    while q:
        required = q.popleft()
        
        # 이전 가장 오래 걸린 진행 일수보다 작거나 같은 경우,
        if required <= current_maximum_required:
            # 배포한 개수를 늘린다.
            answer[-1] += 1
        # 그렇지 않은 경우
        else:
            # 배포 개수를 새로 추가한다.
            answer.append(1)
            current_maximum_required = required
            
    return answer
