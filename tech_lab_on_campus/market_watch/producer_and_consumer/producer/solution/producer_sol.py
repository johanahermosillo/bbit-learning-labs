import pika
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) --> None:

        #save instance variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        #placeholder
        self.connection = None
        self.channel = None

        #connect to RabbitMQ
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:

        parameters = pika.ConnectionParameters('localhost')