import base64
import cv2
import os

from sqlalchemy.orm import Session
from models import get_session
from models.image import ImageModel

DIRTY_IMAGE_PATH = "./resources/1.dirty/"
CLANED_IMAGE_PATH = "./resources/2.cleaned/"

os.makedirs(DIRTY_IMAGE_PATH, exist_ok=True)
os.makedirs(CLANED_IMAGE_PATH, exist_ok=True)


class ImageService:
    model: ImageModel
    session: Session

    def __init__(self, image_model=None):
        self.session = get_session()
        self.model = image_model

    def save_dirty_image(self):
        if self.model.id is None:
            self.session.add(self.model)
            self.session.commit()

        path = os.path.join(DIRTY_IMAGE_PATH, str(self.model.id) + ".png")
        with open(path, "wb") as f:
            f.write(
                base64.b64decode(
                    self.model.base64_encoded_image
                )
            )

        return True

    def load_dirty_image_bytes(self, id):
        image_bytes = []
        image_path = os.path.join(DIRTY_IMAGE_PATH, str(id) + ".png")
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        return image_bytes

    def save_clean_image(self, id, image):
        image_path = os.path.join(CLANED_IMAGE_PATH, str(id) + ".png")
        cv2.imwrite(image_path, image)

    def get_total_images(self):
        total = ImageModel.query.count()
        return total

    def get_navigate_images(self, index, count):
        images = ImageModel.query.filter(
            ImageModel.id >= index
        ).limit(count).all()
        return images
