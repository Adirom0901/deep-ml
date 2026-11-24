import pandas as pd

def solution(df):
    df = df[df["status"] == "completed"]

    df = df.groupby("region")["amount"].sum()

    df = df.sort_values(ascending=False)

    if len(df) >= 10:
        df = df.iloc[:10]
    df=df.reset_index(drop=False)
    return df
    pass