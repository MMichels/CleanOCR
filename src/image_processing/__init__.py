import cv2
import numpy as np
from src.services.image_service import ImageService


class ImageIoManager:
    def __init__(self, id):
        self.id = id
        self.service = ImageService()

    def open_dirty_image(self):
        image_bytes = self.service.load_dirty_image_bytes(self.id)
        image_array = np.fromstring(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, flags=1)
        return image

    def save_clean_image(self, image):
        self.service.save_clean_image(self.id, image)
