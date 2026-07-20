from utils.channel_extractor import ChannelExtractor

from analyzer.chi_square import ChiSquareAnalyzer
from analyzer.entropy import EntropyAnalyzer
from analyzer.variance import VarianceAnalyzer
from analyzer.scorer import ConfidenceScorer
from analyzer.pixel_difference import PixelDifferenceAnalyzer


class ReportAnalyzer:

    @staticmethod
    def analyze(image):

        channels = {
            "red": ChannelExtractor.red(image),
            "green": ChannelExtractor.green(image),
            "blue": ChannelExtractor.blue(image),
        }

        height, width = image.shape[:2]

        metadata = {
            "width": width,
            "height": height,
            "channels": image.shape[2] if len(image.shape) == 3 else 1,
            "dtype": str(image.dtype)
        }

        report = {}

        for name, channel in channels.items():

            pixel_difference = PixelDifferenceAnalyzer.calculate(channel)


            # Windowed, not whole-image: a real hidden message is small
            # relative to the image, so whole-image chi-square dilutes
            # the signal to ~0 even when something IS embedded.
            chi_square = (
                ChiSquareAnalyzer.analyze_windowed(
                    channel
                )
            )

            entropy = (
                EntropyAnalyzer.calculate(
                    channel
                )
            )

            variance = (
                VarianceAnalyzer.calculate(
                    channel
                )
            )

            report[name] = {
                "chi_square": {
                    "statistic": chi_square.statistic,
                    "p_value": chi_square.p_value,
                    "suspicious": chi_square.suspicious,
                },
                "entropy": entropy,
                "variance": variance,
                "pixel_difference": pixel_difference


            }
            

        summary = ConfidenceScorer.calculate(report)

        return {
            "metadata": metadata,
            "summary": summary,
            "channels": report
}       