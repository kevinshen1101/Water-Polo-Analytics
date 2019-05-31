import pandas as pd
import numpy as np

def shot_with_assists_dict(df):
    freq_dict = {}
    for i in range(1, 7):
        for j in range(1, 7):
            if i == j: continue
            filter_df = df[(df['Shooter Position'] == i) & (df["Assisting Player Position"] == j)]
            goals = filter_df['Goal'].sum()
            shots = filter_df.shape[0]
            percentage = 0 if goals == 0 else goals/shots
            freq_dict[(i, j)] = (goals, shots, percentage)
    return freq_dict

