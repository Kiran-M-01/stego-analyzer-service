import numpy as np


class ChannelExtractor:
    """
    Utility class for extracting RGB channels
    from an image array.
    """

    @staticmethod
    def red(image: np.ndarray) -> np.ndarray:
        return image[:, :, 0]

    @staticmethod
    def green(image: np.ndarray) -> np.ndarray:
        return image[:, :, 1]

    @staticmethod
    def blue(image: np.ndarray) -> np.ndarray:
        return image[:, :, 2]

    @staticmethod
    def all_channels(image: np.ndarray):
        return {
            "red": image[:, :, 0],
            "green": image[:, :, 1],
            "blue": image[:, :, 2],
        }