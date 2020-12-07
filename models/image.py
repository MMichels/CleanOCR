import marshmallow as ma
from sqlalchemy import Column, Integer, String, Boolean
from models import Base


class ImageModel(Base):
    __tablename__ = "image_model"
    id = Column(Integer, primary_key=True)
    base64_encoded_image = Column(String, nullable=False)
    base64_encoded_processed_image = Column(String, nullable=True)
    extracted_text = Column(String, nullable=True)
    processed = Column(Boolean, default=False)


class ImageSchema(ma.Schema):
    class Meta:
        unknown = ma.EXCLUDE

    id = ma.fields.Integer(dump_only=True)
    base64_encoded_image = ma.fields.String(required=True)
    base64_encoded_processed_image = ma.fields.String(required=False)
    extracted_text = ma.fields.String(required=False)
    processed = ma.fields.Bool(default=False)

    @ma.post_load()
    def make_image(self, data, **kwargs):
        return ImageModel(**data)
