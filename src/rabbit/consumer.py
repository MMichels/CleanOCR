import pika as pk

from src.rabbit import RabbitConector


class RabbitConsumer(RabbitConector):

    def consume(self, callback):
        if self.channel is None:
            self.connect()

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=self.queue,
            auto_ack=True,
            on_message_callback=callback
        )
        self.channel.start_consuming()