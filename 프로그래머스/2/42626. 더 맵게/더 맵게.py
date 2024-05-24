import heapq

def solution(scoville, K):
    answer = 0
    
    # 모든 스코빌 지수를 힙에 넣는다.
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    # 힙에 자료가 1보다 크고,
    # 가장 처음 값이 K 보다 작을 때까지 반복한다.
    while len(heap) > 1 and heap[0] < K:
        # 힙에서 두개를 꺼낸다.
        first, second = heapq.heappop(heap), heapq.heappop(heap)
        # 계산하여 다시 힙에 집어넣는다.
        mixed = first + second * 2
        heapq.heappush(heap, mixed)
        # 횟수를 1 증가한다.
        answer += 1
        
    return answer if heap[0] >= K else -1
