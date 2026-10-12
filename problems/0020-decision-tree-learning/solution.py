import math
from collections import Counter,defaultdict

def calculate_entropy(labels: list) -> float:
    """Calculate the entropy of a list of labels."""
    counts = Counter(labels)

    n=len(labels)

    if n==0:
        return 0.0
    ent=0.0

    for c in counts.values():
        p=c/n 
        ent-=p*(math.log2(p))
    return ent


    pass

def calculate_information_gain(examples: list[dict], attr: str, target_attr: str) -> float:
    """Calculate the information gain of splitting on attr."""
    # Your code here

    parent_labels=[e[target_attr] for e in examples]
    parent_ent= calculate_entropy(parent_labels)

    groups=defaultdict(list)

    for e in examples:
        groups[e[attr]].append(e)

    weighted_ent= 0.0
    n=len(examples)

    for group in groups.values():
        labels= [e[target_attr] for e in group]

        weighted_ent+=(
            len(group)/n * calculate_entropy(labels)
        )
    
    return parent_ent-weighted_ent
        
     
    pass

def majority_class(examples: list[dict], target_attr: str) -> str:
    """Return the majority class. Break ties alphabetically."""
    # Your code here
    counts= Counter(e[target_attr] for e in examples)

    return min(counts,key=lambda label:(-counts[label],label))

def sort_tree(tree):
    if not isinstance(tree, dict):
        return tree

    return {
        key: sort_tree(tree[key])
        for key in sorted(tree)
    }

def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:
    """Build a decision tree using the ID3 algorithm."""
    # Your code here
    if not examples:
        return {}

    labels= [e[target_attr] for e in examples]
    unique_labels= set(labels)

    if len(unique_labels)==1:
        return labels[0]
    
    if not attributes:
        return majority_class(examples,target_attr)

    best_attr = max(
        attributes,
        key=lambda a: calculate_information_gain(
            examples, a, target_attr
        )
    )

    tree= {
        best_attr:{}
    }

    remaining_attr= [attr for attr in attributes if attr!=best_attr]
    groups=defaultdict(list)
    for e in examples:
        groups[e[best_attr]].append(e)

    for value,subset in groups.items():
        tree[best_attr][value]= learn_decision_tree(
            subset,
            remaining_attr,
            target_attr
        )

    return sort_tree(tree)






    pass