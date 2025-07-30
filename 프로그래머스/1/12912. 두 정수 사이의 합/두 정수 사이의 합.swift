func solution(_ a:Int, _ b:Int) -> Int64 {
    if a > b {
        return getSum(b, a)
    } else if a == b {
        return Int64(a)
    } else {
        return getSum(a, b)
    }
}

func getSum(_ a: Int, _ b: Int) -> Int64 {
    var answer = Int64(a)
    for v in a+1...b {
        answer += Int64(v)
    }
    return answer
}