from itertools import permutations

def solution(numbers):
    answer = 0
    
    # 소수 판별 함수 생성
    def is_prime(n):
        if n <= 1:
            return False
        
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                return False
        return True
    
    # 소수 판별을 끝낸 숫자를 담을 집합, 중복을 제거하기 위해 set로 선언
    checked_number = set()
    
    # 한자리부터 모든 자리까지의 수열을 만들기 위한 반복문
    for i in range(1, len(numbers) + 1):
        for p_arr in permutations(numbers, i):
            # 수열을 숫자로 변환
            num = int(''.join(p_arr))
            # 확인한 숫자라면 다음 수열 확인
            if num in checked_number:
                continue
            # 확인한 숫자 추가
            checked_number.add(num)
            # 소수 판별 후 카운트 증가
            if is_prime(num):
                answer += 1
    
    return answer