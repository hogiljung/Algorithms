import Foundation

var s = [Int]()
let tCase = Int(readLine()!)!
for _ in 1...tCase {
    let commandParts = readLine()!.split(separator: " ")

    switch commandParts[0] {
        case "push":
            s.append(Int(commandParts[1])!)
        case "pop":
            s.isEmpty ? print("-1") : print(s.removeLast())
        case "size":
            print(s.count)
        case "empty":
            s.isEmpty ? print("1") : print("0")
        case "top":
            s.last == nil ? print("-1") : print(s.last!)
        default:
            continue
    }
}