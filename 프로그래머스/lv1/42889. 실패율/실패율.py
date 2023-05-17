def solution(N, stages):
    playing_stage_tb = {}
    stages_sorted = sorted(stages)
    stages_sorted_set = set(stages_sorted)
    fail_rates_stage_tb = {}
    
    for stage in stages:
        playing_stage_tb.setdefault(stage, 0)
        playing_stage_tb[stage] += 1
        
    for stage in range(1, N+1):
        if stage in playing_stage_tb:
            fail_rate = playing_stage_tb[stage] / (len(stages) - stages_sorted.index(stage))
            fail_rates_stage_tb[stage] = fail_rate
        else:
            fail_rates_stage_tb[stage] = 0
    
    return [fail_rates_stage[0] for fail_rates_stage in sorted(fail_rates_stage_tb.items(), key=lambda x: x[1], reverse=True)]