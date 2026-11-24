import pandas as pd

def solution(df1, df2, df3):
    df4= df1.merge(df2,how='inner',on='emp_id')
    df5=df4.merge(df3,how='left',on='emp_id')
    df= df5.reset_index(drop=True)
    return df
    pass