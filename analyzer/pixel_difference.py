import numpy as np


class PixelDifferenceAnalyzer:
    """
    Analyze local pixel differences.

    LSB embedding slightly disturbs the natural similarity
    between neighboring pixels.
    """

    @staticmethod
    def calculate(channel: np.ndarray) -> dict:

        # Horizontal differences
        horizontal = np.abs(
            channel[:, 1:].astype(np.int16) -
            channel[:, :-1].astype(np.int16)
        )

        # Vertical differences
        vertical = np.abs(
            channel[1:, :].astype(np.int16) -
            channel[:-1, :].astype(np.int16)
        )

        mean_difference = (
            horizontal.mean() +
            vertical.mean()
        ) / 2

        std_difference = (
            horizontal.std() +
            vertical.std()
        ) / 2

        return {
            "mean_difference": float(mean_difference),
            "std_difference": float(std_difference)
        }