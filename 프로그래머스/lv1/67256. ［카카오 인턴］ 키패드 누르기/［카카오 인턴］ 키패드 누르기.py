def solution(numbers, hand):
    answer = ''
    l, r = [0, 3], [2, 3]
    key_xy_dict = {1:[0,0], 2:[1,0], 3:[2,0], 4:[0,1], 5:[1,1], 6:[2,1], 7:[0,2], 8:[1,2], 9:[2,2], 0:[1,3]}

    for n in numbers:
        push = ''
        key_xy = key_xy_dict[n]
        if n in [1, 4, 7]:
            push = 'L'
        elif n in [3, 6, 9]:
            push = 'R'
        else:
            d_l = abs(key_xy[0] - l[0]) + abs(key_xy[1] - l[1])
            d_r = abs(key_xy[0] - r[0]) + abs(key_xy[1] - r[1])
            
            if d_l < d_r:
                push = 'L'
            elif d_l > d_r:
                push = 'R'
            else:
                push = 'L' if hand == 'left' else 'R'
            
        if push == 'L':
            l = key_xy
        elif push == 'R':
            r = key_xy
            
        answer += push
    return answer