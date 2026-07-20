from stegano import lsb
from PIL import Image
import numpy as np

# Verify the message exists
message = lsb.reveal("stego.png")
print("Recovered message:")
print(message[:100], "...")   # print first 100 chars

# Compare cover and stego pixel by pixel
cover = np.array(Image.open("cover.png").convert("RGB"))
stego = np.array(Image.open("stego.png").convert("RGB"))

print("Images identical:", np.array_equal(cover, stego))

diff = np.count_nonzero(cover != stego)
print("Different channel values:", diff)