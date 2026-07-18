from utils.image_loader import ImageLoader
from utils.channel_extractor import ChannelExtractor

image, metadata = ImageLoader.load_image(
    "sample_images/clean/sample.png"
)

channels = ChannelExtractor.all_channels(image)

print("Image Shape:", image.shape)

for name, channel in channels.items():
    print(f"{name.capitalize()} Channel Shape: {channel.shape}")