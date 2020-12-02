from models import db
import marshmallow as ma


class ImageModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    base64_encoded_image = db.Column(db.String, nullable=False)
    extracted_text = db.Column(db.String, nullable=True)
    processed = db.Column(db.Boolean, default=False)


class ImageSchema(ma.Schema):
    class Meta:
        unknown = ma.EXCLUDE

    id = ma.fields.Integer(dump_only=True)
    base64_encoded_image = ma.fields.String(required=True)
    extracted_text = ma.fields.String(required=False)
    processed = ma.fields.Bool(default=False)

    @ma.post_load()
    def make_image(self, data, **kwargs):
        return ImageModel(**data)
