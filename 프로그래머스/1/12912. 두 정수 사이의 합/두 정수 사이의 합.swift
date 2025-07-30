func solution(_ a:Int, _ b:Int) -> Int64 {
    if a == b {
        return Int64(a)
    }
    
    var count: Int
    if a < b {
        count = b-a+1
    } else {
        count = a-b+1
    }
    
    return Int64((a+b) * count / 2)
}
