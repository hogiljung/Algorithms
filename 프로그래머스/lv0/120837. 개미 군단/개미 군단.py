def solution(hp):
    answer = 0
    ant_damages = [5, 3, 1]
    for damage in ant_damages:
        count, hp = divmod(hp, damage)
        answer += count
    return answer