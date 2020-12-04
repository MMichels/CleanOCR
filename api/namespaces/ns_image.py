import json
from flask import request
from flask_restplus import Namespace, Resource

from models.image import ImageSchema
from src.services.image_service import ImageService
from src.rabbit.producer import RabbitProducer

from api.request_models.image import post_imagem_model, post_imagem_response_model

ns_image = Namespace("Imagem", "Name space para gerenciar o CRUD das imagens")

upload_image_model = ns_image.model(
    "upload_image_model", post_imagem_model
)
upload_image_response_model = ns_image.model(
    "upload_image_response_model", post_imagem_response_model
)


@ns_image.route("")
class ImageResource(Resource):
    schema = ImageSchema()
    producer = RabbitProducer("IMG.Clean")

    @ns_image.expect(upload_image_model, validate=True)
    @ns_image.marshal_with(upload_image_response_model, code=201)
    def post(self):
        args = request.get_json()
        image_model = self.schema.load(args)
        handler = ImageService(image_model)
        handler.save_dirty_image()

        self.producer.send_message(
            json.dumps({
                "id": image_model.id
            })
        )
        return self.schema.dump(image_model)
