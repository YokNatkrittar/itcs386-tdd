# test_shipping.py
import pytest
from shipping import shipping_fee


@pytest.mark.parametrize("weight, expected", [
    (0.5, 40),    # inside rule 2
    # BUG: breaks Rule 2 (exactly 1 kg must cost 40; code returns 60)
    (1, 40),      # edge: exactly 1 kg
    (1.1, 60),    # just above 1 kg, rule 3
    (3, 60),      # inside rule 3
    (5, 60),      # edge: exactly 5 kg, rule 3
    # BUG: breaks Rule 4 (5.2 kg has started a 6th kg, so 70; code returns 60)
    (5.2, 70),    # rule 4, example given in the docstring
    (6, 70),      # rule 4, exactly 1 kg above 5
    # BUG: breaks Rule 4 (6.5 kg has started a 2nd extra kg, so 80; code returns 70)
    (6.5, 80),    # rule 4, partial kilogram
    (10, 110),    # rule 4, exactly 5 kg above 5
])
def test_shipping_fee(weight, expected):
    assert shipping_fee(weight) == expected


# BUG: breaks Rule 1 (0 kg must raise ValueError; code returns 40)
def test_zero_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(0)


def test_negative_weight_is_rejected():
    with pytest.raises(ValueError):
        shipping_fee(-2)