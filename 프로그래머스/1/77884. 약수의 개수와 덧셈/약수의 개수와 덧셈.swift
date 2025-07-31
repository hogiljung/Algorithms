import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    return (left...right).reduce(0) { 
        isPerfectSquare($1) ? $0 - $1 : $0 + $1 
    }
}

func isPerfectSquare(_ num: Int) -> Bool {
    let root = Int(sqrt(Double(num)))
    return root * root == num
}