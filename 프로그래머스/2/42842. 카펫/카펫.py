def solution(brown, yellow):
    answer = []
    
    # 두 수의 합이 카펫의 넓이와 같다.
    area = brown + yellow
    # 조건에 따라 최소 넓이는 9이고, 최소 세로 길이는 3이다.
    # 최소 세로 길이인 3부터 시작해서 넓이의 제곱근의 수까지 반복한다.
    for i in range(3, int(area ** .5) + 1):
        # 넓이를 나누어 떨어지게 하는 수가 세로 길이가 될 수 있는 후보이다.
        if area % i == 0:
            # 나누어 떨어지게 한 수와 그 때의 몫으로 가로 세로 길이를 선언한다.
            r, c = i, area // i
            # 가로와 세로에서 각각 2를 뺀 수의 곱이 yellow 의 넓이와 같은 경우를 찾는다.
            if (r - 2) * (c - 2) == yellow:
                # 그 때의 큰 값이 가로, 작은 값이 세로이다.
                answer = [max(r, c), min(r, c)]
                break
                
    return answer