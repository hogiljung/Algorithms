def solution(chicken):
    service = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        service += chicken
        chicken += mod
    return service