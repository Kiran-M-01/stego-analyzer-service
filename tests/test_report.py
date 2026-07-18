from pprint import pprint

from utils.image_loader import ImageLoader
from analyzer.report import ReportAnalyzer


image, _ = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

report = ReportAnalyzer.analyze(image)

print("\nAnalysis Report")
print("=" * 60)

pprint(report)