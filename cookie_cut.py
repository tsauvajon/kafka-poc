#
# Receive messages when new images are available
# Download tile image
# Cut each field
#

import json
from random import randrange, choice, seed
from string import ascii_lowercase
from time import sleep

from conf import config
from fake_data import field_names
from topics import image_ready_topic, new_image_topic

from kafka import KafkaConsumer, KafkaProducer


kafka_url = config['kafka']['url']
min, max = config['nb']['min_fields_in_tile'], config['nb']['max_fields_in_tile']
cut_tile_duration = config['duration']['cut_tile']
download_tile_duration = config['duration']['download_tile']

consumer = KafkaConsumer(
    new_image_topic, bootstrap_servers=kafka_url, group_id='cookie_cut')
producer = KafkaProducer(bootstrap_servers=kafka_url)

id = 0
seed()
producer_name = ''.join(choice(ascii_lowercase) for i in range(5))

print('waiting for new tile images...')
for msg in consumer:
    tile = msg.value.decode('utf-8')
    nb_fields = randrange(min, max)

    print(
        f'new_image -> {tile}, contains {nb_fields} fields: downloading...'
    )
    sleep(download_tile_duration)
    print(f'finished downloading {tile}, cutting it')

    for _ in range(nb_fields):
        field = choice(field_names)
        image_id = f'{producer_name}-{id}'
        print(
            f'cut field {field} from tile {tile} into image {image_id} -> image_ready')

        payload = {
            'id': image_id,
            'field': field,
        }
        msg = bytes(json.dumps(payload), 'utf-8')
        producer.send(image_ready_topic, msg)

        id += 1
        sleep(cut_tile_duration)
