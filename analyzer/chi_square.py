from scipy.stats import chi2

from analyzer.models import (
    PairStatistics,
    ChiSquareResult
)


class ChiSquareAnalyzer:

    @staticmethod
    def calculate_statistic(
        pair_statistics: list[PairStatistics]
    ) -> float:

        chi_square = 0.0

        for pair in pair_statistics:

            if pair.expected == 0:
                continue

            chi_square += (
                (pair.observed_even - pair.expected) ** 2
            ) / pair.expected

            chi_square += (
                (pair.observed_odd - pair.expected) ** 2
            ) / pair.expected

        return chi_square

    @staticmethod
    def calculate_p_value(
        statistic: float,
        degrees_of_freedom: int = 127
    ) -> float:

        return chi2.sf(
            statistic,
            degrees_of_freedom
        )

    @staticmethod
    def analyze_channel(
        pair_statistics: list[PairStatistics]
    ) -> ChiSquareResult:

        statistic = (
            ChiSquareAnalyzer.calculate_statistic(
                pair_statistics
            )
        )

        p_value = (
            ChiSquareAnalyzer.calculate_p_value(
                statistic
            )
        )

        suspicious = p_value < 0.05

        return ChiSquareResult(
            statistic=float(statistic),
            p_value=float(p_value),
            suspicious=None
        )