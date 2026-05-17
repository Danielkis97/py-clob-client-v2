from math import floor, ceil
from decimal import Decimal, ROUND_HALF_EVEN

def round_down(x: float, sig_digits: int) -> float:
    return floor(x * (10**sig_digits)) / (10**sig_digits)


def round_normal(x: float, sig_digits: int) -> float:
    return round(x * (10**sig_digits)) / (10**sig_digits)


def round_up(x: float, sig_digits: int) -> float:
    return ceil(x * (10**sig_digits)) / (10**sig_digits)


def to_token_decimals(x: float) -> int:
    return int(
        (Decimal(str(x)) * Decimal("1000000")).to_integral_value(
            rounding=ROUND_HALF_EVEN
        )
    )

def decimal_places(x: float) -> int:
    return abs(Decimal(x.__str__()).as_tuple().exponent)
