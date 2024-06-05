def solution(name):
    answer = 0
    n = len(name)
    # 최적의 커서 이동 계산
    min_move = n - 1  # 오른쪽으로 쭉 가는 경우
    for i in range(n):
        # 각 위치별 알파벳 변경 횟수 계산
        change_counts = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        answer += change_counts
        # 오른쪽에서 가장 가까운 A가 아닌 문자의 인덱스를 찾는다.
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        # 위의 인덱스를 이용해 아래 두가지 이동 경우의 거리를 계산한다.
        # 1. 오른쪽으로 갔다가 다시 왼쪽으로 돌아오는 경우
        right_then_left = i + i + n - next_index
        # 2. 왼쪽으로 갔다가 다시 오른쪽으로 돌아오는 경우
        left_then_right = i + (n - next_index) + (n - next_index)
        # 모든 이동 경우에 대해 커서 이동의 최솟값을 찾는다.
        min_move = min(min_move, right_then_left, left_then_right)

    answer += min_move
    return answer
