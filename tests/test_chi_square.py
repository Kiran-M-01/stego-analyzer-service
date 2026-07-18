from utils.image_loader import ImageLoader
from utils.channel_extractor import ChannelExtractor

from analyzer.histogram import HistogramAnalyzer
from analyzer.statistics import ChiSquareStatistics
from analyzer.chi_square import ChiSquareAnalyzer


image, _ = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

blue = ChannelExtractor.blue(image)

histogram = HistogramAnalyzer.calculate(
    blue
)

statistics = (
    ChiSquareStatistics.observed_expected(
        histogram
    )
)

result = (
    ChiSquareAnalyzer.analyze_channel(
        statistics
    )
)

print()

print("Chi-Square Analysis")

print("-" * 40)

print(result)