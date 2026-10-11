import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    samples= [i for i in range(n_samples)]
    if shuffle:
        np.random.shuffle(samples)
    
    l=[]
    lenn= n_samples//k
    extra=0
    if n_samples%k!=0:
        extra= n_samples%k
    pointer=0
    for iterr in range(k):
        lis=[]
        for i in range(lenn):
            lis.append(samples[pointer])
            pointer+=1
        l.append(lis)
    for ex in range(extra):
        l[0].append(samples[pointer])
        pointer+=1
    ans=[]
    for z in range(k):
        test= l[z]
        train=[]
        for i in range(z):
            train.extend(l[i])
        for j in range(z+1,len(l)):
            train.extend(l[j])

        ans.append((train,test))

    return ans
    

    pass