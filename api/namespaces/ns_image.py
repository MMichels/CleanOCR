import json
from flask import request
from flask_restplus import Namespace, Resource

from models.image import ImageModel, ImageSchema
from src.services.image_service import ImageService
from src.rabbit.producer import RabbitProducer

from api.request_models.image import delete_image_model, delete_image_response_model, \
    get_image_parser, get_image_response_model, \
    post_image_model, post_image_response_model

ns_image = Namespace("Imagem", "Name space para gerenciar o CRUD das imagens")

upload_image_model = ns_image.model(
    "upload_image_model", post_image_model
)
upload_image_response_model = ns_image.model(
    "upload_image_response_model", post_image_response_model
)
download_image_response_model = get_image_response_model.copy()

download_image_response_model["images"].container.model = ns_image.model(
    "image_model",
    download_image_response_model["images"].container.model
)

download_image_response_model = ns_image.model("download_image_response_model", download_image_response_model)


exclude_image_model = ns_image.model("exclude_image_model", delete_image_model)
exclude_image_response_model = ns_image.model("exclude_image_response_model", delete_image_response_model)


@ns_image.route("")
class ImageResource(Resource):
    schema = ImageSchema()
    producer = RabbitProducer("IMG.Clean")

    @ns_image.expect(upload_image_model, validate=True)
    @ns_image.marshal_with(upload_image_response_model, code=201)
    def post(self):
        """
        Posta os dados da imagem em Base64
        :return: id
        """
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
    @ns_image.marshal_with(download_image_response_model, code=200)
    def get(self):
        """
        Retorna as imagens que estão salvas na API
        :return:
        """
        args = get_image_parser.parse_args()
        service = ImageService()
        total = service.get_total_images()
        images = service.get_navigate_images(args["index"], args["count"], only_processed=args["only_processed"])
        images = self.schema.dump(images, many=True)

        if args["only_processed"]:
            for image in images:
                image.pop("base64_encoded_image")


        if len(images) > 0:
            return {
                "status": "success",
                "total": total,
                "images": images
            }

        else:
            return {
                "status": "not_found",
                "error": "Não foi encontrado nenhuma imagem para os parametros recebidos"
            }, 204


    @ns_image.expect(exclude_image_model, validate=True)
    @ns_image.marshal_with(exclude_image_response_model, 200)
    def delete(self):
        """
        Exclui uma imagem com base no id
        :return:
        """
        args = request.get_json()
        id = int(args["id"])

        service = ImageService(id=id)
        service.delete()

        return {
            "status": "deleted"
        }, 200
