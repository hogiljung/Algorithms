import Foundation

struct Stack {
    private var arr = Array<Int>()

    mutating func push(_ n: Int) -> Void {
        arr.append(n)
    }

    mutating func pop() -> Int {
        let last = arr.popLast()
        
        return last == nil ? -1 : last!
    }

    var top: Int {
        return empty == 1 ? -1 : arr.last!
    }

    var empty: Int {
        return arr.isEmpty ? 1 : 0
    }

    var size: Int {
        return arr.count
    }
}

func solution() {
    var s = Stack()
    let commandCount = Int(readLine()!)!

    for _ in (1...commandCount) {
        let command = readLine()!.components(separatedBy: " ")

        switch command[0] {
            case "push":
                s.push(Int(command[1])!)
            case "pop":
                print(s.pop())
            case "size":
                print(s.size)
            case "top":
                print(s.top)
            case "empty":
                print(s.empty)
            default: continue
        }
    }
}

solution()