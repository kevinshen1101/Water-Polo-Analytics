import pandas as pd


def get_miss_breakdown(df):
    goalie_block = sum(df['Block'] == 'goalie')
    field_block = sum(df['Block'] == 'field')
    turn_overs = sum(df['Turnover'] == 1)
    non_goal = sum(df['Goal'] == 0)
    return {'goalie': goalie_block, 'field': field_block,
            'missed': non_goal - goalie_block - field_block - turn_overs, "turnovers": turn_overs}

