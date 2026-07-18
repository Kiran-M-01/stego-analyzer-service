from utils.image_loader import ImageLoader
from utils.channel_extractor import ChannelExtractor

from analyzer.entropy import EntropyAnalyzer


image, metadata = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

red = ChannelExtractor.red(image)
green = ChannelExtractor.green(image)
blue = ChannelExtractor.blue(image)

print("\nEntropy Analysis")
print("-" * 40)

print(f"Red   : {EntropyAnalyzer.calculate(red):.4f}")
print(f"Green : {EntropyAnalyzer.calculate(green):.4f}")
print(f"Blue  : {EntropyAnalyzer.calculate(blue):.4f}")