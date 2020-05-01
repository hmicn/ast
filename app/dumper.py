import os
import json

class Dumper:
    def __init__(self, asterix_receiver):
        self.__asterix_receiver = asterix_receiver
        if not os.path.isdir('dumps'):
            os.makedirs('dumps')

    def serve(self):
        index = 0
        while True:
            asterix_packet = self.__asterix_receiver.get_packet()
            with open(f'dumps/{index}.json', 'w', encoding='utf-8') as fp:
                json.dump(asterix_packet, fp, indent=4) 