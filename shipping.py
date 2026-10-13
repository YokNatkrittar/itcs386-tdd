import math

def shipping_fee(weight_kg):
    """...keep your docstring exactly as it is..."""
    if weight_kg <= 0:
        raise ValueError("weight must be more than 0 kg")
    if weight_kg <= 1:
        return 40
    if weight_kg <= 5:
        return 60
    extra = math.ceil(weight_kg - 5)
    return 60 + 10 * extra