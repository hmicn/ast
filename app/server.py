class Server:
    def __init__(self, asterix_receiver, packet_handler):
        self.__asterix_receiver = asterix_receiver
        self.__packet_handler = packet_handler

    def serve(self):
        while True:
            asterix_packet = self.__asterix_receiver.get_packet()
            self.__packet_handler.handle(asterix_packet)