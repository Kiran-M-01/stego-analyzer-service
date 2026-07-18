import numpy as np


class EntropyAnalyzer:

    @staticmethod
    def calculate(channel: np.ndarray) -> float:
        """
        Calculate Shannon entropy for a single image channel.
        """

        histogram = np.bincount(channel.flatten(), minlength=256)

        probabilities = histogram / histogram.sum()

        # Remove zero probabilities to avoid log2(0)
        probabilities = probabilities[probabilities > 0]

        entropy = -np.sum(
            probabilities * np.log2(probabilities)
        )

        return float(entropy)