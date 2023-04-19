def solution(emergency):
    emergency_sorted = sorted(emergency, reverse=True)
    emergency_dict = {key: value+1 for value, key in enumerate(emergency_sorted)}
    return [emergency_dict[key] for key in emergency]