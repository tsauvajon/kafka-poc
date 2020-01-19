#
# Looks for new available images
#

import random
import time

from conf import config
from fake_data import mgrs_tiles
from topics import new_image_topic

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=config['kafka']['url'])


def new_image_available():
    tile = random.choice(mgrs_tiles)
    msg = bytes(tile, 'utf-8')

    producer.send(new_image_topic, msg)
    print(f'sent msg: tile {tile} -> new_image')


while True:
    new_image_available()
    time.sleep(config['duration']['new_image'])
