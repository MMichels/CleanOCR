from flask_restplus import fields
from . import make_response_model

post_imagem_model = {
    "base64_encoded_image": fields.String(
        required=True,
        description="Bytes da imagem codificada em base64"
    ),
}

post_imagem_response_model = {
    "id": fields.Integer(
        required=True,
        description="Id interno da imagem"
    )
}

post_imagem_response_model = make_response_model(post_imagem_response_model)

