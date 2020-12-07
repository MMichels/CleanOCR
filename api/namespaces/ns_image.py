import json
from flask import request
from flask_restplus import Namespace, Resource

from models.image import ImageModel, ImageSchema
from src.services.image_service import ImageService
from src.rabbit.producer import RabbitProducer

from api.request_models.image import get_image_parser, get_image_response_model, post_image_model, \
    post_image_response_model

ns_image = Namespace("Imagem", "Name space para gerenciar o CRUD das imagens")

upload_image_model = ns_image.model(
    "upload_image_model", post_image_model
)
upload_image_response_model = ns_image.model(
    "upload_image_response_model", post_image_response_model
)

get_image_response_model["images"].container.model = ns_image.model(
    "image_model",
    get_image_response_model["images"].container.model
)

get_image_response_model = ns_image.model("get_image_response_model", get_image_response_model)


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

    @ns_image.expect(get_image_parser, validate=True)
    @ns_image.marshal_with(get_image_response_model, code=200)
    def get(self):
        args = get_image_parser.parse_args()
        service = ImageService()
        total = service.get_total_images()
        images = service.get_navigate_images(args["index"], args["count"])

        if len(images) > 0:
            return {
                "status": "success",
                "total": total,
                "images": self.schema.dump(images, many=True)
            }

        else:
            return {
                "status": "not_found",
                "error": "Não foi encontrado nenhuma imagem para os parametros recebidos"
            }
