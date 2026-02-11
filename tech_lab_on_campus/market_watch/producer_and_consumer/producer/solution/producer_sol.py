import pika
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:

        #save instance variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        #placeholder
        self.connection = None
        self.channel = None

        #connect to RabbitMQ
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:

        parameters = pika.ConnectionParameters(host='rabbitmq')

        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

        #Direct exchange type
        self.channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type='direct',
            durable=True
        )

    def publishOrder(self, message: str) -> None:
        if not self.channel or self.channel.is_closed:
            #reconnect in case connection was closed
            self.setupRMQConnection()

        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
        )

        if self.channel and self.channel.is_open:
            self.channel.close()
        if self.connection and self.connection.is_open:
            self.connection.close()