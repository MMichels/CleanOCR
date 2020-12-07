import cv2
import json
import logging

from src.image_processing import ImageIoManager
from src.image_processing.filters import ImageFilterApplier
from src.rabbit.consumer import RabbitConsumer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def clean_consumer(ch, method, properties, body):
    logger.info("Recebido: " + str(body))
    message = json.loads(body)
    ioManager = ImageIoManager(message["id"])

    image = ioManager.open_dirty_image()

    imgFilterApp = ImageFilterApplier(image)
    gray_image = imgFilterApp.to_gray_scale()
    background = imgFilterApp.median_filter(23)

    imgFilterApp.image = gray_image
    background = cv2.bitwise_not(background)
    imgFilterApp.add(background)

    ioManager.save_clean_image(imgFilterApp.image)

    ch.basic_ack(delivery_tag=method.delivery_tag)

    return 0


if __name__ == "__main__":
    while True:
        try:
            logger.info("Conectando ao rabbitmq")
            consumer = RabbitConsumer("IMG.Clean")
            logger.info("Consumindo")
            consumer.consume(clean_consumer, auto_ack=False)

        except Exception as e:
            logger.error("Erro ao consumir mensagem", exc_info=True)
