import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer = [Int]()
    
    for c in commands {
        let subArr = array[c[0]-1...c[1]-1].sorted()
        answer.append(subArr[c[2]-1])
    }
    
    return answer
}