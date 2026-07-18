from utils.image_loader import ImageLoader
from analyzer.histogram import HistogramAnalyzer

image, metadata = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

red_hist = HistogramAnalyzer.calculate(red)
green_hist = HistogramAnalyzer.calculate(green)
blue_hist = HistogramAnalyzer.calculate(blue)

print("Red Histogram Length:", len(red_hist))
print("Green Histogram Length:", len(green_hist))
print("Blue Histogram Length:", len(blue_hist))

print("\nFirst 10 values of Red Histogram:")
print(red_hist[:10])