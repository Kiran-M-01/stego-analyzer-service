import numpy as np


class HistogramAnalyzer:

    @staticmethod
    def calculate(channel: np.ndarray):
        """
        Calculate histogram for a single image channel.

        Parameters:
            channel (np.ndarray): 2D array representing one color channel.

        Returns:
            np.ndarray: Histogram with 256 bins.
        """
        histogram, _ = np.histogram(
            channel,
            bins=256,
            range=(0, 256)
        )

        return histogram