import os
import base64

from sqlalchemy.orm import Session
from models import get_session
from models.image import ImageModel

DIRTY_IMAGE_PATH = "./resources/1.dirty/"
CLANED_IMAGE_PATH = "./resources/2.cleaned/"

os.makedirs(DIRTY_IMAGE_PATH, exist_ok=True)
os.makedirs(DIRTY_IMAGE_PATH, exist_ok=True)


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

    def get_total_images(self):
        total = ImageModel.query.count()
        return total

    def get_navigate_images(self, index, count):
        images = ImageModel.query.filter(
            ImageModel.id >= index
        ).limit(count).all()
        return images
