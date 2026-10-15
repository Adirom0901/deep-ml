import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    maxx= max(scores)

    l= [math.e**(s-maxx) for s in scores]

    summ= sum(l)
    l= [i/summ for i in l]
    return l