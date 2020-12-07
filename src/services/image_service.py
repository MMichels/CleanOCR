import base64
import cv2
import os
import numpy as np
from sqlalchemy.orm import Session
from models import get_session
from models.image import ImageModel

DIRTY_IMAGE_PATH = "./resources/1.dirty/"
CLANED_IMAGE_PATH = "./resources/2.cleaned/"

os.makedirs(DIRTY_IMAGE_PATH, exist_ok=True)
os.makedirs(CLANED_IMAGE_PATH, exist_ok=True)


class ImageService:
    model: ImageModel = None
    session: Session

    def __init__(self, image_model=None, id: int = None):
        self.session = get_session()
        if image_model is not None:
            self.model = image_model
        elif id is not None:
            self.model = self.session.query(ImageModel).filter(ImageModel.id==id).first()

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

    def load_dirty_image_bytes(self, id=None):
        if id is None and self.model is not None:
            id = self.model.id
        image_bytes = []
        image_path = os.path.join(DIRTY_IMAGE_PATH, str(id) + ".png")
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        return image_bytes

    def load_dirty_image(self, id=None):
        if id is None and self.model is not None:
            id = self.model.id
        image_bytes = self.load_dirty_image_bytes(id)
        image_array = np.fromstring(image_bytes, np.uint8)
        image = cv2.imdecode(image_array, flags=1)
        return image

    def save_clean_image(self, image, id=None):
        if id is None and self.model is not None:
            id = self.model.id
        image_path = os.path.join(CLANED_IMAGE_PATH, str(id) + ".png")
        cv2.imwrite(image_path, image)

        with open(image_path, "rb") as f:
            self.model.base64_encoded_processed_image = base64.b64encode(f.read())

        self.model.processed = True
        self.session.add(self.model)
        self.session.commit()

    def get_total_images(self):
        total = self.session.query(ImageModel).count()
        return total

    def get_navigate_images(self, index, count):
        images = self.session.query(ImageModel).filter(
            ImageModel.id >= index
        ).limit(count).all()
        return images
