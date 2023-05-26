def solution(s):
    ans, pair = 0, {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            if v in pair: stack.append(v)
            elif not stack or v != pair[stack.pop()]: 
                iscorrect = False
                break

        ans += int(iscorrect and not stack)
        s = s[1:]+s[0]

    return ans