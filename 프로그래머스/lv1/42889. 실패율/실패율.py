from collections import Counter

def solution(N, stages):
    successed_stage_player_count = Counter(stages)
    fail_rates_stage_tb = {}
    reached_stage_player_count = len(stages)
    
    for stage in range(1, N+1):
        if reached_stage_player_count != 0:
            fail_rate = successed_stage_player_count[stage] / reached_stage_player_count
            fail_rates_stage_tb[stage] = fail_rate
            reached_stage_player_count -= successed_stage_player_count[stage]
        else:
            fail_rates_stage_tb[stage] = 0
    
    return sorted(fail_rates_stage_tb, key=lambda x: fail_rates_stage_tb[x], reverse=True)