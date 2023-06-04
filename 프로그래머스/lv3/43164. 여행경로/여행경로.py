from collections import defaultdict
answer = []
END = False
def solution(tickets):
    N = len(tickets)
    used = [False] * N
    tickets = [(ticket, i) for i, ticket in enumerate(sorted(tickets, key=lambda x: (x[0], x[1])))]
    dfs('ICN', used, tickets)
    
    return answer

def dfs(current, used, tickets):
    global answer, END
    answer.append(current)
    if all(used):
        END = True
        return
    
    for next_city, ticket_idx in get_adjacent(current, used, tickets):
        if not used[ticket_idx]:
            used[ticket_idx] = True
            dfs(next_city, used, tickets)
            if not END:
                answer.pop()
                used[ticket_idx] = False
            else:
                return

def get_adjacent(current, used, tickets):
    for ticket, i in tickets:
        if ticket[0] == current and not used[i]:
            yield ticket[1], i
            