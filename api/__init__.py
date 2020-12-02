from flask_restplus import Api
from api.namespaces.ns_image import ns_image

api = Api(
    title="CleanOCR",
    description="Api dedicada a realizar a limpeza e extração de texto de uma imagem"
)

api.add_namespace(ns_image, path="/image")
