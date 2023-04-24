def solution(chicken):
    coupon = chicken
    total_service = 0
    while coupon // 10 != 0:
        service, coupon = divmod(coupon, 10)
        total_service += service
        coupon += service
    return total_service