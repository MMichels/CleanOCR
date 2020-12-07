from flask_restplus import fields, reqparse
from . import make_response_model

post_image_model = {
    "base64_encoded_image": fields.String(
        required=True,
        description="Bytes da imagem codificada em base64"
    ),
}

post_image_response_model = {
    "id": fields.Integer(
        required=True,
        description="Id interno da imagem"
    )
}

post_image_response_model = make_response_model(post_image_response_model)

get_image_parser = reqparse.RequestParser()
get_image_parser.add_argument(
    "index",
    type=int,
    default=0,
    location="args",
    required=True,
    help="Index do item inicial da busca (indice da primeira imagem da lista)"
)
get_image_parser.add_argument(
    "count",
    type=int,
    default=10,
    location="args",
    required=True,
    help="Quantidade de elementos retornados a partir do index"
)

get_image_response_model = {
    "total": fields.Integer(
        required=True,
        description="Quantidade total de imagens armazenadas no banco"
    ),
    "images": fields.List(
        fields.Nested({
            "id": fields.Integer(
                required=True,
                description="Id da imagem"
            ),
            "base64_encoded_image": fields.String(
                required=True,
                description="Bytes da imagem encodados em base64"
            ),
            "extracted_text": fields.String(
                required=False,
                description="Texto extraido da imagem utilizando OCR"
            )
        }),
        description="Lista de imagens encontradas")
}

get_image_response_model = make_response_model(get_image_response_model)
