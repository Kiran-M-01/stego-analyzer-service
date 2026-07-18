from utils.image_loader import ImageLoader
from utils.channel_extractor import ChannelExtractor

from analyzer.histogram import HistogramAnalyzer
from analyzer.statistics import ChiSquareStatistics

image, _ = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

blue = ChannelExtractor.blue(image)

histogram = HistogramAnalyzer.calculate(
    blue
)

statistics = (
    ChiSquareStatistics
    .observed_expected(histogram)
)

print("Total Pairs:", len(statistics))

print()

print("First 10 Pair Statistics")

print("-" * 40)

for pair in statistics[:10]:
    print(pair)