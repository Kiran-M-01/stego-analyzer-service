from PIL import Image
import numpy as np


class ImageLoader:

    @staticmethod
    def load_image(source):

        image = Image.open(source).convert("RGB")

        image_array = np.array(image)

        metadata = {
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
        }

        return image_array, metadata