def find_duplicates(records):
    # records: list of hashable items (ints or strings)
    # return a list of values that appear more than once,
    # each listed once, ordered by the position of its second occurrence
    mpp={}
    ans=[]
    for i in records:
        if i in mpp and mpp[i]==1:
            ans.append(i)
            mpp[i]=2
        elif i not in mpp:
            mpp[i]=1
    return ans
        
    pass