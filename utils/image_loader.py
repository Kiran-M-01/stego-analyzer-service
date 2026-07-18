from PIL import Image
import numpy as np


class ImageLoader:

    @staticmethod
    def load_image(image_path: str):

        image = Image.open(image_path)

        image = image.convert("RGB")

        image_array = np.array(image)

        metadata = {
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
            "shape": image_array.shape,
            "dtype": str(image_array.dtype)
        }

        return image_array, metadata