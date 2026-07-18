from utils.image_loader import ImageLoader

image, metadata = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

print(metadata)

print("-" * 40)

for key, value in metadata.items():
    print(f"{key}: {value}")

print("\nImage Array Shape:", image.shape)