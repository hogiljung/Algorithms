def solution(array, n):
    array.append(n)
    array_sorted = sorted(array)
    idx_n = array_sorted.index(n)
    if idx_n == 0:
        return array_sorted[idx_n+1]
    if idx_n == len(array_sorted)-1:
        return array_sorted[idx_n-1]
    pre_n, next_n = array_sorted[idx_n-1], array_sorted[idx_n+1]

    return pre_n if (pre_n + next_n) // 2 >= n else next_n