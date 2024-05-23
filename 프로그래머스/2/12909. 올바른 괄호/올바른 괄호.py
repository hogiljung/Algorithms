def solution(s):
    answer = True
    
    # 문자를 넣기 위한 스택 초기화
    check = []
    
    # 문자열을 순회
    for c in s:
        # 문자열이 ( 인 경우 배열에 넣는다.
        if c == '(':
            check.append(c)
        # 문자열이 ) 인 경우
        elif c == ')':
            # 배열이 비어있다면 ( 가 들어있지 않으므로 올바르지 않음
            if not check:
                answer = False
                break
            # 배열의 마지막 꺼내 값을 확인한다. ( 가 아니라면 올바르지 않음
            if check.pop() != '(':
                answer = False
                break
    
    # 모든 문자열을 확인한 후 배열에 값이 남아있다면 올바르지 않음
    if check:
        answer = False

    return answer