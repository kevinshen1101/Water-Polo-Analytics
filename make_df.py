import pandas as pd
import os

def make_df(path):
    start = os.curdir
    os.chdir(path)
    files = os.listdir()
    df = pd.read_excel(files[1])
    # start at 1 bc list starts with [.DS_Store ..] -- hack solution but works for now
    for file in files[2:]:
        df_tmp = pd.read_excel(file)
        df = pd.concat([df, df_tmp], sort=False)
    os.chdir(start)
    return df
