import numpy as np
from scipy.stats import chi2

from analyzer.models import (
    PairStatistics,
    ChiSquareResult
)
from analyzer.histogram import HistogramAnalyzer
from analyzer.statistics import ChiSquareStatistics


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
        pair_statistics: list[PairStatistics]
    ) -> float:

        valid_pairs = sum(
            1
            for pair in pair_statistics
            if pair.expected > 0
        )

        degrees_of_freedom = max(valid_pairs - 1, 1)

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
                statistic,
                pair_statistics
            )
        )

        # BUG FIX: this was `p_value < 0.05`, which is backwards.
        # The null hypothesis here is "the pairs ARE equalized" (i.e.
        # embedding occurred) -- a HIGH p-value means the histogram
        # matches that pattern closely, which is the suspicious case.
        suspicious = p_value > 0.95

        return ChiSquareResult(
            statistic=float(statistic),
            p_value=float(p_value),
            # BUG FIX: this was hardcoded to None, so the field was
            # always empty regardless of the computed value above.
            suspicious=bool(suspicious)
        )

    @staticmethod
    def analyze_windowed(
        channel: np.ndarray,
        num_windows: int = 128
    ) -> ChiSquareResult:

        flat = channel.flatten()
        chunk_size = max(1, len(flat) // num_windows)

        best = None

        for i in range(num_windows):

            start = i * chunk_size
            end = len(flat) if i == num_windows - 1 else start + chunk_size

            chunk = flat[start:end]

            if chunk.size == 0:
                continue

            histogram = HistogramAnalyzer.calculate(chunk)

            pair_statistics = (
                ChiSquareStatistics.observed_expected(histogram)
            )

            result = ChiSquareAnalyzer.analyze_channel(pair_statistics)

            if best is None or result.p_value > best.p_value:
                best = result

        return best