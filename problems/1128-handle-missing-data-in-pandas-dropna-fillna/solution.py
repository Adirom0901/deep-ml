import pandas as pd

def solution(df):
    # 1. Drop columns with more than 50% missing values
    df = df.dropna(axis=1, thresh=len(df) * 0.5)

    # 2. Drop rows with more than 50% missing values
    df = df.dropna(axis=0, thresh=df.shape[1] * 0.5)

    # 3. Fill missing values
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0])

    return df