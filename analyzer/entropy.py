import numpy as np


class EntropyAnalyzer:

    @staticmethod
    def calculate(channel: np.ndarray) -> float:
        """
        Calculate Shannon entropy of the Least Significant Bit (LSB) plane.
        Returns a value between 0 and 1.
        """

        # Extract LSB plane
        lsb = channel & 1

        # Count 0s and 1s
        histogram = np.bincount(lsb.flatten(), minlength=2)

        total = histogram.sum()

        if total == 0:
            return 0.0

        probabilities = histogram / total
        probabilities = probabilities[probabilities > 0]

        entropy = -np.sum(probabilities * np.log2(probabilities))

        return float(entropy)