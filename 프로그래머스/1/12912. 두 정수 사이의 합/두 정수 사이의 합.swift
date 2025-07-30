func solution(_ a:Int, _ b:Int) -> Int64 {
    var count = a < b ? b-a+1 : a-b+1
    return Int64((a+b) * count / 2)
}
