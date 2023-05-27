def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = 0
        for j in range(i, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)