from analyzer.pairs import PairGenerator
from analyzer.models import PairStatistics


class ChiSquareStatistics:
    """
    Computes observed and expected frequencies
    for Pair-of-Values analysis.
    """

    @staticmethod
    def observed_expected(histogram):
        """
        Parameters:
            histogram (np.ndarray): Histogram with 256 bins.

        Returns:
            list of tuples:
            (observed_even,
             observed_odd,
             expected)
        """

        results = []

        for even, odd in PairGenerator.generate():

            observed_even = histogram[even]
            observed_odd = histogram[odd]

            expected = (
                observed_even + observed_odd
            ) / 2.0

            results.append(
                PairStatistics(
                    even_value=even,
                    odd_value=odd,
                    observed_even=int(observed_even),
                    observed_odd=int(observed_odd),
                    expected=float(expected)
                )
            )

        return results