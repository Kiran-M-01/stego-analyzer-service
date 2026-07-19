from utils.channel_extractor import ChannelExtractor

from analyzer.chi_square import ChiSquareAnalyzer
from analyzer.entropy import EntropyAnalyzer
from analyzer.variance import VarianceAnalyzer
from analyzer.scorer import ConfidenceScorer
from analyzer.pixel_difference import PixelDifferenceAnalyzer


class ReportAnalyzer:

    @staticmethod
    def analyze(image):

        print("=" * 50)
        print(image.shape)
        print(image.dtype)
        print(image.min())
        print(image.max())
        print("=" * 50)
        print(image[0:5, 0:5])

        channels = {
            "red": ChannelExtractor.red(image),
            "green": ChannelExtractor.green(image),
            "blue": ChannelExtractor.blue(image),
        }

        report = {}

        for name, channel in channels.items():

            pixel_difference = PixelDifferenceAnalyzer.calculate(channel)

            print("\n========================")
            print(name.upper())
            print("========================")
            print(pixel_difference)

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
            "summary": summary,
            "channels": report
}       