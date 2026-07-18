from utils.image_loader import ImageLoader
from utils.channel_extractor import ChannelExtractor

from analyzer.variance import VarianceAnalyzer


image, _ = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

print("\nLSB Variance")
print("-" * 40)

print(f"Red   : {VarianceAnalyzer.calculate(ChannelExtractor.red(image)):.6f}")
print(f"Green : {VarianceAnalyzer.calculate(ChannelExtractor.green(image)):.6f}")
print(f"Blue  : {VarianceAnalyzer.calculate(ChannelExtractor.blue(image)):.6f}")