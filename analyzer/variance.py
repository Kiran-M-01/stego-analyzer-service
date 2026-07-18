import numpy as np


class VarianceAnalyzer:

    @staticmethod
    def calculate(channel: np.ndarray) -> float:
        """
        Calculate the variance of the Least Significant Bit (LSB) plane.
        """

        lsb = channel & 1

        return float(np.var(lsb))