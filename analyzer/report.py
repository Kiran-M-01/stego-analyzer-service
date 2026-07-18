from utils.channel_extractor import ChannelExtractor

from analyzer.histogram import HistogramAnalyzer
from analyzer.statistics import ChiSquareStatistics
from analyzer.chi_square import ChiSquareAnalyzer
from analyzer.entropy import EntropyAnalyzer
from analyzer.variance import VarianceAnalyzer


class ReportAnalyzer:

    @staticmethod
    def analyze(image):

        channels = {
            "red": ChannelExtractor.red(image),
            "green": ChannelExtractor.green(image),
            "blue": ChannelExtractor.blue(image),
        }

        report = {}

        for name, channel in channels.items():

            histogram = HistogramAnalyzer.calculate(channel)

            pair_statistics = (
                ChiSquareStatistics.observed_expected(
                    histogram
                )
            )

            chi_square = (
                ChiSquareAnalyzer.analyze_channel(
                    pair_statistics
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
            }

        return report