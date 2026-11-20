def birthday_problem(n: int, days: int = 365) -> float:
    """
    Calculate the probability that at least two people share the same birthday.
    
    Args:
        n: Number of people in the group
        days: Number of days in a year (default 365)
    
    Returns:
        float: Probability of at least one shared birthday, rounded to 4 decimal places
    """
    # Your code here
    if n<=0:
        return 0 
    if n>days:
        return 1
    
    s=days
    tot=1.0

    for i in range(n):
        s=days-i
        tot= tot*s/days
    return 1-tot


    
    pass