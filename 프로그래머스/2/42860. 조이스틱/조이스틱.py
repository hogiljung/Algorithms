def solution(name):
#     answer = 0
    
#     # 위아래로 움직이는 최소 횟수 맵핑.
#     num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]

#     n = len(name)
#     # 좌우로 움직이는 최소 횟수는 문자열의 수.
#     move = n - 1
    
#     for right in range(n):
#         # 위아래 움직이는 수 계산 후 더해준다.
#         answer += num_char[ord(name[right]) - ord('A')]
#         # 다음으로 A가 아닌 인덱스를 찾기 위한 변수 선언.
#         next_a_idx = right + 1
#         # A가 아닌 문자를 찾을 때까지 인덱스를 늘린다.
#         while (next_a_idx < n) and (name[next_a_idx] == 'A'):
#             next_a_idx += 1
#         left = n - next_a_idx
#         # 현재 위치로의 이동거리와 다음으로 A가 아닌 문자의 문자의 끝에서부터 거리를 비교하여 작은걸 찾는다.
#         # 이걸 통해 다음 변경할 A가 현재 위치에서 오른쪽으로 가는게 빠른지 왼쪽에서 가는게 빠른지 알 수 있다.
#         move = min(move, min(right + right + left, left + left + right))

#     answer += move
    
#     return answer
    n = len(name)
    answer = 0

    # 각 위치별 알파벳 변경 횟수 계산
    change_counts = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]
    answer += sum(change_counts)

    # 최적의 커서 이동 계산
    min_move = n - 1  # 기본적으로 오른쪽으로 쭉 가는 경우
    for i in range(n):
        # 오른쪽에서 가장 가까운 A가 아닌 문자의 인덱스를 찾는다.
        next_index = i + 1
        while next_index < n and name[next_index] == 'A':
            next_index += 1
        # 위의 인덱스를 이용해 아래 두가지 이동 경우의 거리를 계산한다.
        # 1. 오른쪽으로 갔다가 다시 왼쪽으로 돌아오는 경우
        right_then_left = i + i + n - next_index
        # 2. 왼쪽으로 갔다가 다시 오른쪽으로 돌아오는 경우
        left_then_right = i + (n - next_index) + (n - next_index)
        min_move = min(min_move, right_then_left, left_then_right)

    answer += min_move
    return answer
