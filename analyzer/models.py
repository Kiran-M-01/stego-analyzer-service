from dataclasses import dataclass


@dataclass
class PairStatistics:
    """
    Stores statistical information for one Pair-of-Values (PoV).
    """

    even_value: int
    odd_value: int

    observed_even: int
    observed_odd: int

    expected: float


@dataclass
class ChiSquareResult:
    """
    Result of the Chi-Square analysis for a single color channel.
    """

    statistic: float
    p_value: float
    suspicious: bool