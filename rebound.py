import pandas as np

'returns {"non-rebound: (goals, shots, %), "rebounds": (goals, shots, %), ' \
'"stats": (#non-rebound posetions, #rebounds_posetions, %non-rebounds_posetions, %rebounds_posetions, %plays_led to rebound)}'
def get_rebounds(df):
    non_rebound = df[df['Rebound'] == 0]
    rebound = df[df['Rebound'] == 1]
    non_rebound_tuple = make_goal_tuple(non_rebound)
    rebound_tuple = make_goal_tuple(rebound)
    non_rebound_pos = non_rebound_tuple[1]
    rebound_pos = rebound_tuple[1]
    total_pos = non_rebound_pos + rebound_pos
    return {"non-rebound": non_rebound_tuple, "rebound": rebound_tuple,
            "stats": (non_rebound_pos, rebound_pos, non_rebound_pos/total_pos, rebound_pos/total_pos, rebound_pos/non_rebound_pos)}



def make_goal_tuple(df):
    goals = df['Goal'].sum()
    shots = df.shape[0]
    percentage = 0 if goals == 0 else goals/shots
    return (goals, shots, percentage)


